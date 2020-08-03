import numpy as np
import pandas as pd

if __name__ == '__main__':
    b1 = pd.read_excel("b1.xls")
    print(b1)
    b2s = pd.read_excel("b2.xls", 1).loc[5:]
    for i in range(2, 8):
        b2 = pd.read_excel("b2.xls", i).loc[5:]
        b2s = b2s.append(b2, ignore_index=True)
    # Index(['宽城满族自治县', 'Unnamed: 1', 'Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4'], dtype='object')
    b2s = b2s.rename(columns={str("宽城满族自治县"): "户主姓名"})
    b2s = b2s.rename(columns={str("Unnamed: 1"): "退耕还林补贴"})
    b2s = b2s[["户主姓名", "退耕还林补贴"]]
    b2s["退耕还林补贴"] = np.ceil(b2s["退耕还林补贴"] * 90)
    b1["退耕还林补贴"] = np.ceil(b1["退耕还林补贴"])
    b2s["户主姓名"] = b2s["户主姓名"].str.replace("\u3000", "")
    b1["户主姓名"] = b1["户主姓名"].str.replace("\u3000", "")
    print(b2s)
    df_inner = pd.merge(b1, b2s, indicator=True, how='outer', on=['户主姓名', "退耕还林补贴"]) \
        .query('_merge=="left_only"').drop('_merge', axis=1)
    print(df_inner)
    df_inner.to_excel("a.xls")