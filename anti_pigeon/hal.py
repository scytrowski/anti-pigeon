from abc import abstractmethod


# HAL - Hardware Abstraction Layer
class HAL:
    @abstractmethod
    def strain_gauge(self): pass

    @abstractmethod
    def camera(self): pass


class StrainGaugeInterface:
    @abstractmethod
    def probe(self): pass


class CameraInterface:
    @abstractmethod
    def probe(self): pass
