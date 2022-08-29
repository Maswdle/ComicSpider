# -*-coding:utf-8 -*-

"""
@ File       : hen.py
@ Time       ：2022/8/29 8:46
@ Author     ：Maswdle
@ version    ：python 3.9
@ Description：批量下载
"""

import requests, re, os, sys
from bs4 import BeautifulSoup


class Spider:
    d_lst = []
    image_lst = []
    lastname = ".jpg"
    group_pages = 0
    __r_url = ""
    information_dic_T = {
        "name": "",
        "pages": 0,
        "language": ""
    }
    #! 这个是模板
    def __init__(self, raw_url):
        self.__r_url = raw_url

    def _getpage_group(self, soup):
        tags = soup.find_all("li", class_="page-item")
        self.group_pages = len(tags) - 1
        ...

    def _get_all_d(self):
        for i in range(self.group_pages):
            url = self.__r_url + f"/{i + 1}"
            web = requests.get(url=url)
            cont = web.content
            soup = BeautifulSoup(cont, "lxml")
            tags = soup.find_all("a", class_="cover")
            self._add_d_lst(tags)
            ...

    def parse_url_group(self):
        # 一页
        web = requests.get(url=self.__r_url)
        cont = web.content
        soup = BeautifulSoup(cont, "lxml")
        self._getpage_group(soup)
        self._get_all_d()
        print(len(self.d_lst))

    def _add_d_lst(self, tags):
        for i in tags:
            self.d_lst.append(i["href"])

    def language_filter(self):
        ...

    def parse_url_d(self):
        for i in self.d_lst:
            cont = requests.get(i).content

    def download(self):
        """
        :f: 下载
        :return: None
        """
        # todo 更正循环以及及其他
        os.makedirs(f'./works/{self.information_dic["name"]}', exist_ok=True)
        os.chdir(f'{os.getcwd()}\\works\\{self.information_dic["name"]}')
        rl = len(self.image_lst)
        for i in range(rl):
            con = requests.get(i).content
            fname = f"{i}{self.lastname}"
            with open(fname, "wb") as f:
                f.write(con)
                f.close()
            print(f"{i + 1}/{rl} OK")
        print("end")


if __name__ == "__main__":
    s = Spider("https://3hentai.net/artists/yd")
    s.parse_url_group()
    print(s.group_pages)
