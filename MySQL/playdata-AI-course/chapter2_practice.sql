use encore;

#2-1
select last_name, salary
from employees
where salary > 12000;

#2-2
select last_name, department_id
from employees
where employee_id = 176;

#2-3
select last_name, salary
from employees
where salary < 5000
or salary > 12000;

#2-4
select last_name, job_id, hire_date
from employees
where hire_date between '2006-02-20' and '2006-05-01'
order by hire_date;

#2-5
select last_name, department_id
from employees
where department_id = 50 or department_id = 20
order by last_name;

#2-6
select last_name Employee, salary 'Monthly Salary'
from employees
where (salary > 5000 and salary < 12000)
and (department_id = 20 or department_id = 50);

#2-7
select last_name, hire_date
from employees
where hire_date like '__04%';

#2-8
select last_name, job_id
from employees
where manager_id is null;

#2-9
select last_name, salary, commission_pct
from employees
where commission_pct is not null
order by salary desc, commission_pct desc;

#2-10
select last_name
from employees
where last_name like '__a%';

#2-11
select last_name
from employees
where last_name like '%a%e%' 
or last_name like '%e%a%';

#2-12
select last_name, job_id, salary
from employees
where (job_id like '%CLERK' or job_id like 'SA%')
and salary not in (2500, 3500, 7000);

#2-13
select last_name Employee, salary 'Monthly Salary', commission_pct
from employees
where commission_pct = .2;