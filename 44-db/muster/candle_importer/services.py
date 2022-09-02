import logging

from pymongo import MongoClient
from pymongo.database import Database
from time import sleep
from pandas import Timestamp, Timedelta
from logging import getLogger, Logger
from utils.trade import calc_period_min
from utils.etoro import CandleBar, EtoroBroker


class EtoroCandleImporterService:
	def __init__(self,
	             etoro_broker: EtoroBroker,
	             mongo_db_url: str,
				 etoro_instrument_ids: str,
	             bar: str,
	             import_wait_time_min: int,
	             keep_alive_time_sec: int):
		self._logger: Logger = getLogger(__name__)
		self._etoro_broker = etoro_broker
		self._mongo_db_url = mongo_db_url
		self._etoro_instrument_ids = etoro_instrument_ids.split()
		self._period_min = import_wait_time_min + 2
		self._bar_min = calc_period_min(bar)
		self._import_wait_time_min = import_wait_time_min
		self._keep_alive_time_sec = keep_alive_time_sec
		self._last_ts_by_ins_id = dict()

	def _import_id(self, db: Database, etoro_instrument_id: str):
		candles: dict = self._etoro_broker.get_trade_candles(
			ins_id=etoro_instrument_id,
			candle_count=self._period_min,
			candle_bar=CandleBar.ONE_MINUTE
		)
		last_date = self._last_ts_by_ins_id.get(etoro_instrument_id)
		candle_list = candles.get('Candles')
		if candle_list is not None and len(candle_list) > 0:
			act_date = candle_list[0]['FromDate']
		else:
			act_date = None
		if act_date == last_date:
			self._logger.info(f'Doppel: {last_date}')
			return

		result = db[f'etoro{etoro_instrument_id}'].insert_one(candles)
		self._last_ts_by_ins_id[etoro_instrument_id] = act_date
		self._logger.info(f'{result.inserted_id}')

	def start_import(self):
		last_ts: Timestamp = Timestamp.utcnow() - Timedelta(minutes=self._import_wait_time_min)
		while True:
			act_ts = Timestamp.utcnow()
			if act_ts - last_ts < Timedelta(minutes=self._import_wait_time_min):
				self._logger.info('keep-alive')
				sleep(self._keep_alive_time_sec)
			else:
				client = MongoClient(self._mongo_db_url)
				try:
					db = client.admin
					if self._logger.isEnabledFor(logging.DEBUG):
						server_status_result = db.command('serverStatus')
						self._logger.debug(server_status_result)
					db: Database = client.etoro_data
					for etoro_instrument_id in self._etoro_instrument_ids:
						self._import_id(db, etoro_instrument_id)
				except Exception as e:
					self._logger.error(f'Fehler bei EToro Instrument-Import: {e}', exc_info=True)
				finally:
					client.close()
				last_ts = Timestamp.utcnow()
