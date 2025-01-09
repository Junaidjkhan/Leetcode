import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    
    once = views[views['author_id'] == views['viewer_id']]

    result = once['author_id'].unique()

    result = sorted(result)

    return pd.DataFrame({'id': result})
