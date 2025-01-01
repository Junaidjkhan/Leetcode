import pandas as pd

def delete_duplicate_emails(person: pd.DataFrame) -> None:
    email = person.sort_values(by='id', inplace= True)

    person.drop_duplicates(subset='email', keep='first', inplace=True)
