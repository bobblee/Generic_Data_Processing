# -*- coding: utf-8 -*-
import pandas as pd

json1 = [{"Name":"Person1","attributes":[{"attr_key":"role","attr_value":"husband"},{"attr_key":"build","attr_value":"cuddly"}]},
         {"attributes":[{"attr_key":"role","attr_value":"child"},{"attr_key":"build","attr_value":"itty bitty"}]},
         {"Name":"Person2","attributes":[{"attr_key":"role","attr_value":"wife"},{"attr_key":"build","attr_value":"beautiful"}]}]

# =============================================================================
# df = pd.json_normalize(json1)
# df = df.explode('attributes')
# print(df)
# 
# df['attributes']
# 
# =============================================================================
rows = []
for data in json1:
    data_row = data.get('attributes')
    Name = data.get('Name')

    for row in data_row:
        print(row)
        row['Name'] = Name
        rows.append(row)

new_df = pd.DataFrame(rows)
print(new_df)
