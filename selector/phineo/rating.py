import logging
import sys
from enum import Enum

import cv2

from selector.phineo.common import IMAGE_TYPE


class LEISTUNGS_XCOORDS(Enum):
    VISION = 10
    LEISTUNGS_GREMIUM = 35
    AUFSICHTS_GREMIUM = 60
    FINANZEN = 78
    FINANZIERUNGSKONZEPT = 105
    OFFENTLICHKEIT = 125


# y coordinates
leistungs_ycoords = [7, 25, 45, 60, 75]


class WIRKUNGS_XCOORDS(Enum):
    ZEILE = 10
    KONZEPT = 30
    QUALITAET = 50


wirkungs_ycoords = [7, 25, 45, 65, 77]


class Rating:
    def __init__(self, image_path, image_type, log_level=logging.ERROR):
        self.img_path = image_path
        self.star = image_type
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(log_level)
        self.handler = logging.StreamHandler(sys.stdout)
        self.logger.addHandler(self.handler)
        if image_type == IMAGE_TYPE.LEISTUNG:
            rows = LEISTUNGS_XCOORDS
            cols = leistungs_ycoords
            self.reputation = self.compute_ratings(rows, cols)
        if image_type == IMAGE_TYPE.WIRK:
            rows = WIRKUNGS_XCOORDS
            cols = wirkungs_ycoords
            self.reputation = self.compute_ratings(rows, cols)

    def to_black_white(self):
        image = cv2.imread(self.img_path)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        min_white = 175
        max_white = 255
        (thresh, bw) = cv2.threshold(gray, min_white, max_white, cv2.THRESH_BINARY)
        return bw

    def get_ratings(self):
        return self.reputation

    def compute_ratings(self, row, col):
        bw = self.to_black_white()
        ratings = {}
        for x in row:
            rating = 0
            for y in col:
                pixel = bw[x.value, y]
                if pixel == 0:
                    rating = rating + 1
            ratings[x] = rating
        return ratings
