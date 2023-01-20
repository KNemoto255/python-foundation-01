"""
datetimeの使い方
"""
import datetime
today =datetime.date(2020,11,10)
print(today.year)

current = datetime.date.today()
print(current)


"""
文字列の操作・変換
"""
#len() - 文字列の長さを取得
#unicodedataのモジュールを使うことで、日本語などのマルチバイト文字をどうカウントするかを指定できる
import unicodedata

title="Python Project"
print(len(title))

title_jp= "Pythonプロジェクト"
count = 0

for ch in data:
    if unicodedata.east_asian_width(ch) in "FWA":
        count += 2
    else:
        count += 1

print(count)

"""
部分文字列の取得
list型や文字列から部分を取り出すには、インデックス/スライス構文を利用する
"""

title = "あいうえお、かきくけこ"

print(title[2])
print(title[2:5])

print(title[-10:])
print(title[::-1])


"""
文字列を区切り文字で分割
split、rsplitメソッドを使う。splitは前方から、rsplitは後方から分割する
指定がない場合は、空白文字で分割してlist型に格納する
"""

msg1 = "Cat Dog Racoon"
msg2 = "Cherry\Peach\Apple"

msg_spt1 = msg1.split()
msg_spt2 = msg2.split("\")

print(msg_spt1)
print(msg_spt2)


"""
文字列を改行文字で分割
splitlinesメソッドで改行ごとに分割ができる。自然言語処理などでよく用いられる
"""
msg = '''\
こんにちは、
こんばんは、
さようなら
'''

print(msg.splitlines())
print(msg.splitlines(True))

"""
リストを結合する。リスト以外にも文字列型などのイテラブル型を結合できる。
joinメソッドを使って指定の区切り文字で連結する
"""

data1 = ["Cat","Dog","Racoon"]
data1_joined = ","join(data1)

print(data1_joined)


"""
文字列を置き換える。文字列に含まれている特定の文字列の置き換えには、replaceメソッドを使う。
第三引数に置き換える文字の数を指定することができる。
"""

msg = "にわにはには、にわとりがいる"
print(msg.replace("にわ","ニワ"))
print(msg.replace("にわ","ニワ",2))

"""
文字列を置き換える際、translateメソッドを使うと辞書型をつかってまとめて変換ができる。
不要な記号を省いたり、語尾を全て丁寧語に直したい場合に便利。
"""

msg = "今日の、あなたの運勢は、★良い感じ★ です。"
dictionary = str.maketrans({",":" ",".":" ","★":" "})
msg_trans = msg.translate(dictionary)

print(msg_trans)


"""
文字列を整形する
formatメソッドを使うことで、指定した書式の文字を挿入することができる。
入力された文字を次の出力に反映したいときに有効。
"""
pt_strings = "{}は{}歳です。".format("キャットちゃん",2)
