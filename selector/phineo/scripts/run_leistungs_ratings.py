from phineo.rating import ProjectRating
from enum import Enum
import  logging
from phineo.common import IMAGE_TYPE



if __name__ == '__main__':
    star = ProjectRating('../test/data/leistung.jpg', IMAGE_TYPE.LEISTUNG, log_level=logging.DEBUG)