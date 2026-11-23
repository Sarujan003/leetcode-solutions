select filter.name as Department, Employee.name as Employee, Employee.salary as Salary
from Employee
left join (
    select max(Employee.salary) as max_salary, Employee.departmentId, Department.name
    from Employee
    left join Department
    on Employee.departmentId = Department.id
    group by Department.name
) as filter
on Employee.departmentId = filter.departmentId
where salary = filter.max_salary


