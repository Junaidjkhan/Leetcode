import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    Customers = customers.merge(orders, how='left', left_on='id', right_on='customerId')

    mask = Customers[Customers['customerId'].isna()]

    return pd.DataFrame(mask['name']).rename(columns = {'name':'Customers'})
