select customer_id, count(visit_id) as count_no_trans
from Visits
where visit_id not in (
    select distinct(visit_id)
    from Transactions
)
group by customer_id


-- import pandas as pd

-- def find_customers(visits: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
--     visit_id = transactions['visit_id'].unique()

--     return visits[~visits['visit_id'].isin(visit_id)].groupby('customer_id')['visit_id'].count().reset_index().rename(
--         columns={
--             'visit_id': 'count_no_trans'
--         }
--     )