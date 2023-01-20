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
セットについて
setは複数の値を扱うことができるが、順序を持たず値が重複できない。そのため、インデックス使った抽出などは出来ない。
重複を許さないケースで、かつ他の集合と内包関係にあるか等を検証したい場合に用いられる。
setはミュータブル、frozensetはイミュータブルな集合をとりあつかいたい場合に用いる
"""

my_set = {"Elen","Mikasa","Armin"}
print(my_set)
my_frozenset = frozenset({'value1', 'value2', 'value3', 'value4'})
print(my_frozenset)

my_sets.add("Jean")
my_sets.remove("Elen")

for item in my_set:
    print(item)

#set型には順序がないので、popすると毎回結果が異なる
print(my_set.pop())
print(my_set)

my_set.clear()
print(my_set)

"""
セットの比較と判定
要素が含まれているか、部分集合になっているかを判定する
"""

sets1 = {15,25,37,20}
sets2 = {10,13,32}
sets3 = {25,37}

print(10 in sets1)
print(10 not in sets1)

print(sets3.issubset(sets1))
print(sets3.issuperset(sets1))
