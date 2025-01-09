import pandas as pd

def reformat_table(department: pd.DataFrame) -> pd.DataFrame:
    
    prefixes = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]

    reformed = department.pivot(columns ='month', index='id', values='revenue')

    reformed = reformed.reindex(columns = prefixes)

    reformed.rename(columns = lambda prefix: prefix + '_Revenue', inplace = True)

    reformed.reset_index(inplace =True)

    return pd.DataFrame(reformed)
