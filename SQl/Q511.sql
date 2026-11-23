select player_id, min(event_date) as first_login
from Activity
group by player_id


-- import pandas as pd

-- def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
--     return activity.groupby(by='player_id')['event_date'].min().reset_index().rename(columns={
--         'event_date': 'first_login'
--     })