"""
標準ライブラリー
コレクションとコンテナについて
データ型の中でも、複数の値を束ねるための仕組みをコレクション・コンテナと呼ぶ。
Pythonにおけるコンテナは、シーケンス・セット・ディクショナリーの3型がある。
シーケンス - 順に並んだ値を扱う。中身の重複・異なる型をあつかえる。いわゆる配列
セット - 順序を持たず、値の重複ができない。数学の集合に近い
ディクショナリー - キー・値の仕組みで要素を管理する。キーは重複不可・値はOK。
"""

"""
ディクショナリーについて
dict型のデータは、一意のキーと値のペアを使って管理される。
自然言語処理を行う際や、言語を翻訳したいときに役立つ。
言語によってはディクショナリーはハッシュ・連想配列と呼ばれる。
dict型のデータ構造は、ハッシュ表という数値型のテーブルをキー・値と対応させるという
内部構造となっている。そのためdict型のデータはハッシュアブルな型を用いなければならない。
Pythonではint, str, bytes, tuple, frozenset等がハッシュアブルな型となっている。
通常、dict型のキーはintかstr型とする。

ディクショナリーの内容を参照する
"""
d1 = {"Red":"赤", "White":"白", "Yellow":"黄"}
print(d1)

#特定キーの値を参照する
print(d1["red"])

#登録されたキー全ての値を参照する
print(d1.items)

"""
ディクショナリーに新たな値・型を設定する
"""

d = {"apple":"りんご", "orange":"みかん", "melon":"メロン"}

d["apple"] = "アップル"
d["strawberry"] = "いちご"

#setdefaultメソッドはキーが存在しない場合のみ値を設定する
d.setdefault("apple","Good!!")
d.setdefault("watermelon","Good!!")

print(d)

"""
ディクショナリーから値を取得する
"""
d = {"apple":"りんご", "orange":"みかん", "melon":"メロン"}

#getは値を取得、popは値を取得して削除（取り出し）する
#popitem()は値をLIFOで取り出す（※Python3.7以降のみ）
#getする際にはKeyErrorがおこらないよう、規定値（"×"）を指定する
print(d.get("apple", "×"))
print(d.get("pear", "×"))
print(d.pop("melon", "×"))
print(d.popitem())

"""
ディクショナリーのキーを判定
"""
#特定のキーが含まれるかを判定したい時は、in演算子を使う
d = {"apple":"りんご", "orange":"みかん", "melon":"メロン"}
print("orange" in d)
print("pear" in d)

"""
ディクショナリーのキーを削除
"""
#delで特定キーの削除、clearで全てのキーの削除を行う
d = {"apple":"りんご", "orange":"みかん", "melon":"メロン"}

del d["orange"]
print(d)

d.clear()
print(d)

"""
ディクショナリーの内容を列挙する
items, keys, valuesの戻り値は列挙可能な型となっている。
"""

d = {"Apple":"リンゴ","Orange":"ミカン","Melon":"メロン"}

#項目を列挙
for item in d.items():
    print(item)
#キーと値を抽出して列挙
for key, value in d.items():
    print(key, " : ", value)

#キーを列挙
for key in d.keys():
    print(key)
#値を列挙
for value in d.values():
    print(value)

"""
ディクショナリーのキーを比較する
&, |等の演算子を使えば異なる辞書のkeys・valueの積集合・和集合を求めることができる
"""
d1 = {"Apple":"リンゴ","Orange":"ミカン","Melon":"メロン"}
d2 = {"Grape":"ブドウ","Orange":"ミカン","Pear":"なし","Apple":"リンゴ"}

print(d1.keys() & d2.keys())
print(d1.values() & d2.values())

"""
ディクショナリーの初期化判定をする
collectionsモジュール、defaultGaGaを使うことで初期値を管理する
"""
import collections

#リストに何個同じキーが含まれているかを判定し、キーと対応する値をdict型に格納する
data = ["01","02","02","03","03"]
result = collections.defaultdict(int)

for key in data:
    result[key] += 1

print(result)

"""
ディクショナリーの内包表記
リスト・セットの内包表記と同様、ディクショナリーも内包表記にすることができる
他のディクショナリー型を別のディクショナリーにコピーする、等の用途で使える
リスト型やセット型の内容をディクショナリー型にコピーする事もできる
"""

d = {"Apple":"リンゴ","Orange":"ミカン","Melon":"メロン"}
result = {value: key for key, value ind.items()}
print(result)

data = ["Apple","Pear","Olive"]
