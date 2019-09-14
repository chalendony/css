import os
import cv2
import imutils

from selector.phineo.common import IMAGE_TYPE
from selector.phineo.rating import (
    LEISTUNGS_XCOORDS,
    leistungs_ycoords,
    WIRKUNGS_XCOORDS,
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
    image = cv2.imread(os.path.join("data", "leistung.jpg"))
    scale = Rating()
    ratings = scale.compute_ratings(image, IMAGE_TYPE.LEISTUNG)
    rows = LEISTUNGS_XCOORDS
    cols = leistungs_ycoords
    assert ratings[LEISTUNGS_XCOORDS.VISION] == 4


def test_ratings_leistung():
    image = cv2.imread(os.path.join("data", "leistung.jpg"))
    scale = Rating()
    rows = LEISTUNGS_XCOORDS
    cols = leistungs_ycoords
    ratings = scale.compute_ratings(image, IMAGE_TYPE.LEISTUNG)
    assert ratings[LEISTUNGS_XCOORDS.LEISTUNGS_GREMIUM] == 4


def test_ratings_aufsichts():
    image = cv2.imread(os.path.join("data", "leistung.jpg"))
    scale = Rating()
    rows = LEISTUNGS_XCOORDS
    cols = leistungs_ycoords
    ratings = scale.compute_ratings(image, IMAGE_TYPE.LEISTUNG)
    assert ratings[LEISTUNGS_XCOORDS.AUFSICHTS_GREMIUM] == 3


def test_ratings_leistung_finanzen():
    image = cv2.imread(os.path.join("data", "leistung.jpg"))
    scale = Rating()
    rows = LEISTUNGS_XCOORDS
    cols = leistungs_ycoords
    ratings = scale.compute_ratings(image, IMAGE_TYPE.LEISTUNG)
    assert ratings[LEISTUNGS_XCOORDS.FINANZEN] == 3


def test_ratings_leistung_finanzierungs():
    image = cv2.imread(os.path.join("data", "leistung.jpg"))
    scale = Rating()
    rows = LEISTUNGS_XCOORDS
    cols = leistungs_ycoords
    ratings = scale.compute_ratings(image, IMAGE_TYPE.LEISTUNG)
    assert ratings[LEISTUNGS_XCOORDS.FINANZIERUNGSKONZEPT] == 5


def test_ratings_leistung_offentlich():
    image = cv2.imread(os.path.join("data", "leistung.jpg"))
    scale = Rating()
    rows = LEISTUNGS_XCOORDS
    cols = leistungs_ycoords
    ratings = scale.compute_ratings(image, IMAGE_TYPE.LEISTUNG)
    assert ratings[LEISTUNGS_XCOORDS.OFFENTLICHKEIT] == 4


def test_ratings_wirk_konzept():
    image = cv2.imread(os.path.join("data", "wirk_img.jpg"))
    scale = Rating()
    rows = WIRKUNGS_XCOORDS
    cols = wirkungs_ycoords
    ratings = scale.compute_ratings(image, IMAGE_TYPE.WIRK)
    assert ratings[WIRKUNGS_XCOORDS.KONZEPT] == 5


def test_read_file_from_url():
    url = 'https://www.phineo.org/typo3temp/GB/9ed448bd3f.jpg'
    image = imutils.url_to_image(url)
    scale = Rating()
    rows = WIRKUNGS_XCOORDS
    cols = wirkungs_ycoords
    ratings = scale.compute_ratings(image, IMAGE_TYPE.WIRK)
    assert ratings[WIRKUNGS_XCOORDS.KONZEPT] == 4
