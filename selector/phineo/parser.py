import logging
import os
import sys
from string import Template

from bs4 import BeautifulSoup
import requests
from requests_html import HTML
from requests_html import HTMLSession

session = HTMLSession()

## !!! RECALL : access the element by pulling it out of the list

#base = 'https://www.phineo.org/projekte?tx_phineoprojectslite_pi1%5Bpps%5D=25&tx_phineoprojectslite_pi1%5Bpointer%5D='
#home = 'https://www.phineo.org/projekte'

# TODO : add logger instead of print
PROJ_PER_PAGE = 10
last_page = 25

class Catalog:

    def __init__(self, log_level=logging.ERROR):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(log_level)
        self.handler = logging.StreamHandler(sys.stdout)
        self.logger.addHandler(self.handler)
        self.metadata = None

    def pager(self):
        self.flipBoxPages()
        #turn page()


    def themen(self, url):
        selector = '#c9293 > div > div > div.marginLeft_08 > div > div.leftStyle.marginTop_16.paddingBottom_16 > div.subc.width_472.leftStyle > div:nth-child(1) > div > dl:nth-child(1) > dd > a'
        r = session.get(url)
        res =  r.html.find(selector)
        return res.text

    def zielgruppe(self,url):
        selector = '#c9293 > div > div > div.marginLeft_08 > div > div.leftStyle.marginTop_16.paddingBottom_16 > div.subc.width_472.leftStyle > div:nth-child(1) > div > dl:nth-child(2) > dd'
        r = session.get(url)
        res = r.html.find(selector)
        res = res[0].text.split(',')
        print(f"*************** {res}")
        return res

    def standort(self, url):
        selector = '#c9293 > div > div > div.marginLeft_08 > div > div.leftStyle.marginTop_16.paddingBottom_16 > div.subc.width_472.leftStyle > div:nth-child(2) > div > dl:nth-child(1) > dd > a'
        r = session.get(url)
        res =  r.html.find(selector)
        res = res[0].text
        print(f"*************** {res}")
        return res

    def reichweite(self, url):
        selector = '#c9293 > div > div > div.marginLeft_08 > div > div.leftStyle.marginTop_16.paddingBottom_16 > div.subc.width_472.leftStyle > div:nth-child(2) > div > dl:nth-child(2) > dd > a'
        r = session.get(url)
        res =  r.html.find(selector)
        res = res[0].text
        print(f"*************** {res}")
        return res

    def auf_einen_blick(self, url):
        selector = '#c9293 > div > div > div.marginLeft_08 > div > div:nth-child(3) > div.width_552.marginTop_12.marginRight_24 > div:nth-child(1) > p'
        r = session.get(url)
        res =  r.html.find(selector)
        res = res[0].text
        print(f"*************** {res}")
        return res

    def wirk_image(self,url):
        selector =  '#c9293 > div > div > div.marginLeft_08 > div > div:nth-child(5) > div.leftStyle.marginTop_12 > div:nth-child(1) > div > img'
        r = session.get(url)
        res = r.html.find(selector)[0].attrs.get('src') # get tags's attribute
        print(f"*************** {res}")
        return res


    def leistungs_image(self,url):
        selector =  '#c9293 > div > div > div.marginLeft_08 > div > div:nth-child(5) > div.leftStyle.marginTop_12 > div:nth-child(2) > div > img'
        r = session.get(url)
        #name = 'img[src]'
        res = r.html.find(selector)[0].attrs.get('src') # get tags's attribute
        print(f"*************** {res}")
        return res

    def list_all_pages(self):
        pages = []

        for i in range(0, last_page):
            url = f"https://www.phineo.org/projekte?tx_phineoprojectslite_pi1%5Bpps%5D={PROJ_PER_PAGE}&tx_phineoprojectslite_pi1%5Bpointer%5D={i}"
            pages.append(url)
        return pages

    def get_projects(self, url):
        #selector = '#searchresults > div:nth-child(2) > div.teaserImage.leftStyle.width_232 > a'
        # searchresults > div:nth-child(2) > div.teaserImage.leftStyle.width_232 > a
        # searchresults
        lst = []
        r = session.get(url)
        for i in range(1,12):
            selector = f"#searchresults > div:nth-child({i}) > div.teaserImage.leftStyle.width_232 > a"

            res = r.html.find(selector)
            if len(res) > 0:
                ## !pull element out of list and get the elements attributes...
                res = res[0].attrs.get('href')
                print(f"{res}")
                lst.append(res)
        print(f"*********************")
        return lst



    def details(self):
        count = 0
        details = []
        pages = self.list_all_pages()
        print(f"Total pages: {len(pages)}")
        for page in pages:
            print(page)

            num_projects_on_page = self.get_projects(page)
            #print(f"Number Projects on Page {len(num_projects_on_page)}")
            # for project in num_projects_on_page:
            #     selector = f"#searchresults > div:nth-child({project}) > div.teaserText.leftStyle.width_448.marginRight_24 > a"
            # searchresults > div.searchBox_01 > div.teaserText.leftStyle.width_448.marginRight_24 > a
            #     r = session.get(page)
            #     res = r.html.find(selector)
            #     ## parser all details
            #count = count + len(num_projects_on_page)

        return  count


    def website_project(self):
        selector = "#c9293 > div > div > div.marginLeft_08 > div > div.leftStyle.marginTop_16.paddingBottom_16 > div.subc.width_472.leftStyle > div.subc.clearBox.defaultBox_01.leftStyle > ul > li:nth-child(3) > a"
        pass

## teaser text
## #searchresults > div:nth-child(2) > div.teaserText.leftStyle.width_448.marginRight_24 > p



  #
  # def count_projects(self, url):
  #       lst = []
  #       #selector = "searchresults > div.searchBox_01 > div.teaserText.leftStyle.width_448.marginRight_24 > a"
  #       for i in range(2, PROJ_PER_PAGE + 1):
  #           selector = f"searchresults > div:nth-child({i}) > div.teaserText.leftStyle.width_448.marginRight_24 > a"
  #           r = session.get(url)
  #           res = r.html.find(selector)
  #           print(f"Still not working : {res}")
  #           lst.append(res)
  #       return lst