-- import pandas as pd

-- def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
--     scores['rank'] = scores['score'].rank(ascending=False, method='dense')

--     return scores[['score', 'rank']].sort_values(by='rank')



select score, DENSE_RANK() over (order by score desc) as 'rank'
from Scores