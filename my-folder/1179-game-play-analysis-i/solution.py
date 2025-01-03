import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:

    activity['event_date'] = pd.to_datetime(activity['event_date'])
    
    first_login = activity.groupby('player_id')['event_date'].agg(min).reset_index()

    return pd.DataFrame(first_login).rename(columns = {'event_date': 'first_login'})
