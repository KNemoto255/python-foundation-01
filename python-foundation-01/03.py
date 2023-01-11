"""
演算子の使い方
Pythonでは、様々な算術演算子を使うことができる。
データの型によって、演算子の挙動は変化する
"""

print(2+3)
print(2-3)
print(5*6)
print(5**6)

print(10/7)
print(10//7)
print(10%7)

print("10" + "3")
print("Hello" + "Kira!")

print("Hello, "*3)

"""
演算子の使い方次第でタイプエラーが起きることもある。
このような場合には、型を変換してから演算する。
"""

print(15 + int("30"))
print(str(15) + "30")

"""
浮動小数点数の演算の注意点
PC内では2進数で演算が行われるため、
10 進数を表現するのに無限循環小数となってしまう場合がある。
10 進数を使った厳密な演算が行いたい場合は、decimalというライブラリーを使う。
"""
import decimal

print(0.2 * 3)
print(0.2 * 3 == 0.6)

d1 = decimal.Decimal("0.2")
d2 = decimal.Decimal("3")
d3 = decimal.Decimal("0.6")

print(d1 * d2)
print(d1 * d2 == d3)

"""
代入演算子の使い型
Pythonの代入演算子には値を代入する他、算術演算・ビット演算を兼ねた機能を提供する複合演算子もある
"""

i = 1
i += 1
print(i)

i -= 1
print(i)

i *= 25
print(i)

i /= 5
print(i)

i **= 4
print(i)

"""
Pythonにおける代入と参照渡し
Pythonにおける代入は、変数のメモリ上の場所を参照する”参照渡し”となっている。
代入を行うと、変数が異なるだけで参照先＝オブジェクトは同じという状態になる
"""

n_01 = 100
n_02 = n_01

print(n_02)
print(id(n_01))
print(id(n_02))

"""
ミュータブル型・イミュータブル型の違い
list型はミュータブルで、オブジェクトはそのままに中身を変更できる
int型はイミュータブルで、中身を変更するとそれ以前のオブジェクトとは別のオブジェクトとなる
"""

#data型の場合 - ミュータブルなので、data1・data2が同じオブジェクトを参照する
data1 = [1,2,3]
data2 = data1
data1[0] = 100
print(data1)
print(data2)

#int型の場合 - イミュータブルなので、演算子を使うとx・yは別のオブジェクトとなる
x = 2
y = x
x += 20
print(x)
print(y)

"""
アンパック代入
list型・disctionary型を分解し、個々の変数に代入することができる
この際、左辺変数と右辺（リスト）の要素数は一致していなければならない
変数を少なくしたい時、最後の変数に*をつけることで最後の変数に残りの要素をまとめて代入することができる
使い方次第で、いらない要素を切り捨てるのに使うことができ宇r

"""

data = [1,2,3,4,5]
a,b,c,d,e = data

print(a)
print(b)
print(c)
print(d)
print(e)

data = [1,2,3,4,5]
a,b,*c = data
print(a,b,c)

data = [1,2,3,4,5]
a,*b,c = data
print(a,b,c)

data = [1,2,3,4,5]
*a,b,c = data
print(a,b,c)

data = [1,2,3,4,5]
a,*_,b = data
print(a,b)


"""
比較演算子
左辺・右辺の値を比較する。結果はTrue / Falseで返される。
異なる型での比較は、多くの場合Falseとなる

浮動小数点数を比較するには、2 進数による誤差を考慮しイプシロンのような丸め単位を使うのが有効
mathライブラリーを使えば、小数点以下9桁までの精度で比較ができるisclose関数を使った比較ができる
"""

print(10 > 5)
print(10 < 5)
print(10 == 5)
print(10 != 5)
print("\n")

print([1,2] is [1,3])
print([1,2] is not [1,3])
print(3 in [1,3])
print(3 not in [1,3])
print("\n")

print(1 == "1")
print(False == None)
print("\n")

import math
epsilon = 0.000001

x = 0.2 * 3
y = 0.6

print(abs(x-y) < epsilon)
print(math.isclose(0.2*3, 0.6))

#rel_tolで大数との割合で比較する相対誤差、abs_tolで定数を使った絶対誤差を比較できる
print(math.isclose(0.1, 0.1001, rel_tol=0.0001))
print(math.isclose(0.1, 0.1001, rel_tol=0.001))


"""
同一性と同値性の比較
is と == とでは比較する内容が異なる。
isは参照値が同じオブジェクトかを、==はオブジェクトが同じ値かを比較する
型がNoneかを判定するには、==ではなくisをつかう。Noneか否かの判定は、フェイルセーフを設けるのに役立つ
"""

data1 = [1,2,3]
data2 = [1,2,3]

print(data1 == data2)
print(data1 is data2)


"""
論理演算子
条件式の真偽を結合してその結果を返す。結果はTrue / Falseで返される。
論理積、論理和、排他的論理和、否定の4式ですべての演算のパターンを表せる
"""

bool1 = True
bool2 = False

print(boo1 and bool2)
print(boo1 or bool2)
print(boo1 ^ bool2)
print(not boo1)





