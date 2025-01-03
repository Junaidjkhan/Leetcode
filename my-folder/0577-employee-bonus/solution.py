import pandas as pd

def employee_bonus(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:
    lowest_bonus = employee.merge(bonus, how = 'left', left_on = 'empId', right_on = 'empId' )

    lowest_bonus1 = lowest_bonus[(lowest_bonus['bonus'] < 1000) | (lowest_bonus['bonus'].isna())]

    return lowest_bonus1[['name','bonus']]
