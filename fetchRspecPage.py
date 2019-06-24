# -*- coding: utf-8 -*-

import json
import csv
from pprint import pprint

# 連番や等差数列を生成する関数
import numpy as np
# coding: UTF-8
import urllib.request as ur
import urllib.parse
from bs4 import BeautifulSoup

headers = { 'Content-Type': 'application/json', }

# csv 開く
file = open('rspec_file.csv', 'w')
writer = csv.writer(file, lineterminator='\n')

url_link = ['AllFiles', 'Controllers', 'Models', 'Mailers', 'Helpers', 'Jobs', 'Libraries', 'Ungrouped']
# url_link = ['AllFiles']

url = "http://samurai.page.gitlab.usaqh.com/living-related/#_AllFiles"
# htmlをBeautifulSoupで扱う
html = ur.urlopen(url)
soup = BeautifulSoup(html, "html.parser")

for link in url_link:

  covered_percent = '0%'
  covered_percent = soup.find(id=f'{link}').find(class_="covered_percent").find("span").text
  covered = covered_percent.replace('%', '')

  # 表示する数値
  print(covered)

  cover_array = []
  # cover_array.append(link)
  cover_array.append(covered)
  # print(cover_array)

  writer.writerow(cover_array)

# CSVファイルを閉じる
file.close()
