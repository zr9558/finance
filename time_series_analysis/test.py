import numpy as np
import pandas as pd
import tushare as ts

# df = ts.get_tick_data('000581',date='2018-01-09')
df = ts.get_realtime_quotes('000581')
print(df)

df = ts.get_hist_data('000581')

df.plot()

print(np.array(10))
