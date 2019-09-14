import logging

from selector.phineo.common import IMAGE_TYPE
from selector.phineo.rating import Rating

if __name__ == "__main__":
    star = Rating(
        "../test/data/leistung.jpg", IMAGE_TYPE.LEISTUNG, log_level=logging.DEBUG
    )
