"""
正規表現、ファイルの操作、HTTP通信、数学演算
正規表現について -文字列の中から、パターンに合うものを検索する
（電話番号・郵便番号）

"""
import re

msg ="電話番号は、080-111-9999"です。
ptn = re.compile(r"(\d{2,4})-(\d{2,4})-(\d{4})")

#文字列を検索して表示

if result := ptn.search(msg):
    print(result.group(0))
    print(result.group(1))
    print(result.group(2))
    print(result.group(3))
else:
    print("Search did't found the result.")
