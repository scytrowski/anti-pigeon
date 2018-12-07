from anti_pigeon.detectors import StrainGaugeDetector
import unittest


class StrainGaugeInterfaceMock:
    def __init__(self, probe):
        self._probe = probe

    def probe(self): return self._probe


class HALMock:
    def __init__(self, strain_gauge_probe):
        self._strain_gauge_probe = strain_gauge_probe

    def strain_gauge(self): return StrainGaugeInterfaceMock(self._strain_gauge_probe)


class StrainGaugeDetectorTest(unittest.TestCase):
    def test_probe_below_threshold(self):
        hal = HALMock(13)
        detector = StrainGaugeDetector(hal, 20)
        self.assertFalse(detector.check())

    def test_probe_equals_threshold(self):
        hal = HALMock(13)
        detector = StrainGaugeDetector(hal, 13)
        self.assertTrue(detector.check())

    def test_probe_above_threshold(self):
        hal = HALMock(13)
        detector = StrainGaugeDetector(hal, 12)
        self.assertTrue(detector.check())
