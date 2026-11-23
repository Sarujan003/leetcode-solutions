-- import pandas as pd

-- def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
--     result =  actor_director.groupby(['actor_id','director_id'])['actor_id'].count().reset_index(name='count')

--     return result[result['count']>=3][['actor_id', 'director_id']]


select actor_id, director_id
from ActorDirector
group by actor_id, director_id
having count(*) >= 3