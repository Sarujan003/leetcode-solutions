-- select Examinations.student_id, subject_name,count(Examinations.student_id) as attended_exams
-- from Examinations
-- left join Students
-- on Students.student_id = Examinations.student_id
-- group by Examinations.student_id, subject_name

-- select *
-- from Students
-- cross join Subjects

-- select *
-- from (
--     select *
--     from Students
--     cross join Subjects
-- ) as ct
-- left join Examinations
-- on ct.student_id = Examinations.student_id

select ct.*, COALESCE(rt.attended_exams, 0) as attended_exams
from (
    select *
    from Students
    cross join Subjects
) as ct

left join (
    select Examinations.student_id, subject_name,count(Examinations.student_id) as attended_exams
    from Examinations
    left join Students
    on Students.student_id = Examinations.student_id
    group by Examinations.student_id, subject_name
) as rt

on rt.student_id = ct.student_id and rt.subject_name = ct.subject_name 

order by ct.student_id, ct.subject_name

