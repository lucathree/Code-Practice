use encore;

#4-1
select last_name, department_id, department_name
from employees
join departments
using (department_id);

#4-2
select job_id, location_id
from employees e join departments d
using (department_id)
where department_id = 80;

#4-3
select e.last_name, d.department_name, l.location_id, l.city
from employees e
join departments d
on e.department_id = d.department_id
join locations l
on d.location_id = l.location_id
where e.commission_pct is not null;

#4-4
select last_name, department_name
from employees e
join departments d
using (department_id)
where last_name like '%a%';

#4-5
select last_name, job_id, department_id, department_name
from employees
join departments
using (department_id)
join locations
using (location_id)
where city = 'Toronto';

#4-6
select e.last_name Employee, e.employee_id 'EMP#', m.last_name Manager, e.manager_id 'Mgr#'
from employees e
join employees m
on e.manager_id = m.employee_id;

#4-7
select e.last_name Employee, e.employee_id 'EMP#', m.last_name Manager, e.manager_id 'Mgr#'
from employees e
left outer join employees m
on e.manager_id = m.employee_id
order by e.employee_id;

#4-8
select e.department_id DEPARTMENT, e.last_name EMPLOYEE, c.last_name COLLEAGUE
from employees e
join employees c
using (department_id)
where not e.last_name = c.last_name
order by e.department_id;

#4-10
select h.last_name, h.hire_date
from employees e
join employees h
where e.last_name = 'Davies'
and e.hire_date < h.hire_date;

#4-11
select e.last_name Employee, e.hire_date 'Emp Hired', m.last_name Manager, m.hire_date 'Mgr Hired'
from employees e
join employees m
on e.manager_id = m.employee_id
where e.hire_date < m.hire_date;