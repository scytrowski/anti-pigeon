from anti_pigeon.handlers import WoodcutterAxeHandler
import unittest


class HALMock:
    def __init__(self):
        self._woodcutter_axe = WoodcutterAxeInterfaceMock()

    def woodcutter_axe(self):
        return self._woodcutter_axe

    def chopped_once(self):
        return self._woodcutter_axe.invoked_once()


class WoodcutterAxeInterfaceMock:
    def __init__(self):
        self._chop_counter = 0

    def chop(self):
        self._chop_counter += 1

    def invoked_once(self):
        return self._chop_counter == 1


class WoodcutterAxeHandlerTest(unittest.TestCase):
    def test_woodcutter_axe_chopped(self):
        hal = HALMock()
        handler = WoodcutterAxeHandler(hal)
        handler.handle()
        self.assertTrue(hal.chopped_once())
