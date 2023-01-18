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
シーケンスについて
シーケンス型にはlist, tuple, range等の型がある。
シーケンス型の要素には、インデックス値を使ってアクセスすることができる。

listが扱えるのはイテラブルな型で、list(iterable)という宣言でインスタンス化することができる。
他にもリスト内包表記や、sorted(), split()といったメソッドがlistを返す。
"""
my_list = list(["x","y","z"])
my_list02 = list("abc")

print(my_list)
print(my_list_02)

#スライス構文
#list[start:end:step]
my_list03 = list("あいうえこかきくけこ")

print(my_list03[0:4])
print(my_list03[5:9])
print(my_list03[0:9:2])

#リストの要素数を取得
len(my_list03)

"""
listの要素の操作について
listのメソッドを使うことで、要素を追加・削除できる
"""
my_list_04 = list("abcdefghijklmn")
my_list_04.append("o") #末尾に追加
print(my_list_04)

my_list_04.insert(5, "*INSERTED*") #インデックスの直前に追加
print(my_list_04)

my_list_04.pop([4]) #インデックスの値を削除（値を取り出している）
print(my_list_04)

my_list_04.remove("a") #要素を削除（前から順にヒットした1つの要素のみ
print(my_list_04)

my_list_04.clear() #リストを空リストにする
print(my_list_04)


"""
listを使ってスタック(後入れ先出し式、LIFO)を実装する
"""
data =[]
data.append(10)
data.append(15)
data.append(30)

print(data)
print(data.pop())
print(data)

```python

```

"""
リスト内包表記を使って指定した全ての要素を削除する
"""
data = list(["a","b","b","a","c"])
data = [elem for elem in data if elem != "a"]

print(data)


"""
スライスを使って複数の要素を置換する
"""
data = list("あいうえお")
data[1:3] = ["1","2","3"]
print(data)

del data[1:3]
print(data)


"""
リスト内の要素を検索する
"""
data = list("いろはにほへとちりぬるを")

print(data.index("い"))
print(data.index("ち", 4))
print(data.index("ち", 4, 7))
print(data.index("ち", -4, -1))


"""
同一の要素が登場する回数をカウントする
"""
data = list("いろはにほへとちりぬるを・いろいろ")
print(data.count("い"))


"""
リストの連結
"""
data = list("いろはにほへと")
data02 = list("ちりぬるを")
print(data + data02)

data03 = list()
data03 += data
data03 += data02
print(data03)

#appendを使ってリストを連結しようとすると、リストそのものが1つの要素として扱われてしまう
data04 = data
data04.append(data02)
print(data04)


"""
リストをソートする
sortメソッドを用いる
sortは要素の型に応じて大小を判定する。数値型は値の大小で、文字型は文字の辞書順でソートされる
sortの引数にキーオプションとラムダ式を使えば、独自のルールで並べ替えることができる
"""
data_numeric = [205, 13, 78, 65]
data_string = ["banana","apple","orange","melon"]
data_lambda = ["pen","ipad","mouse","waterbottole"]
data_numeric.sort()
data_string.sort()
data_lambda = sort(key=lambda x:len(x)) #リテラルの文字数でソートする

print(data_numeric)
print(data_string)
print(data_lambda)


"""
リストをforループを使って処理
インデックス・値をforで取り出すほかにも、enumerate・zipを使うことでより複雑なリスト処理が実装できる
"""
data = ["Panda","Rabbit","Koara","Tiger"]
data02 = ["パンダ","ウサギ","コアラ","トラ"]

#インデックスと値を全て表示
for index, value in enumerate(data):
    print(index, ":",value)

#二つのリストの値を双方抽出する
for d1, d2 in zip (data, data02):
    print(d1, " Translated: ", d2)
"""
リスト内要素の真偽を判定
allで全てがTrueか、anyで1つでもTrueがあるか、not anyで全てがFalseかを判定する
要素が空か否か、条件式で条件を満たしているかも判定できる
"""
print(all([False, True, False]))
print(any([False, True, False]))
print(not any([False, True, False]))

print(any(["",""]))

data =["Rose","Cherry","Lily","Tulip"]
print(any([len(str)> 4 for str in data]))


"""
リスト内要素を加工して新しいリストをつくる
mapメソッドとlambda式を組み合わせる
"""
data = [1,3,5]
result = map(lambda v: v : v, data)
print(list(result))

data = [1,3,5]
data2 = [2,7,10]
result = map(lambda v1, v2:v1*v2,data, data2)
print(list(result))


"""
リストの要素を特定の条件で絞り込む
"""
data = ["フレンチブルドッグ","ヨークシャーテリア","コーギー"]
result = filter(lambda v:len(v) < 8,data)
print(list(result))
