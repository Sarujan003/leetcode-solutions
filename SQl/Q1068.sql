-- import pandas as pd

-- def sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
--     return pd.merge(sales, product, how='left', on='product_id')[['product_name', 'year', 'price']]


select Product.product_name, Sales.year as 'year', Sales.price
from Sales
left join Product
on Product.product_id = Sales.product_id