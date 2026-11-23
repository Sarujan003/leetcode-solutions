-- import pandas as pd

-- def big_countries(world: pd.DataFrame) -> pd.DataFrame:
--     result = world[(world['area'] >= 3000000) | (world['population'] >= 25000000)]

--     return result[['name','area','population']]


select name, population, area
from World
where area >= 3000000 or population >= 25000000