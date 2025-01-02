import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:

    weather['recordDate'] = pd.to_datetime(weather['recordDate'])

    wether_shifted = weather.copy()

    wether_shifted['recordDate'] = wether_shifted['recordDate'] + pd.to_timedelta(1, unit='D')

    merge_weather = pd.merge(weather, wether_shifted, how = 'inner', on='recordDate', suffixes = ('_today','_yesterday'))

    result = merge_weather[merge_weather['temperature_today'] > merge_weather['temperature_yesterday']][['id_today']]

    return result[['id_today']].rename(columns = {'id_today': 'Id'})
