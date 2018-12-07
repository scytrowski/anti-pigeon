from anti_pigeon.detectors import AggregatedDetector
import unittest


class DetectorMock:
    def __init__(self, detection_result):
        self._detection_result = detection_result

    def check(self):
        return self._detection_result


class AggregatedDetectorTest(unittest.TestCase):
    def test_detected_by_all_detectors(self):
        detectors = DetectorMock(True), DetectorMock(True)
        aggregated_detector = AggregatedDetector(detectors)
        self.assertTrue(aggregated_detector.check())

    def test_not_detected_by_one_detector(self):
        detectors = DetectorMock(True), DetectorMock(False)
        aggregated_detector = AggregatedDetector(detectors)
        self.assertFalse(aggregated_detector.check())

    def test_not_detected_by_any_detector(self):
        detectors = DetectorMock(False), DetectorMock(False)
        aggregated_detector = AggregatedDetector(detectors)
        self.assertFalse(aggregated_detector.check())
