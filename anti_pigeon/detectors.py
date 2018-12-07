from abc import abstractmethod


class Detector:
    """
    Detector abstraction
    """
    @abstractmethod
    def check(self): pass


class AggregatedDetector(Detector):
    """
    Aggregates results of many detectors
    """
    def __init__(self, aggregators):
        self._aggregators = aggregators

    def check(self):
        return all(map(lambda d: d.check(), self._aggregators))


class HALBackedDetector(Detector):
    """
    Uses HAL interfaces in detection process
    """
    def __init__(self, hal):
        self._hal = hal

    @abstractmethod
    def check(self): pass


class StrainGaugeDetector(HALBackedDetector):
    """
    Strain gauge detector implementation
    """
    def __init__(self, hal, threshold):
        super().__init__(hal)
        self._threshold = threshold

    def check(self):
        strain_gauge_probe = self._hal.strain_gauge().probe()
        return strain_gauge_probe >= self._threshold


class CameraDetector(HALBackedDetector):
    """
    Camera detector implementation
    """
    def __init__(self, hal, image_analyzer):
        super().__init__(hal)
        self._image_analyzer = image_analyzer

    def check(self):
        camera_image = self._hal.camera().probe()
        return self._image_analyzer.analyze(camera_image)
