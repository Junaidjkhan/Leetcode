import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    
    Email = person.loc[person.duplicated('email'),['email']]

    return pd.DataFrame(Email['email']).rename(columns={"email": "Email"}).drop_duplicates()
