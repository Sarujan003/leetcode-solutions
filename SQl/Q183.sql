select name as Customers
from Customers
left join Orders
on Customers.id = Orders.customerId
where Orders.id is null


-- pandas

-- import pandas as pd

-- def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
--     result = pd.merge(customers, orders, how='left', left_on='id', right_on='customerId')

--     return result[result['id_y'].isna()][['name']].rename(columns={'name': 'Customers'})