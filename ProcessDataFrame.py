import pandas as pd
import numpy as np

'''
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
print(a.loc['Serbia'])
'''
def process_csv_file (file_name, data_name):
    fresh_data = pd.read_csv(file_name, index_col=[0], header=None)
    
    vertical_integer_col_name = fresh_data.iloc[0,1:].apply(int)
    horizontal_integer_col_name = np.reshape(vertical_integer_col_name,(1,vertical_integer_col_name.size))
    
    fresh_data_body = pd.DataFrame(fresh_data.iloc[1:,1:])
   
    stack_integer_col_and_data_body = np.vstack((horizontal_integer_col_name, fresh_data_body))

    headerless_country_by_year_data = pd.DataFrame(stack_integer_col_and_data_body, index=fresh_data.index)

    #grab row 0 as header
    new_header = headerless_country_by_year_data.iloc[0] #grab the first row for the header
    body = headerless_country_by_year_data[1:] #take the data less the header row
    body.columns = new_header.rename('year') #set the header row as the df header
    country_by_year_data = pd.DataFrame(body, index=body.index.rename('country'))


    country_year_data = pd.DataFrame(country_by_year_data.stack())
    stage1 = country_year_data.rename(columns={country_year_data.columns.values[0]:data_name})
    stage2 = pd.DataFrame(stage1, index=stage1.index.set_names(['country', 'year']))


    stage3 = stage2[data_name].replace({"k":"*1e3", "M":"*1e6", "B":"*1e9"}, regex=True).map(pd.eval).astype(int)
    stage4 = pd.DataFrame(stage3)
    stage5 = stage4.reset_index()
    return stage4


a = process_csv_file("net_users_num.csv", "internet")

print(a)

b = process_csv_file("coal_consumption_total.csv", "coal")

c = pd.merge(a, b, left_index=True, right_on=['country', 'year'])

print(c)

c = c.reset_index()
print(c)

#a = a.reset_index()
print(c[(c['year'] > 2010) & (c['country'] == 'UAE')])

