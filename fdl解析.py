import numpy as np
import pandas as pd

if __name__ == '__main__':
    # 读取文件
    b1 = pd.read_excel("fdl.xlsx")
    # 替换nan 为 ""
    b1 = b1.fillna("")
    # 选取机位点 标识
    b2 = b1[b1.iloc[:, 0].str.startswith("参考点处的")].index._values.tolist()[0]
    # 机位点标识下2格 为开始表
    tables = b1.iloc[b2 + 2:, :]
    # 替换表头
    new_header = tables.iloc[0]
    tables = tables[1:]
    tables.columns = new_header
    # 选取主机位点
    table_X = tables[tables.iloc[:, 0] == "X"]
    # 备选点
    table_B = tables[tables.iloc[:, 0] == "B"]

    print(tables)
