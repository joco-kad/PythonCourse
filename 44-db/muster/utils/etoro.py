from requests import Request, Session, Response
from enum import Enum
from typing import NamedTuple


class CandleBar(Enum):
	ONE_MINUTE = 'OneMinute'
	FIVE_MINUTES = 'FiveMinutes'
	FIFTEEN_MINUTES = 'FifteenMinutes'
	THIRTY_MINUTES = 'ThirtyMinutes'
	ONE_HOUR = 'OneHour'
	FOUR_HOURS = 'FourHours'
	ONE_DAY = 'OneDay'
	ONE_WEEK = 'OneWeek'

	@property
	def minutes(self) -> int:
		if self.value == 'OneMinute':
			return 1
		if self.value == 'FiveMinutes':
			return 5
		if self.value == 'FifteenMinutes':
			return 15
		if self.value == 'ThirtyMinutes':
			return 30
		if self.value == 'OneHour':
			return 60
		if self.value == 'FourHours':
			return 4 * 60
		if self.value == 'OneDay':
			return 24 * 60
		if self.value == 'OneWeek':
			return 7 * 24 * 60

	@property
	def etoro_bar(self) -> str:
		return self.value

	@property
	def freq(self) -> str:
		if self.value == 'OneMinute':
			return 'T'
		if self.value == 'FiveMinutes':
			return '5T'
		if self.value == 'FifteenMinutes':
			return '15T'
		if self.value == 'ThirtyMinutes':
			return '30T'
		if self.value == 'OneHour':
			return '1H'
		if self.value == 'FourHours':
			return '4H'
		if self.value == 'OneDay':
			return f'24H'
		if self.value == 'OneWeek':
			return f'{7 * 24}H'


class EtoroTradeType(Enum):
	BUY = 'BUY'
	SELL = 'SELL'


class EtoroOpenPosition(NamedTuple):
	symbol: str
	trade_type: EtoroTradeType
	amount: float
	leverage: int
	rate: float
	tp_rate: float
	sl_rate: float


class EtoroBroker:
	def __init__(self, etoroapi_baseurl: str, mode='demo'):
		self._etoroapi_baseurl = etoroapi_baseurl
		self._mode = mode

	@staticmethod
	def _request(url: str, method='GET', headers: dict = None, body: dict = None) -> Response:
		request = Request(method, url)
		if headers is not None:
			request.headers = headers
		if body is not None:
			request.json = body

		response: Response = Session().send(request.prepare())

		if response.status_code != 200:
			raise Exception(f"Fehler {url} (HTTP {response.status_code}): {response.text}")

		return response

	def get_cash(self) -> float:
		url = f'{self._etoroapi_baseurl}/account/cash'
		response: Response = self._request(url=url, headers={'mode': self._mode})
		return float(response.text)

	def get_trade_candles(self, ins_id: str, candle_count: int, candle_bar: CandleBar) -> dict:
		url = f'https://candle.etoro.com/candles/desc.json/{candle_bar.etoro_bar}/{candle_count}/{ins_id}'
		response: Response = self._request(url=url)
		candles_dict_list = response.json()['Candles']
		if candles_dict_list is None or len(candles_dict_list) == 0:
			return None
		all_candle_dicts = []
		ins_id = None
		for candles_dict in candles_dict_list:
			candles_item_list = candles_dict['Candles']
			act_ins_id = candles_dict['InstrumentId']
			if ins_id is None:
				ins_id = act_ins_id
			if ins_id != act_ins_id:
				raise ValueError('Inkonsistente InstrumentIds')
			for candle_dict in candles_item_list:
				all_candle_dicts.append(candle_dict)
		ret_candles_dict_list = {
			'InstrumentId': ins_id,
			'Candles': all_candle_dicts
		}
		return ret_candles_dict_list

	def open_position(self, op: EtoroOpenPosition) -> dict:
		url = f'{self._etoroapi_baseurl}/positions/open'
		body = {'symbol': op.symbol,
		        'type': op.trade_type.value,
				'amount': op.amount,
		        'leverage': op.leverage,
		        'rate': op.rate,
		        'takeProfitRate': op.tp_rate,
		        'stopLossRate': op.sl_rate}

		response: Response = self._request(url=url, headers={'mode': self._mode}, method='POST', body=body)
		return response.json()


