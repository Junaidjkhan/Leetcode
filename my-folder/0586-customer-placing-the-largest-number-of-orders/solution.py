import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    

    return pd.DataFrame(orders['customer_number'].mode())
