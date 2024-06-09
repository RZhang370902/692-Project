import pandas as pd
import numpy as np

def process_data (file_name, type):
    stage1 = pd.read_csv(file_name, index_col=[0], header=[0])
    stage2 = pd.DataFrame(stage1.stack())
    #print(stage2.columns.values[0])
    stage3 = stage2.rename(columns={stage2.columns.values[0]:type})
    stage4 = pd.DataFrame(stage3, index=stage3.index.set_names(['country', 'year']))
    stage5 = stage4[type].replace({"k":"*1e3", "M":"*1e6", "B":"*1e9"}, regex=True).map(pd.eval).astype(int)
    stage6 = pd.DataFrame(stage5)
    return stage6

a = process_data("net_users_num.csv", "network")
print(a)

b = process_data("coal_consumption_total.csv", "coal")
#print(b)


c = process_data("coal_consumption_total.csv", "coal2")


test = pd.merge(a, b, left_index=True, right_on=['country', 'year'])
print(test)

test2 = pd.merge(test, c, left_index=True, right_on=['country', 'year'])
print(test2)


w = pd.DataFrame(test2['coal'])
print(w)

print(np.sum(w, axis=0))

