import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    [r,i] = players.shape

    return [r,i]
