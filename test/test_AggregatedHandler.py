from anti_pigeon.handlers import AggregatedHandler
import unittest


class HandlerMock:
    def __init__(self):
        self._invoke_counter = 0

    def handle(self):
        self._invoke_counter += 1

    def invoked_once(self):
        return self._invoke_counter == 1


class AggregatedHandlerTest(unittest.TestCase):
    def test_invoked_once_all_handlers(self):
        handlers = HandlerMock(), HandlerMock(), HandlerMock()
        aggregated_handler = AggregatedHandler(handlers)
        aggregated_handler.handle()
        self.assertTrue(all(map(lambda h: h.invoked_once(), handlers)))
