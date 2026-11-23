select Weather.id
from Weather
join (
    SELECT id, DATE_ADD(recordDate, INTERVAL 1 DAY) AS recordDate, temperature 
    FROM Weather
) as w1
on w1.recordDate = Weather.recordDate

where w1.temperature < Weather.temperature

-- pandas

-- import pandas as pd
-- from pandas.tseries.offsets import DateOffset

-- def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
--     weather_previous = weather.copy()
--     weather_previous['recordDate'] = weather_previous['recordDate'] + DateOffset(days=1)

--     result = pd.merge(weather, weather_previous, how='inner', on='recordDate')

--     return result[result['temperature_x'] > result['temperature_y']][['id_x']].rename(columns={'id_x': 'Id'})