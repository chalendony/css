import logging
import sys
import inspect
import hashlib

from requests_html import HTMLSession

session = HTMLSession()

PROJ_PER_PAGE = 10
last_page = 25
base_url = 'https://www.phineo.org/'


def set_property():
    pass


class Catalog:
    def __init__(self, log_level=logging.ERROR):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(log_level)
        self.handler = logging.StreamHandler(sys.stdout)
        self.logger.addHandler(self.handler)

    def build(self):
        count = 0
        pages = self.list_all_pages()
        self.logger.debug(f"Total pages: {len(pages)}")
        for page in pages:
            for project_url in self.get_projects(page):
                project_id = hashlib.md5(project_url).hexdigest()
                url = base_url + project_url
                theme = self.themen(url)
                # for extractor in self.get_extractors():
                #     logging.info(f"Launching Extractor : {extractor.__name__}")
                #     url = base_url + project_url
                #     res = extractor(url)

        return count


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

    def get_extractors(self):
        """some introspection needed ..."""
        lst=[]
        lst.append(self.themen)
        lst.append(self.wirk_image)
        lst.append(self.zielgruppe)
        lst.append(self.standort)
        lst.append(self.auf_einen_blick)
        lst.append(self.leistungs_image)
        lst.append(self.project_website)
        return lst

    @set_property
    def themen(self, url):
        selector = "#c9293 > div > div > div.marginLeft_08 > div > div.leftStyle.marginTop_16.paddingBottom_16 > div.subc.width_472.leftStyle > div:nth-child(1) > div > dl:nth-child(1) > dd > a"
        r = session.get(url)
        res = r.html.find(selector)[0].text
        self.logger.info(res)
        return res

    @set_property
    def zielgruppe(self, url):
        selector = "#c9293 > div > div > div.marginLeft_08 > div > div.leftStyle.marginTop_16.paddingBottom_16 > div.subc.width_472.leftStyle > div:nth-child(1) > div > dl:nth-child(2) > dd"
        r = session.get(url)
        res = r.html.find(selector)
        print(res)
        res = res[0].text.split(",")
        self.logger.debug(f"*************** {res}")
        return res

    @set_property
    def standort(self, url):
        selector = "#c9293 > div > div > div.marginLeft_08 > div > div.leftStyle.marginTop_16.paddingBottom_16 > div.subc.width_472.leftStyle > div:nth-child(2) > div > dl:nth-child(1) > dd > a"
        r = session.get(url)
        res = r.html.find(selector)
        res = res[0].text
        self.logger.debug(f"*************** {res}")
        return res

    @set_property
    def reichweite(self, url):
        selector = "#c9293 > div > div > div.marginLeft_08 > div > div.leftStyle.marginTop_16.paddingBottom_16 > div.subc.width_472.leftStyle > div:nth-child(2) > div > dl:nth-child(2) > dd > a"
        r = session.get(url)
        res = r.html.find(selector)
        res = res[0].text
        self.logger.debug(f"*************** {res}")
        return res

    @set_property
    def auf_einen_blick(self, url):
        selector = "#c9293 > div > div > div.marginLeft_08 > div > div:nth-child(3) > div.width_552.marginTop_12.marginRight_24 > div:nth-child(1) > p"
        r = session.get(url)
        res = r.html.find(selector)
        res = res[0].text
        self.logger.debug(f"*************** {res}")
        return res

    @set_property
    def wirk_image(self, url):
        selector = "#c9293 > div > div > div.marginLeft_08 > div > div:nth-child(5) > div.leftStyle.marginTop_12 > div:nth-child(1) > div > img"
        r = session.get(url)
        res = r.html.find(selector)[0].attrs.get("src")  # get tags's attribute
        self.logger.debug(f"*************** {res}")
        return res

    @set_property
    def leistungs_image(self, url):
        selector = "#c9293 > div > div > div.marginLeft_08 > div > div:nth-child(5) > div.leftStyle.marginTop_12 > div:nth-child(2) > div > img"
        r = session.get(url)
        res = r.html.find(selector)[0].attrs.get("src")  # get tags's attribute
        self.logger.debug(f"*************** {res}")
        return res

    @set_property
    def project_website(self, url):
        selector = "#c9293 > div > div > div.marginLeft_08 > div > div.leftStyle.marginTop_16.paddingBottom_16 > div.subc.width_472.leftStyle > div.subc.clearBox.defaultBox_01.leftStyle > ul > li:nth-child(3) > a"
        r = session.get(url)
        print(r)
        res = r.html.find(selector)[0].attrs.get("href")
        self.logger.debug(f"*************** {res}")
        return res

    @set_property
    def title(self):
        pass