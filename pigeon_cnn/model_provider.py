from abc import abstractmethod


class ModelProvider:
    """
    Provides network model for CNN
    """

    @abstractmethod
    def provide(self): pass


class HardcodedModelProvider(ModelProvider):
    """
    Provides hardcoded model for CNN
    """

    def provide(self): pass
