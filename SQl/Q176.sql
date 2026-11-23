select Coalesce(max(salary), null) as SecondHighestSalary
from Employee
where salary < (
    select max(salary) from Employee
)


-- import pandas as pd

-- def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
--     unique_salaries = employee['salary'].drop_duplicates().nlargest(2)

--     if len(unique_salaries) < 2:
--         val = None

--     else:
--         val = unique_salaries.iloc[-1]

--     return pd.DataFrame({
--         'SecondHighestSalary': [val]
--     })

