# -*-coding:utf-8 -*-

"""
@ File       : hen.py
@ Time       ：2022/8/29 8:46
@ Author     ：Maswdle
@ version    ：python 3.9
@ Description：
"""

import requests, re, os, sys
from bs4 import BeautifulSoup


class Spider:
    d_lst = []
    image_lst = []
    lastname = ".jpg"
    information_dic = {
        "name": "",
        "pages": 0,
        "language": ""
    }

    def __init__(self, raw_url):
        self.__r_url = raw_url

    def parse_url_group(self):
        cont = requests.get(url=self.__r_url).content
        soup = BeautifulSoup(cont, "lxml")
        tags = soup.find_all("a", class_="cover")
        for i in tags:
            self.d_lst.append(i["href"])
        print(self.d_lst)

    def select(self):
        ...

    def parse_url_d(self):
        for i in self.d_lst:
            cont = requests.get(i).content

    def download(self):
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
