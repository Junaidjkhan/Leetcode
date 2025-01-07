import pandas as pd

def sales_analysis(product: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    
    sales['sale_date'] = pd.to_datetime(sales['sale_date'])

    sales = sales.groupby('product_id')['sale_date'].agg(['min','max']).reset_index()
    
    sales = sales[(sales['min'] >= '2019-01-01') & (sales['max'] <= '2019-03-31')]

    result = pd.merge(product, sales, how = 'inner', on = 'product_id')[['product_id', 'product_name']]

    return result
