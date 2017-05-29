from ImageTypes import ImageTypes


class Satellite(object):
    """
    http://satellite.imd.gov.in/dynamic/satfaq.pdf
    """
    INSAT3D = "INSAT-3D-IMAGER"
    KALPANA1 = "KALPANA-1"
    BASE_URL = "http://satellite.imd.gov.in/archive/"

    def __init__(self, sat_name):
        self.image_type = None
        self.name = sat_name
        self.image_types = ImageTypes(sat_name)

    def get_URL(self):
        full_url = Satellite.BASE_URL
        if self.name == Satellite.KALPANA1:
            full_url += self.name + "/ASIA-SECTOR/"
        elif self.name == Satellite.INSAT3D:
            full_url += self.name + "/3D-ASIA-SECTOR/"

        return full_url + self.image_type + "/MAY_2017/"

    def set_image_type(self, image_type):
        self.image_type = image_type

    def get_image_type(self):
        return self.image_type
