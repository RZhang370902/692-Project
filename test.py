import pandas as pd
import numpy as np
file_name = "net_users_num.csv"

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
coutry_by_year_data = pd.DataFrame(body, index=body.index.rename('country'))

print(coutry_by_year_data)