select name
from SalesPerson
where sales_id not in (
    select sales_id
    from Company
    join Orders
    on Company.com_id = Orders.com_id
    where Company.name = 'RED'
)

-- pandas

-- import pandas as pd

-- def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:

--     com_id = company[company['name'] == 'RED']['com_id']

--     sales_id = orders[orders['com_id'].isin(com_id)]['sales_id']

--     return sales_person[~(sales_person['sales_id'].isin(sales_id))][['name']]