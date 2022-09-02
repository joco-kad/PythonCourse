import logging.config
from dependency_injector import containers, providers

from candle_importer.services import EtoroCandleImporterService, EtoroBroker


class Container(containers.DeclarativeContainer):

    config = providers.Configuration(ini_files=["config.ini"])

    logging = providers.Resource(
        logging.config.fileConfig,
        fname="candle_importer/logging.ini",
    )

    etoro_broker = providers.Factory(
        EtoroBroker,
        etoroapi_baseurl=config.etorobroker.baseurl,
        mode=config.etorobroker.mode
    )

    etoro_candle_importer_service = providers.Factory(
        EtoroCandleImporterService,
        etoro_broker,
        config.mongo.db_url,
        config.candleimport.etoro_instrument_ids,
        config.candleimport.bar,
        config.candleimport.import_wait_time_min.as_int(),
        config.candleimport.keep_alive_time_sec.as_int()
    )
