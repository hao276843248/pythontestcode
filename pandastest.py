import numpy as np
import pandas as pd

s = pd.Series([1, 2, 3, 4, 5, 15, 12412, np.nan])
print(s)

dates = pd.date_range("20200522", periods=6)
print(dates)

df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=['a', 'b', 'c', 'd'])

print(df)
df1 = pd.DataFrame(np.arange(12).reshape(4, 3))
print(df1)
df2 = pd.DataFrame({"A": 1,
                    "B": "123",
                    "c": 123123,
                    "D": np.array([3] * 4),
                    "F": pd.Categorical(["1", 2, 3, 4])})
print(df2)
print(df2.dtypes)
print(df2.columns)
print(df2.values)
print(df2["F"].dtypes)
print(df2["F"].index)
# 统计信息
print(df2.describe())
#          A         c    D
# count  4.0       4.0  4.0
# mean   1.0  123123.0  3.0
# std    0.0       0.0  0.0
# min    1.0  123123.0  3.0
# 25%    1.0  123123.0  3.0
# 50%    1.0  123123.0  3.0
# 75%    1.0  123123.0  3.0
# max    1.0  123123.0  3.0
# 颠倒
print(df2.T)
print(df)
df = df.sort_index(axis=1)
print(df)
print("*" * 10)
# select by
# loc中【行：【】，列：【】】
print(df.loc["2020-05-22"])
# a    0.006229
# b    0.218419
# c   -1.126906
# d    0.440700
# Name: 2020-05-22 00:00:00, dtype: float64
print("*" * 10)
print(df.loc[:, ["a", "c"]])
print("*" * 10)
print(df.iloc[3:5, :])
print("*" * 10)
print(df.iloc[[0, 2], 1:3])
print("*" * 10)
# ix 启用 df.ix
print(df)
print("*" * 10)
print(df.iloc[1])
print("*" * 10)
print(df.iloc[1:2].T)
print("*" * 10)
print(df[(df["a"] > 0.2) & (df.iloc[1] > 0.2)])
print("*" * 10)
print(df[(df["a"] > 0.2) & (df.iloc[1:2].T.iloc[0] > 0.2)])
df.drop()
print(df.iloc[1:2].T.iloc[0])
df.drop()
# aa = pd.DataFrame({"asdf": 123})
# print(aa)
# pands timestamp 转 字符串
# df .strftime("%Y-%m-%d %H:%M:%S")
# df[['年月日时分秒']].apply(lambda x: x.strftime("%Y-%m-%d %H:%M:%S"))
# df['年月日时分秒'] = [x.strftime('%Y-%m-%d') for x in df['年月日']]
