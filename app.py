from anti_pigeon.detectors import *
from anti_pigeon.handlers import *
from anti_pigeon.facade import Facade
from rpi_hal.hal import RPiHAL


HAL = RPiHAL()

IMAGE_ANALYZER = object()

DETECTORS = (
    StrainGaugeDetector(HAL, 10),
    CameraDetector(HAL, IMAGE_ANALYZER))

HANDLERS = (
    WoodcutterAxeHandler(HAL),)


def main():
    try:
        HAL.setup()
        facade = Facade(DETECTORS, HANDLERS)
        while True:
            facade.detect_and_handle()
    except KeyboardInterrupt:
        return
    finally:
        HAL.cleanup()


if __name__ == "__main__":
    main()
