# coding: UTF-8
import urllib.request as ur
from bs4 import BeautifulSoup

# アクセスするURL
url = "http://www.seiku.net/kotowaza/99_01.html"

# URLにアクセスする htmlが帰ってくる → <html><head><title>経済、株価、ビジネス、政治のニュース:日経電子版</title></head><body....
html = ur.urlopen(url)

# htmlをBeautifulSoupで扱う
soup = BeautifulSoup(html, "html.parser")

# # タイトル要素を取得する → <title>経済、株価、ビジネス、政治のニュース:日経電子版</title>
# title_tag = soup.title

# # 要素の文字列を取得する → 経済、株価、ビジネス、政治のニュース:日経電子版
# title = title_tag.string

# # タイトル要素を出力
# print(title_tag)

# # タイトルを文字列を出力
# print(title)

# span要素全てを摘出する→全てのspan要素が配列に入ってかえされます→[<span class="m-wficon triDown"></span>, <span class="l-h...
dl = soup.find_all("dl")

# print時のエラーとならないように最初に宣言しておきます。
# nikkei_heikin = ""
kotowaza_all = []
# for分で全てのspan要素の中からClass="mkc-stock_prices"となっている物を探します
for i, tag in enumerate(dl):
    kotowaza = []
    title = []
    # classの設定がされていない要素は、tag.get("class").pop(0)を行うことのできないでエラーとなるため、tryでエラーを回避する
    dd = tag.find_all('dd')
    # print(tag.dt.text)
    title = tag.dt.text.strip().split("\n")
    print(title[0])

    kotowaza.append(i)
    kotowaza.append(title[0])
    kotowaza.append(title[1])
    kotowaza.append(dd[1].string)

    kotowaza_all.append(kotowaza)
    # try:
        # tagの中からclass="n"のnの文字列を摘出します。複数classが設定されている場合があるので
        # get関数では配列で帰ってくる。そのため配列の関数pop(0)により、配列の一番最初を摘出する
        # <span class="hoge" class="foo">  →   ["hoge","foo"]  →   hoge
        # string_ = tag.get("class").pop(0)

        # print(tag)

        # # 摘出したclassの文字列にmkc-stock_pricesと設定されているかを調べます
        # if string_ in "news":
        #     # mkc-stock_pricesが設定されているのでtagで囲まれた文字列を.stringであぶり出します
        #     nikkei_heikin = tag.string
        #     # print(tag.string)
        #     # 摘出が完了したのでfor分を抜けます
        #     break
    # except:
    #     # パス→何も処理を行わない
    #     pass

# 摘出した日経平均株価を出力します。
# print(nikkei_heikin)

print(kotowaza_all)
