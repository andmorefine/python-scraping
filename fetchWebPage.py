
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
file = open('sample.csv', 'w')
writer = csv.writer(file, lineterminator='\n')

# url_link = np.array(range(1, 45))
url_link = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44']

link_page = np.array(range(2, 10))
link_page = ['', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8', 'p9']

for link in url_link:
  for page in link_page:
    # アクセスするURL
    url = "http://www.seiku.net/kotowaza/99_%s%s.html" % (link, page)

    # URLにアクセスする htmlが帰ってくる → <html><head><title>経済、株価、ビジネス、政治のニュース:日経電子版</title></head><body....

    try:
      html = ur.urlopen(url)
    except:
      print('pass')
      continue
      pass

    # htmlをBeautifulSoupで扱う
    soup = BeautifulSoup(html, "html.parser")

    # span要素全てを摘出する→全てのspan要素が配列に入ってかえされます→[<span class="m-wficon triDown"></span>, <span class="l-h...
    dl = soup.find_all("dl")

    # print時のエラーとならないように最初に宣言しておきます。
    kotowaza_all = []
    # for分で全てのspan要素の中からClass="mkc-stock_prices"となっている物を探します
    for i, tag in enumerate(dl):
      kotowaza = []
      title = []
      # classの設定がされていない要素は、tag.get("class").pop(0)を行うことのできないでエラーとなるため、tryでエラーを回避する
      dd = tag.find_all('dd')
      # print(tag.dt.text)
      title = tag.dt.text.strip().split("\n")

      kotowaza.append(i)
      kotowaza.append(title[0])
      kotowaza.append(title[1])
      kotowaza.append(dd[1].string)

      kotowaza_all.append(kotowaza)

    # writer.writerow(list)
    # 二次元配列
    writer.writerows(kotowaza_all)

# CSVファイルを閉じる
file.close()
