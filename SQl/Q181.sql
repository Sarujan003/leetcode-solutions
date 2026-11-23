select e1.name as Employee
from Employee as e1
join Employee as e2
on e1.managerId = e2.id
where e1.salary > e2.salary


-- pandas

-- import pandas as pd

-- def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
--     result = pd.merge(employee, employee, how='inner', right_on='id', left_on='managerId')

--     return result[result['salary_x'] > result['salary_y']][['name_x']].rename(columns={'name_x': 'Employee'})

