import pandas as pd

def project_employees_i(project: pd.DataFrame, employee: pd.DataFrame) -> pd.DataFrame:
    avg_exp = project.merge(employee, how = 'left', left_on = 'employee_id', right_on = 'employee_id')

    df = avg_exp.groupby('project_id')['experience_years'].mean().round(2).rename('average_years').reset_index()
    
    return pd.DataFrame(df)
