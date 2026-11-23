-- import pandas as pd
-- import numpy as np

-- def users_percentage(users: pd.DataFrame, register: pd.DataFrame) -> pd.DataFrame:
--     temp = register.groupby('contest_id')['user_id'].count().reset_index().rename(
--         columns={
--             'user_id': 'percentage'
--         }
--     )

--     temp['percentage'] = np.round(temp['percentage'] / len(users) * 100, 2)

--     return temp.sort_values(by=['percentage', 'contest_id'], ascending=[False, True])

