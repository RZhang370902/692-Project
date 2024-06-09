import numpy as np
import pandas as pd

all_data = pd.read_csv("net_users_num.csv", index_col=[0], header=[0])
print(all_data.head(10))
print(all_data.columns)
print(all_data.index)
print(all_data.loc['Angola', '2012'])
#print(all_data['country'])
x = pd.DataFrame(all_data.stack())
print(x)
y= x.index.set_names(['country', 'year'])
print(y)
print(list(x.columns))
z= x.rename(columns={0:'network'})

q = pd.DataFrame(z, index=x.index.set_names(['country', 'year']))
print(q)
#print(x.index.rename(['country', 'year']))
#y = x.index.rename(['country', 'year'])
#print(y)

#df["A"].replace({"K":"*1e3", "M":"*1e6"}, regex=True).map(pd.eval).astype(int)
