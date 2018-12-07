from anti_pigeon.detectors import CameraDetector
import unittest


class CameraInterfaceMock:
    def __init__(self, image):
        self._image = image

    def probe(self):
        return self._image


class HALMock:
    def __init__(self, camera_image):
        self._camera_image = camera_image

    def camera(self):
        return CameraInterfaceMock(self._camera_image)


class ImageAnalyzerMock:
    def __init__(self, analyze_result):
        self._analyze_result = analyze_result

    def analyze(self, _):
        return self._analyze_result


class CameraDetectorTest(unittest.TestCase):
    def test_positive_analyze(self):
        hal = HALMock(object())
        image_analyzer = ImageAnalyzerMock(True)
        camera_detector = CameraDetector(hal, image_analyzer)
        self.assertTrue(camera_detector.check())

    def test_negative_analyze(self):
        hal = HALMock(object())
        image_analyzer = ImageAnalyzerMock(False)
        camera_detector = CameraDetector(hal, image_analyzer)
        self.assertFalse(camera_detector.check())
