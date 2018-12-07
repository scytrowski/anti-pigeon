from abc import abstractmethod


class Handler:
    """
    Handler abstraction
    """
    @abstractmethod
    def handle(self): pass


class AggregatedHandler(Handler):
    """
    Aggregates many handlers
    """
    def __init__(self, handlers):
        self._handlers = handlers

    def handle(self):
        for handler in self._handlers:
            handler.handle()


class HALBackedHandler(Handler):
    """
    Uses HAL interfaces in detection process
    """
    def __init__(self, hal):
        self._hal = hal

    @abstractmethod
    def handle(self): pass


class WoodcutterAxeHandler(HALBackedHandler):
    """
    CHOP, CHOP, CHOP!!!
    """
    def __init__(self, hal):
        super().__init__(hal)

    @abstractmethod
    def handle(self):
        self._hal.woodcutter_axe().chop()
