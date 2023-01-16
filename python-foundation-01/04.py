"""
制御構文に関する章
条件分岐について

if-else文を使えば、与えられた条件を使って実行するべき処理を変えられる。
if-elif文の場合、複数の条件に合致しても実行されるのは最初に合致した命令だけである。
"""

cond = True
if cond:
    print("Condition is TRUE.")
else:
    print("Condition is FALSE.")

i = 100
if i > 50:
    print("変数 > 50")
elif i > 30:
    print("変数 > 30")
else:
    print("変数 < 30")


"""
==演算子を使った多岐分岐となる場合は、dictionaryを活用すると効率がいい
"""

rank = "B"

msg = {
    "A":"良いですね",
    "B":"まあまあ",
    "C":"ダメ！"
}

if rank in msg:
    print(msg[rank])
else:
    print("???")

"""
繰り返し処理について

while文を使えば、条件が真の間だけ処理を繰り返す
繰り返し処理を行う場合は、無限ループが発生しないような条件式とする
for文を使えば、in演算子をつかってリストの中の要素分だけ処理を行うことができる
"""

i = 1

while i <6:
    print(i, "番のループを表示")
    i += 1

data = ["札幌","東京","大阪"]
for value in data:
    print(value)

data = "for文を使って文字列を処理"
for value in data:
    print(value)

for in range(1,6):
    print(i, "番目のループ")

for in range(0,10,2):
    print(i, "rangeの使い方、その1")

for in range(5,0,-1):
    print(i, "rangeの使い方、その2")

print(list(range(0,7,2)))


"""
繰り返し処理について

while文を使えば、条件が真の間だけ処理を繰り返す
繰り返し処理を行う場合は、無限ループが発生しないような条件式とする
for文を使えば、in演算子をつかってリストの中の要素分だけ処理を行うことができる


#dataの値を2倍にした数のリストを作成する
data = [15,43,7,59,98]
data2 = [i * 2 for i in data]
print(data2)

#内包表記の処理は、for文をつかって記述もできる
data3 = [15,43,7,59,98]
data4 = []
for i in data3:
    data4.append(i*2)
print(data4)

#リスト内包表記では、if節を利用することでリストの内容を絞り込むことができる
data = [15,43,7,59,98]
data2 = sum[i for i in data if i < 50]
print(data2)


"""
ループの制御

break, continue,tryの使い方
breakを使うとfor文ループを終了させる。主に条件分岐と組み合わせて使用する。
continueを使うと、その時のループ処理だけをスキップする。条件分岐と組み合わせて使用する。
コンパイルエラーが起きた際の例外処理を実装するには、try-except-finally構文を使う
else文を使えば、break・continueを使わなくても処理を記述できる
"""

sum = 0
for i in range(1,101):
    sum += i
    if sum > 1000:
        break
print("合計が1000を超える時の値→", sum)

sum = 0
for i in range(1,101):
    if i % 2 != 0:
        continue
    sum += i
print("1 - 100までの奇数の合計は、", sum, "です")

data = ["桜","梅","桔梗"]
for name in data:
    if name == "x":
        break
    else:
        print("ループ終了")

while True:
    try:
        num = input("数字を入力")
        print(float(num))
    except ValueError:
        print("入力値が数値ではありません")
    else:
        break
