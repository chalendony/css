import logging
import sys
from enum import Enum

import cv2

from selector.phineo.common import IMAGE_TYPE


class LEISTUNGS(Enum):
    VISION = 10
    LEISTUNGS_GREMIUM = 35
    AUFSICHTS_GREMIUM = 60
    FINANZEN = 78
    FINANZIERUNGSKONZEPT = 105
    OFFENTLICHKEIT = 125


# y coordinates
leistungs_ycoords = [7, 25, 45, 60, 75]


class WIRKUNGS(Enum):
    ZEILE = 10
    KONZEPT = 30
    QUALITAET = 50


wirkungs_ycoords = [7, 25, 45, 65, 77]


class Rating:
    def __init__(self, log_level=logging.ERROR):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(log_level)
        self.handler = logging.StreamHandler(sys.stdout)
        self.logger.addHandler(self.handler)

    def to_black_white(self, image):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        min_white = 175
        max_white = 255
        (thresh, bw) = cv2.threshold(gray, min_white, max_white, cv2.THRESH_BINARY)
        return bw


    def compute_ratings(self, data, image_type):
        if image_type == IMAGE_TYPE.LEISTUNG:
            rows = LEISTUNGS
            cols = leistungs_ycoords
        if image_type == IMAGE_TYPE.WIRK:
            rows = WIRKUNGS
            cols = wirkungs_ycoords
        bw = self.to_black_white(data)
        res = {}
        for x in rows:
            rating = 0
            for y in cols:
                pixel = bw[x.value, y]
                if pixel == 0:
                    rating = rating + 1
            res[x.__str__().lower()] = rating
        return res
