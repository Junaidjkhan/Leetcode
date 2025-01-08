import pandas as pd

def user_activity(activity: pd.DataFrame) -> pd.DataFrame:
    active_users = activity.groupby('activity_date')['user_id'].nunique().reset_index().rename(columns= {'activity_date':'day','user_id':'active_users'})

    return active_users[active_users.day.between("2019-06-28",
                                           "2019-07-27")]
