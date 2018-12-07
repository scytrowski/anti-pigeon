from abc import abstractmethod


class ImageAnalyzer:
    @abstractmethod
    def analyze(self, image): pass
