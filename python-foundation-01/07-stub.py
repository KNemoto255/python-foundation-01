"""
正規表現、ファイルの操作
正規表現について -文字列の中から、パターンに合うものを検索する
（電話番号・郵便番号）
compileで正規表現を定義、searchで正規表現にマッチした文字列の抽出を行う
"""
import re

msg ="電話番号は、080-111-9999です。"
ptn = re.compile(r"(\d{2,4})-(\d{2,4})-(\d{4})")

#文字列を検索して表示

if result := ptn.search(msg):
    print(result.group(0))
    print(result.group(1))
    print(result.group(2))
    print(result.group(3))
else:
    print("Search did't found the result.")

"""
findallを使って、正規表現にマッチした全ての文字列の抽出を行う
"""
msg ="電話番号は、080-111-9999です。携帯は、334-114-1415です。"
ptn = re.compile(r"(\d{2,4})-(\d{2,4})-(\d{4})")

#引っかかった文字列を全て抽出
results = ptn.findall(msg)
for results in results:
    print(result)

"""
ファイル操作
テキストファイルを保存する等、アプリやソフトウェアのログ・セーブデータを残したい場合はfileクラスを利用する
ファイルを開く・読み書きする・閉じる
ファイルオブジェクトはcloseされるか、コードが終了すると破棄される
"""
import datetime

#第二引数 - rで読み込み、wで書き込み、aで追記（末尾にデータを追記していく）
file = open("log.txt", "a", encoding = "UTF-8")

#ファイルに書き込むデータ型は、文字列にする
file.write(f"{datetime.datetime.now'()}\n")
file.close()
print("現在時刻をファイルに保存")


"""
ファイル操作をする際は、with構文を使ってフェイルセーフする。
with構文を使えば、ファイル操作の途中でエラーが発生しても確実にファイルを閉じることができる
ファイルに不明な形式の文字列が含まれている場合は、errors属性で例外処理を指定できる
errors="replace"は不明な形式の文字を?に変換する
"""
with open("log.txt", "w", encoding = "UTF-8", errors="replace") as file:
    file.write(f"{datetime.datetime.now'()}\n")
