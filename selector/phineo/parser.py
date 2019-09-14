import logging
import os
import sys

from bs4 import BeautifulSoup
import requests
from requests_html import HTML
from requests_html import HTMLSession

session = HTMLSession()

#base = 'https://www.phineo.org/projekte?tx_phineoprojectslite_pi1%5Bpps%5D=25&tx_phineoprojectslite_pi1%5Bpointer%5D='
home = 'https://www.phineo.org/projekte'
class Parser:

    def __init__(self, log_level=logging.ERROR):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(log_level)
        self.handler = logging.StreamHandler(sys.stdout)
        self.logger.addHandler(self.handler)


    def pager(self):
        self.flipBoxPages(base)
        #turn page()


    def themen(self, url):
        selector = '#c9293 > div > div > div.marginLeft_08 > div > div.leftStyle.marginTop_16.paddingBottom_16 > div.subc.width_472.leftStyle > div:nth-child(1) > div > dl:nth-child(1) > dd > a'
        r = session.get(url)
        res =  r.html.find(selector)
        #res = res[0].text
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
        #name = 'img[src]'
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

    def flipBoxPages(self):
        pages = []
        selector = '#searchresults > div.columnTriple.leftStyle.width_704 > div.columnDouble.subc.rightStyle.width_480 > div > div > div > a'
        r = session.get(home)
        #name = 'a[href]'
        res = r.html.find(selector) #.attrs.get('href')  # get tags's attribute
        print(f"*************** {res}")
        for e in res:
            page = home + e.attrs.get('href')
            print(page)
            pages.append(page)
        return pages


