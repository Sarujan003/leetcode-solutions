-- import pandas as pd

-- def employee_bonus(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:
--     result = pd.merge(employee, bonus, how='left', on='empId')

--     return result[(result['bonus']< 1000) | (result['bonus'].isna())][['name', 'bonus']]


select name, bonus
from Employee
left join Bonus
on Employee.empId = Bonus.empId

WHERE Bonus.bonus < 1000 or Bonus.bonus is null