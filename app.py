from anti_pigeon.detectors import *
from anti_pigeon.handlers import *
from anti_pigeon.facade import Facade
from rpi_hal.hal import RPiHAL


def main():
    try:
        hal = RPiHAL()
        image_analyzer = object()
        detectors = (
            StrainGaugeDetector(hal, 10),
            CameraDetector(hal, image_analyzer))
        handlers = (
            WoodcutterAxeHandler(hal),)
        facade = Facade(detectors, handlers)
        while True:
            facade.detect_and_handle()
    except KeyboardInterrupt:
        return


if __name__ == "__main__":
    main()
