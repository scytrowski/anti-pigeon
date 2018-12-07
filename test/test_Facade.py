from anti_pigeon.facade import Facade
import unittest


class DetectorMock:
    def __init__(self, detection_result):
        self._detection_result = detection_result

    def check(self):
        return self._detection_result


class HandlerMock:
    def __init__(self):
        self._handle_counter = 0

    def handle(self):
        self._handle_counter += 1

    def not_invoked(self):
        return self._handle_counter == 0

    def invoked_once(self):
        return self._handle_counter == 1


class FacadeTest(unittest.TestCase):
    def test_handled_if_detected(self):
        detector = DetectorMock(True)
        handler = HandlerMock()
        facade = Facade((detector,), (handler,))
        facade.detect_and_handle()
        self.assertTrue(handler.invoked_once())

    def test_not_handled_if_not_detected(self):
        detector = DetectorMock(False)
        handler = HandlerMock()
        facade = Facade((detector,), (handler,))
        facade.detect_and_handle()
        self.assertTrue(handler.not_invoked())
