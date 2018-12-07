from abc import abstractmethod


class HAL:
    """
    HAL - Hardware Abstraction Layer
    """
    @abstractmethod
    def strain_gauge(self): pass

    @abstractmethod
    def camera(self): pass

    @abstractmethod
    def woodcutter_axe(self): pass


class StrainGaugeInterface:
    """
    Strain gauge abstraction
    """
    @abstractmethod
    def probe(self): pass


class CameraInterface:
    """
    Camera abstraction
    """
    @abstractmethod
    def probe(self): pass


class WoodcutterAxeInterface:
    """
    Chop some pigeo... ups, wood!
    """
    @abstractmethod
    def chop(self): pass
