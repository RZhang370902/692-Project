import numpy as np
import pandas as pd

all_data = pd.read_csv("net_users_num.csv", index_col=[0], header=None)
print(all_data)

#df.iloc[1].apply(int)
print(all_data.iloc[0,1:])
a = all_data.iloc[0,1:].apply(int)
a = np.reshape(a,(1,29))
print(a)
b = pd.DataFrame(all_data.iloc[1:,1:])
print(b)
print(a.shape)
print(b.shape)
c = np.vstack((a,b))
print(c)

d = pd.DataFrame(c, index=all_data.index)
print(d)

new_header = d.iloc[0] #grab the first row for the header
df = d[1:] #take the data less the header row
df.columns = new_header.rename('year') #set the header row as the df header
print(df)
print(df.loc['Angola'])
print(df.columns.map(type))
print(df.index)
print(new_header.rename('year'))
df = pd.DataFrame(df, index=df.index.rename('country'))
print(df)
stage2 = pd.DataFrame(df.stack())
stage3 = stage2.rename(columns={stage2.columns.values[0]:"demo"})
stage4 = pd.DataFrame(stage3, index=stage3.index.set_names(['country', 'year']))
print(stage4)
print(stage4.loc[('Angola', 1991)])
print(stage4.index)
print(stage4.loc['Angola', 1991])
print(stage4.loc[stage4.index])

stage5 = stage4["demo"].replace({"k":"*1e3", "M":"*1e6", "B":"*1e9"}, regex=True).map(pd.eval).astype(int)
stage6 = pd.DataFrame(stage5)

print(stage6)
hhh = stage6.reset_index()
print(hhh)

print(hhh[(hhh['year'] > 2010) & (hhh['country'] == 'Zimbabwe')])


