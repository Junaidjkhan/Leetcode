import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    
    df = sales_person.merge(orders, how = 'left', left_on = 'sales_id', right_on = 'sales_id')

    df1 = df.merge(company, how = 'left', left_on = 'com_id', right_on = 'com_id')

    red = df1[df1['name_y'] == 'RED'][['name_x']]

    non_red = sales_person[['name']].merge(red, how = 'outer', left_on = 'name', right_on = 'name_x', indicator = True)

    return non_red[non_red['_merge'] == 'left_only'][['name']]
