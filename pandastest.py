import numpy as np
import pandas as pd

s = pd.Series([1, 2, 3, 4, 5, 15, 12412, np.nan])
print(s)

dates = pd.date_range("20200522", periods=6)
print(dates)

df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=['a', 'b', 'c', 'd'])

print(df)
