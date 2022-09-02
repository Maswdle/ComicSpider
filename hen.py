# -*-coding:utf-8 -*-

"""
@ File       : hen.py
@ Time       ：2022/8/29 8:46
@ Author     ：Maswdle
@ version    ：python 3.9
@ Description：批量下载
"""

import os
import re
import requests
from bs4 import BeautifulSoup


class Spider:
    d_lst = []
    image_lst = []
    lastname = ".jpg"
    group_pages = 0
    __r_url = ""
    information_dic = {
        "title": "",
        "pages": 0,
        "language": "",
        "s": 0,
        "number": 0
    }

    def __init__(self, raw_url):
        self.__r_url = raw_url
        self.__path = os.path.abspath(".")

    def _getpage_group(self, soup):
        tags = soup.find_all("li", class_="page-item")
        self.group_pages = len(tags) - 1
        if self.group_pages == -1:
            self.group_pages = 1
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
        print(f'total : {len(self.d_lst)}\n')

    def _add_d_lst(self, tags):
        for i in tags:
            self.d_lst.append(i["href"])

    def filter_and_download(self, language, length = -1):
        # * 即语言和标题的获取，
        c = 0
        for i in self.d_lst:
            web = requests.get(url=i)
            cont = web.content
            soup = BeautifulSoup(cont, "lxml")
            # * 语言和标题
            title = soup.find("title").string
            lang = soup.find_all(
                "a", class_="name", href=f"https://3hentai.net/language/{language}")
            if len(lang) == 0:  # 筛选语言
                continue
            else:
                if c == length:
                    return
                c += 1
            # 其他
            tag = soup.find("a", class_="name", rel="nofollow")
            s_tags = soup.find_all("img", class_="lazy small-bg-load")
            s_url = s_tags[0].attrs["data-src"]
            s_number = int(re.search(r'/(.+).3', str(s_url)).group()[3])
            a = str(tag.contents)
            result = re.search(r'\d+', a)
            ur: str = i
            d_num = int(ur.split("/")[-1])
            # * dic
            self.information_dic["pages"] = int(result.group())
            self.information_dic["s"] = s_number
            self.information_dic["title"] = title
            self.information_dic["number"] = d_num
            self._download()

    def parse_url_d(self):
        ...

    def _download(self):
        """
        :f: 下载
        :return: None
        s_number
        """
        os.chdir(self.__path)
        os.makedirs("works", exist_ok=True)
        os.chdir(f"{self.__path}\\works")
        path: str = self.information_dic["title"]
        path = path.replace("/", "-")  # 避免多层目录
        path = path.replace(":", "-")
        os.makedirs(path, exist_ok=True)  # todo 修改这一句
        os.chdir(f"{self.__path}\\works\\{path}")
        rl = self.information_dic["pages"]
        self._out()
        for i in range(1, rl + 1):
            url = f'https://s{self.information_dic["s"]}.3hentai.net/d{self.information_dic["number"]}/{i}.jpg'
            con = requests.get(url=url).content
            fname = f"{i}{self.lastname}"
            with open(fname, "wb") as f:
                f.write(con)
                f.close()
            print(f"{i}/{rl} OK")
        print("end")
        os.chdir(f"{self.__path}\\works")

    def _out(self):
        print(f'title: {self.information_dic["title"]}')
        print(f'pages: {self.information_dic["pages"]}')
        print(f'number: {self.information_dic["number"]}')


if __name__ == "__main__":
    name = input("artist>>>")
    times = int(input("times>>>"))
    lang = input("language>>>")
    s = Spider(f"https://3hentai.net/artists/{name}")
    s.parse_url_group()
    s.filter_and_download(lang, length=times)
    print(s.group_pages)
    input("")
