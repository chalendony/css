import os
import cv2
import imutils

from selector.phineo.common import IMAGE_TYPE
from selector.phineo.rating import (
    LEISTUNGS,
    leistungs_ycoords,
    WIRKUNGS,
    wirkungs_ycoords,
    Rating,
)


def test_check_image():
    image = cv2.imread(os.path.join("data", "leistung.jpg"))
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    (thresh, bw) = cv2.threshold(gray, 175, 255, cv2.THRESH_BINARY)
    assert 144 == bw.shape[0]
    cv2.imshow("b/w image", bw)


def test_ratings_vision():
    rows = LEISTUNGS
    cols = leistungs_ycoords
    image = cv2.imread(os.path.join("data", "leistung.jpg"))
    scale = Rating()
    ratings = scale.compute_ratings(image, IMAGE_TYPE.LEISTUNG)
    assert ratings[LEISTUNGS.VISION] == 4


def test_ratings_leistung():
    rows = LEISTUNGS
    cols = leistungs_ycoords
    image = cv2.imread(os.path.join("data", "leistung.jpg"))
    scale = Rating()
    ratings = scale.compute_ratings(image, IMAGE_TYPE.LEISTUNG)
    assert ratings[LEISTUNGS.LEISTUNGS_GREMIUM] == 4


def test_ratings_aufsichts():
    rows = LEISTUNGS
    cols = leistungs_ycoords
    image = cv2.imread(os.path.join("data", "leistung.jpg"))
    scale = Rating()
    ratings = scale.compute_ratings(image, IMAGE_TYPE.LEISTUNG)
    assert ratings[LEISTUNGS.AUFSICHTS_GREMIUM] == 3


def test_ratings_leistung_finanzen():
    rows = LEISTUNGS
    cols = leistungs_ycoords
    image = cv2.imread(os.path.join("data", "leistung.jpg"))
    scale = Rating()
    ratings = scale.compute_ratings(image, IMAGE_TYPE.LEISTUNG)
    assert ratings[LEISTUNGS.FINANZEN] == 3


def test_ratings_leistung_finanzierungs():
    rows = LEISTUNGS
    cols = leistungs_ycoords
    image = cv2.imread(os.path.join("data", "leistung.jpg"))
    scale = Rating()
    ratings = scale.compute_ratings(image, IMAGE_TYPE.LEISTUNG)
    assert ratings[LEISTUNGS.FINANZIERUNGSKONZEPT] == 5


def test_ratings_leistung_offentlich():
    rows = LEISTUNGS
    cols = leistungs_ycoords
    image = cv2.imread(os.path.join("data", "leistung.jpg"))
    scale = Rating()
    ratings = scale.compute_ratings(image, IMAGE_TYPE.LEISTUNG)
    assert ratings[LEISTUNGS.OFFENTLICHKEIT] == 4


def test_ratings_wirk_konzept():
    rows = WIRKUNGS
    cols = wirkungs_ycoords
    image = cv2.imread(os.path.join("data", "wirk_img.jpg"))
    scale = Rating()
    ratings = scale.compute_ratings(image, IMAGE_TYPE.WIRK)
    assert ratings[WIRKUNGS.KONZEPT] == 5


def test_read_file_from_url():
    rows = WIRKUNGS
    cols = wirkungs_ycoords
    url = "https://www.phineo.org/typo3temp/GB/9ed448bd3f.jpg"
    image = imutils.url_to_image(url)
    scale = Rating()
    ratings = scale.compute_ratings(image, IMAGE_TYPE.WIRK)
    assert ratings[WIRKUNGS.KONZEPT] == 4
