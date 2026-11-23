-- import pandas as pd

-- def project_employees_i(project: pd.DataFrame, employee: pd.DataFrame) -> pd.DataFrame:
--     return pd.merge(project, employee, how='left', on='employee_id').groupby('project_id')['experience_years'].mean().round(2).reset_index(name='average_years')


select project_id, round(avg(experience_years),2) as average_years
from Project
left join Employee
on Project.employee_id = Employee.employee_id
group by project_id