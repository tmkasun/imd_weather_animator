from Sattellite import Satellite


class ImageTypes(object):
    def __init__(self, sat_type):
        if sat_type == Satellite.KALPANA1:
            self.COLOR = "COLOR"
            self.INFRARED = "INFRARED"
            self.VISIBLE = "VISIBLE"
            self.WATERVAPOR = "WATERVAPOR"
        elif sat_type == Satellite.INSAT3D:
            self.INFRARED1 = "INFRARED-1"
            self.INFRARED2 = "INFRARED-2"
            self.SWIR = "SWIR"
            self.MID_INFRARED = "MID_INFRARED"
            self.CTBT = "CTBT"
