select max(num) as num
from (
    select num
    from MyNumbers
    group by num
    having count(*) = 1
) as unique_numbers


-- pandas

-- import pandas as pd

-- def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
--     result = my_numbers.groupby('num')['num'].count().reset_index(name='count')

--     maximum = result[result['count']==1]['num'].max()

--     return pd.DataFrame({
--         'num': [maximum]
--     })