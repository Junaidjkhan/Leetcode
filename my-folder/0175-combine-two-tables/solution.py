import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame: 
    
    join = person.merge(address, how='left', left_on='personId', right_on='personId')
    
    return join[['firstName', 'lastName', 'city', 'state']]
