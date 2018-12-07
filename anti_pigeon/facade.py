from .detectors import AggregatedDetector
from .handlers import AggregatedHandler


class Facade:
    """
    Used to connect all the submodules
    """

    def __init__(self, detectors, handlers):
        self._detector = AggregatedDetector(detectors)
        self._handler = AggregatedHandler(handlers)

    def detect_and_handle(self):
        detection_result = self._detector.check()
        if detection_result:
            self._handler.handle()
