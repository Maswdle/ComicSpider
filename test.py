# -*-coding:utf-8 -*-

"""
@ File       : test.py
@ Time       ：2022/9/1 9:26
@ Author     ：Maswdle
@ version    ：python 3.9
@ Description：
"""
import os

path = 'C:\\Users\\wondr\\PycharmProjects\\ComicSpider\\works\\(C100) [OrangeMaru (YD)] OrangeMaru vol.12 (THE iDOLM@STER: Shiny Colors) [Chinese] [無邪気漢化組] - 3Hentai'
print(path)
path = path.replace(":","")
os.makedirs(path, exist_ok=True)
os.chdir(path)
