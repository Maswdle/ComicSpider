# -*-coding:utf-8 -*-

"""
@ File       : main.py
@ Time       ：2022/8/29 8:33
@ Author     ：Maswdle
@ version    ：python 3.9
@ Description：
"""

import requests, re, os, sys
from bs4 import BeautifulSoup


class Spider:
    image_lst = []
    lastname = ".jpg"
    information_dic = {}
    def __init__(self, raw_url):
        self.__r_url = raw_url

    def parse_url(self):
        cont = requests.get(url=self.__r_url).content
        soup = BeautifulSoup(cont, "lxml")

    def select(self,your_args):
        ...

    def download(self):
        os.makedirs("./works", exist_ok=True)
        os.chdir(f"{os.getcwd()}\\works")
        rl = len(self.image_lst)
        for i in range(rl):
            con = requests.get(i).content
            fname = f"{i}{self.lastname}"
            with open(fname, "wb") as f:
                f.write(con)
                f.close()
            print(f"{i + 1}/{rl} OK")
        print("end")
