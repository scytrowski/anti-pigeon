from abc import abstractmethod


class ImageAnalyzer:
    """
    Image analyzer abstraction
    """
    @abstractmethod
    def analyze(self, image): pass
