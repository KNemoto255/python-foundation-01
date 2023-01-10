"""
JupyterNotebookの使い方 - マークダウン方式
セル上部のCodeをMarkDownに変更すると、コードの代わりにマークダウン形式のテキストを記載できる

# 見出し1
## 見出し2
### 見出し3
#### 見出し4
##### 見出し5
###### 見出し6

"""

"""

Pythonはプログラミング言語であり、特に人間に読みa書きできる高水準言語である
Pythonはソースコードを逐次翻訳しながら実行する、インタープリター言語である
Pythonの良点 - 文法が簡単、予約語が少ない(スクリプト言語）、オブジェクト指向プログラミングができる
ラムダ式・ジェネレーターといった関数型プログラミングもできる。
また処理の流れを順に記述する、手続き型言語の側面もある。
Pythonは様々なプログラミング思想を取り入れた、マルチパラダイムな言語である。

"""

"""
Printの使い方

インデントについて
Pythonにおいてはインデント(字下げ)が文法上の意味を持つので、無条件 のインデントは認められていない
行継続中に限ってインデントも自由 

"""
print("Hello",
      "world")


#printを文字区切りで出力したい場合は、こう記述する

name = "KNemoto"
print("Hello", name, "さん！", sep =" + ")

"""
Printによる出力の末尾には、デフォルトで改行コードが付与される
改行コードを別の物に変えるには、end = "" という引数を追加する
"""
print("Hello", end = "★ ")
print("Welcome", end = "★ ")


# ## 関数の定義

def hello():
    print("こんにちは")
hello()

"""
Anacondaに標準搭載されているライブラリ(NumPy, matplotlib)を使えば、
JupyterNotebook内でグラフを作成できる。

matplot公式サイトのサンプルコード - https://matplotlib.org/stable/gallery/lines_bars_and_markers/barh.html

% matplotlib inline
"""

import matplotlib.pyplot as plt
import numpy as np

# Fixing random state for reproducibility
np.random.seed(19680801)


plt.rcdefaults()
fig, ax = plt.subplots()

# Example data
people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
y_pos = np.arange(len(people))
performance = 3 + 10 * np.random.rand(len(people))
error = np.random.rand(len(people))

ax.barh(y_pos, performance, xerr=error, align='center')
ax.set_yticks(y_pos, labels=people)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('Performance')
ax.set_title('How fast do you want to go today?')

plt.show()

