from anti_pigeon.hal import HAL
from .strain_gauge import RPiStrainGaugeInterface
from .camera import RPiCameraInterface
from .woodcutter_axe import RPiWoodcutterAxeInterface


class RPiHAL(HAL):
    """
    Default HAL used in the project
    """

    def __init__(self):
        self._strain_gauge = RPiStrainGaugeInterface()
        self._camera = RPiCameraInterface()
        self._woodcutter_axe = RPiWoodcutterAxeInterface()

    def setup(self): pass

    def cleanup(self): pass

    def strain_gauge(self):
        return self._strain_gauge

    def camera(self):
        return self._camera

    def woodcutter_axe(self):
        return self._woodcutter_axe
