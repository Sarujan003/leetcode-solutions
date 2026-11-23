select class
from Courses
group by class
having count(student) >= 5


-- import pandas as pd

-- def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
--     result = courses.groupby('class')['student'].count().reset_index(name='count')

--     return result[result['count'] >= 5][['class']]

