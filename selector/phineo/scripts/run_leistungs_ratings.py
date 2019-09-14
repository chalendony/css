from selector.phineo.rating import Rating, IMAGE_TYPE
from enum import Enum
import logging
from selector.phineo.common import IMAGE_TYPE


if __name__ == "__main__":
    star = Rating(
        "../test/data/leistung.jpg", IMAGE_TYPE.LEISTUNG, log_level=logging.DEBUG
    )
