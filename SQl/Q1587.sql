select name, balance
from (
    select trans_id, account, sum(amount) as balance
    from Transactions
    group by account
    having sum(amount) > 10000
) as st
left join Users
on Users.account = st.account


-- import pandas as pd

-- def account_summary(users: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
--     temp = transactions.groupby('account')['amount'].sum().reset_index().rename(
--         columns={
--             'amount': 'balance'
--         }
--     )

--     return pd.merge(temp[temp['balance']>10000], users, how='left', on='account')[['name', 'balance']]