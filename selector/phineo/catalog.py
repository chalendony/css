import hashlib
import logging
import sys
from collections import namedtuple

import imutils
import pandas as pd
from requests_html import HTMLSession

from selector.phineo.common import IMAGE_TYPE
from selector.phineo.rating import Rating

import json

session = HTMLSession()


PROJ_PER_PAGE = 10
last_page = 25
base_url = "https://www.phineo.org/"

# catalog metadata
language = "germany"
source_name = "phineo"
source_website = "https://www.phineo.org/"

Entry = namedtuple(
    "Entry",
    [
        "id",
        "name",
        "tagline",
        "mission",
        "location",
        "geo_reach",
        "category",
        "rating",
        "key_visual",
        "target_group",
        "home_page",
    ],
)


class Catalog:
    def __init__(self, log_level=logging.ERROR):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(log_level)
        self.handler = logging.StreamHandler(sys.stdout)
        self.logger.addHandler(self.handler)
        self.ids = []
        self.COUNTER = 0
        self.LIMIT = 5

    def build(self):
        cat = []
        pages = self.list_all_pages()
        self.logger.debug(f"Total pages: {len(pages)}")
        rater = Rating()
        self.logger.info(f"Building Catalog .....")
        for page in pages:
            for project_url in self.get_projects(page):
                id_m = hashlib.md5(project_url.encode("utf-8")).hexdigest()
                url = base_url + project_url
                name_m = self.name(url)
                tagline_m = self.tagline(url)
                mission_m = self.mission(url)
                location_m = self.location(url)
                geo_reach_m = self.geo_reach(url)
                category_m = self.category(url)
                img_rating = self.rating(url)
                input_image = imutils.url_to_image(base_url + img_rating)
                rating_m = rater.compute_ratings(input_image, IMAGE_TYPE.WIRK)
                key_visual_m = self.key_visual(url)
                target_group_m = self.target_group(url)
                home_page_m = self.home_page(url)
                e = {
                    "id": id_m,
                    "name": name_m,
                    "tagline": tagline_m,
                    "mission": mission_m,
                    "location": location_m,
                    "goe_reach": geo_reach_m,
                    "category": category_m,
                    "rating": rating_m,
                    "key_visual": key_visual_m,
                    "target_group": target_group_m,
                    "home_page": home_page_m,
                }
                cat.append(e)
                #self.COUNTER = self.COUNTER + 1
                #if self.COUNTER == self.LIMIT:
                #    self.trydump(cat)
        self.logger.info(f"Catalog built with {len(cat)} records")
        return cat

    def trydump(self, cat):
        with open('phineo.json', 'w') as f:
            f.write(json.dumps(cat))
        exit(1)

    def is_duplicated_ids(self):
        return not len(self.ids) == len(set(self.ids))

    def list_all_pages(self):
        pages = []
        for i in range(0, last_page):
            url = f"https://www.phineo.org/projekte?tx_phineoprojectslite_pi1%5Bpps%5D={PROJ_PER_PAGE}&tx_phineoprojectslite_pi1%5Bpointer%5D={i}"
            pages.append(url)
        return pages

    def get_projects(self, url):
        lst = []
        r = session.get(url)
        for i in range(1, 12):
            selector = f"#searchresults > div:nth-child({i}) > div.teaserImage.leftStyle.width_232 > a"
            res = r.html.find(selector)
            if len(res) > 0:
                #!RECALL : access the element by pulling it out of the list and then get the elements attributes...
                res = res[0].attrs.get("href")
                lst.append(res)
        return lst

    def get_metadata_extractors(self):
        lst = []
        lst.append(self.name)
        lst.append(self.tagline)
        lst.append(self.mission)
        lst.append(self.location)
        lst.append(self.geo_reach)
        lst.append(self.category)
        lst.append(self.rating)
        lst.append(self.key_visual)
        lst.append(self.target_group)
        lst.append(self.home_page)
        return lst

    #########################################################################
    # @meta
    def category(self, url):
        metadata = None
        selector = "#c9293 > div > div > div.marginLeft_08 > div > div.leftStyle.marginTop_16.paddingBottom_16 > div.subc.width_472.leftStyle > div:nth-child(1) > div > dl:nth-child(1) > dd > a"
        r = session.get(url)
        res = r.html.find(selector)
        self.logger.debug(res)
        if len(res) > 0:
            metadata = res[0].text
        return metadata

    # @meta
    def target_group(self, url):
        metadata = None
        selector = "#c9293 > div > div > div.marginLeft_08 > div > div.leftStyle.marginTop_16.paddingBottom_16 > div.subc.width_472.leftStyle > div:nth-child(1) > div > dl:nth-child(2) > dd"
        r = session.get(url)
        res = r.html.find(selector)
        self.logger.debug(f"*************** {res}")
        if len(res) > 0:
            metadata = res[0].text.split(",")
        return metadata

    # @meta
    def location(self, url):
        selector = "#c9293 > div > div > div.marginLeft_08 > div > div.leftStyle.marginTop_16.paddingBottom_16 > div.subc.width_472.leftStyle > div:nth-child(2) > div > dl:nth-child(1) > dd > a"
        r = session.get(url)
        res = r.html.find(selector)
        res = res[0].text
        self.logger.debug(f"*************** {res}")
        return res

    # @meta
    def geo_reach(self, url):
        metadata = None
        selector = "#c9293 > div > div > div.marginLeft_08 > div > div.leftStyle.marginTop_16.paddingBottom_16 > div.subc.width_472.leftStyle > div:nth-child(2) > div > dl:nth-child(2) > dd > a"
        r = session.get(url)
        res = r.html.find(selector)
        self.logger.debug(f"*************** {res}")
        if len(res) > 0:
            metadata = res[0].text
        return metadata

    # @meta
    def mission(self, url):
        metadata = None
        selector = "#c9293 > div > div > div.marginLeft_08 > div > div:nth-child(3) > div.width_552.marginTop_12.marginRight_24 > div:nth-child(1) > p"
        r = session.get(url)
        res = r.html.find(selector)
        self.logger.debug(f"*************** {res}")
        if len(res) > 0:
            metadata = res[0].text
        return metadata

    # @meta
    def rating(self, url):
        metadata = None
        selector = "#c9293 > div > div > div.marginLeft_08 > div > div:nth-child(5) > div.leftStyle.marginTop_12 > div:nth-child(1) > div > img"
        r = session.get(url)
        res = r.html.find(selector)
        self.logger.debug(f"*************** {res}")
        if len(res) > 0:
            metadata = res[0].attrs.get("src")  # get tags's attribute
        return metadata

    # @meta # omit for now ...
    def leistungs_image(self, url):
        metadata = None
        selector = "#c9293 > div > div > div.marginLeft_08 > div > div:nth-child(5) > div.leftStyle.marginTop_12 > div:nth-child(2) > div > img"
        r = session.get(url)
        res = r.html.find(selector)
        self.logger.debug(f"*************** {res}")
        if len(res) > 0:
            metadata = res[0].attrs.get("src")  # get tags's attribute
        return metadata

    # @meta
    def home_page(self, url):
        metadata = None
        selector = "#c9293 > div > div > div.marginLeft_08 > div > div.leftStyle.marginTop_16.paddingBottom_16 > div.subc.width_472.leftStyle > div.subc.clearBox.defaultBox_01.leftStyle > ul > li:nth-child(3) > a"
        r = session.get(url)
        res = r.html.find(selector)
        self.logger.debug(f"*************** {res}")
        if len(res) > 0:
            metadata = res[0].attrs.get("href")
        return metadata

    # @meta
    def name(self, url):
        metadata = None
        selector = "#c9293 > div > div > div.marginLeft_08 > div > div.dottedLine.color_02.paddingBottom_12 > h1"
        r = session.get(url)
        res = r.html.find(selector)
        self.logger.debug(f"*************** {res}")
        if len(res) > 0:
            metadata = res[0].text
        return metadata

    # @meta
    def tagline(self, url):
        metadata = None
        selector = "#c9293 > div > div > div.marginLeft_08 > div > div.dottedLine.color_02.paddingBottom_12 > h2"
        r = session.get(url)
        res = r.html.find(selector)
        self.logger.debug(f"*************** {res}")
        if len(res) > 0:
            metadata = res[0].text
        return metadata

    # @meta
    def key_visual(self, url):
        metadata = None
        selector = "#c9293 > div > div > div.marginLeft_08 > div > div:nth-child(3) > div.width_552.marginTop_12.marginRight_24 > div:nth-child(2) > img"
        r = session.get(url)
        res = r.html.find(selector)
        self.logger.debug(f"*************** {res}")
        if len(res) > 0:
            metadata = res[0].attrs.get("src")
        return metadata

    # @meta
    def long_description(self):
        # TODO: Later
        selector = "#c9293 > div > div > div.marginLeft_08 > div > div:nth-child(4) > div.width_552.marginTop_12.marginRight_24 > div"
        pass
