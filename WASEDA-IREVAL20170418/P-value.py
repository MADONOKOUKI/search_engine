# 参考URL
# csv関係
# http://qiita.com/okadate/items/c36f4eb9506b358fb608
# F検定
# http://kusuri-jouhou.com/statistics/fkentei.html
# T検定
# https://openbook4.me/projects/183/sections/1367
# http://stat.biopapyrus.net/statistic/t-test.html

import csv
import numpy as np
import scipy as sp
from scipy import stats

# 各配列の宣言
BASELINE_D_J_1 =[]
MSINT_D_J_4_B = []  
MSINT_D_J_5_B = [] 
MSINT_D_J_R_2 = []

#配列代入作業
with open('exp1.csv', 'r') as f:
    reader = csv.reader(f)
    header = next(reader)  # ヘッダーを読み飛ばしたい時
    for row in reader:
      row = row[0].split()
      BASELINE_D_J_1.append(float(row[0]))
      MSINT_D_J_4_B.append(float(row[1]))
      MSINT_D_J_5_B.append(float(row[2]))
      MSINT_D_J_R_2.append(float(row[3]))
BASELINE_D_J_1 = np.array(BASELINE_D_J_1)
MSINT_D_J_4_B = np.array(MSINT_D_J_4_B) 
MSINT_D_J_5_B = np.array(MSINT_D_J_5_B)
MSINT_D_J_R_2 = np.array(MSINT_D_J_R_2)

#等分散かどうか念のためにF検定を行う
#帰無仮説(h0)→「2群間の分散に差がない（等分散である）」
#対立仮説(h0)→「2群間の分散に差がある（等分散でない）」
print(stats.f.cdf(np.var(BASELINE_D_J_1) / np.var(MSINT_D_J_4_B),len(BASELINE_D_J_1) - 1,len(MSINT_D_J_4_B) - 1))
print(stats.f.cdf(np.var(BASELINE_D_J_1) / np.var(MSINT_D_J_5_B),len(BASELINE_D_J_1) - 1,len(MSINT_D_J_5_B) - 1))
print(stats.f.cdf(np.var(BASELINE_D_J_1) / np.var(MSINT_D_J_R_2),len(BASELINE_D_J_1) - 1,len(MSINT_D_J_R_2) - 1))
print(stats.f.cdf(np.var(MSINT_D_J_4_B) / np.var(MSINT_D_J_5_B),len(MSINT_D_J_4_B) - 1,len(MSINT_D_J_5_B) - 1))
print(stats.f.cdf(np.var(MSINT_D_J_4_B) / np.var(MSINT_D_J_R_2),len(MSINT_D_J_4_B) - 1,len(MSINT_D_J_R_2) - 1))
print(stats.f.cdf(np.var(MSINT_D_J_5_B) / np.var(MSINT_D_J_R_2),len(MSINT_D_J_5_B) - 1,len(MSINT_D_J_R_2) - 1))
#→　p値が0.05をすべて超えているので、H0の元で起こり得ることだとわかり、等分散だとわかる
#p値が0.05以下であった場合は有意水準において統計的に優位であるとわかる

# t検定は,正規分布に従う2つの実験群の平均値を比較し、
# 両者に有意差が存在するかどうかを検定する方法。
# t検定は,2つの実験群の分散が等しいかどうかによって,計算が異なる。

#①分散が同じ　→　stats.ttest_ind(list,list)
#②分散が違う　→　stats.ttest_ind(list,list,equal_var = False)
#③従属なデータの場合　→ stats.ttest_rel(list,list)　。(Ex)　薬投薬前・薬投薬後など、従属関係が見えるデータの例。
#　分散が同じケースと同じ結果を出力する
t = stats.ttest_ind(BASELINE_D_J_1,MSINT_D_J_4_B)
print("①BASELINE_D_J_1とMSINT_D_J_4_Bの結果")
print(t)
t = stats.ttest_ind(BASELINE_D_J_1,MSINT_D_J_5_B)
print("②BASELINE_D_J_1とMSINT_D_J_5_Bの結果")
print(t)
t = stats.ttest_ind(BASELINE_D_J_1,MSINT_D_J_R_2)
print("③BASELINE_D_J_1とMSINT_D_J_R_2の結果")
print(t)
t = stats.ttest_ind(MSINT_D_J_4_B,MSINT_D_J_5_B)
print("④MSINT_D_J_4_BとMSINT_D_J_5_Bの結果")
print(t)
t = stats.ttest_ind(MSINT_D_J_4_B,MSINT_D_J_R_2)
print("⑤MSINT_D_J_4_BとMSINT_D_J_R_2の結果")
print(t)
t = stats.ttest_ind(MSINT_D_J_5_B,MSINT_D_J_R_2)
print("⑥MSINT_D_J_5_BとMSINT_D_J_R_2の結果")
print(t)

# if p < 0.05:
#     print("有意な差があります")
# else:
#     print("有意な差がありません")