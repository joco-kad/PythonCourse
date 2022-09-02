from dependency_injector.wiring import Provide, inject

from candle_importer.services import EtoroCandleImporterService
from candle_importer.containers import Container


@inject
def main(etoro_candle_importer_service: EtoroCandleImporterService = Provide[Container.etoro_candle_importer_service]):
	etoro_candle_importer_service.start_import()


if __name__ == "__main__":
	container = Container()
	container.init_resources()
	container.wire(modules=[__name__])
	main()
