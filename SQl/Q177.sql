-- import pandas as pd

-- def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
--     unique_salaries = employee['salary'].drop_duplicates().nlargest(N)

--     col_name = 'getNthHighestSalary(' + str(N) + ')'

--     if len(unique_salaries) == N and N != 0:
--         val = unique_salaries.iloc[-1]

--     else:
--         val = None

--     return pd.DataFrame({
--         col_name : [val]
--     })


