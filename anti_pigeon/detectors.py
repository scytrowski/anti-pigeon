from abc import abstractmethod


class Detector:
    def __init__(self, hal):
        self._hal = hal

    @abstractmethod
    def check(self): pass


class StrainGaugeDetector(Detector):
    def __init__(self, hal, threshold):
        super().__init__(hal)
        self._threshold = threshold

    def check(self):
        strain_gauge_probe = self._hal.strain_gauge().probe()
        return strain_gauge_probe >= self._threshold


class CameraDetector(Detector):
    def __init__(self, hal, image_analyzer):
        super().__init__(hal)
        self._image_analyzer = image_analyzer

    def check(self):
        camera_image = self._hal.camera().probe()
        return self._image_analyzer.analyze(camera_image)
