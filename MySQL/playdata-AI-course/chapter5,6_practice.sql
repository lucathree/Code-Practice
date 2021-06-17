use encore;

#5-1
#그룹 함수는 여러 행에 적용되어 그룹 당 하나의 결과를 출력합니다
#정답: True

#5-2
#그룹 함수는 계산에 널을 포함합니다.
#정답: False

#5-3
#WHERE 절은 그룹 계산에 행을 포함시키기 전에 행을 제한합니다.
#정답: True

#5-4
SELECT Round(Max(salary)) Maximum, Round(Min(salary)) Minimum, Round(Sum(salary)) Sum, Round(Avg(salary)) Average
FROM employees;

#5-5
SELECT job_id, Round(Max(salary)) Maximum, Round(Min(salary)) Minimum, Round(Sum(salary)) Sum, Round(Avg(salary)) Average
FROM employees
GROUP BY job_id;

#5-6
SELECT job_id, count(*)
FROM employees
GROUP BY job_id;

#5-7
select count(distinct manager_id) as 'Number of Managers'
from employees;

#5-8
select (max(salary) - min(salary)) as DIFFERENCE
from employees;

#5-9
select manager_id, min(salary)
from employees
where manager_id is not null
group by manager_id
having min(salary) > 6000
order by min(salary) desc;

#5-10
select department_name as 'Name', location_id 'Location', count(*) as 'Number of People', round(avg(salary),2) as 'Salary'
from employees
join departments
using (department_id)
group by department_name;

#5-11
#if함수 활용 - if(수식, 참일때실행문, 거짓일때실행문)
SELECT IF(hire_date like '2005%', last_name, null)
FROM employees;

#ifnull(컬럼/값, 널일때실행문)
select last_name, commission_pct, 12*salary+12*salary*commission_pct  #커미션이 없는 경우는 값이 널이 되어버린다
from employees;

select last_name, commission_pct, 12*salary+12*salary*ifnull(commission_pct, 0)  #커미션이 없는 경우 0을 곱한다
from employees;

#nullif(exp1, exp2): exp1과 exp2가 같으면 null, 같지 않으면 exp1 반환
select last_name, length(last_name), first_name, length(first_name), nullif(length(last_name), length(first_name))
from employees;

#case문: 비교할 조건이 여러개 일때 사용
/*
case exp
	when 값1 then 실행문
    when 값2 then 실행문
    when 값3 then 실행문
    else 실행문
end as '컬럼별칭'
*/

SELECT department_id,
case department_id
	when 10 then '10번 부서'
    when 20 then '20번 부서'
    when 30 then '30번 부서'
	else '이외 부서'
end as '부서명'
from employees;

select count(*) TOTAL,
sum(if(hire_date like '2005%', 1, 0)) '2005',
sum(if(hire_date like '2006%', 1, 0)) '2006',
sum(if(hire_date like '2007%', 1, 0)) '2007',
sum(if(hire_date like '2008%', 1, 0)) '2008'
from employees;

#5-12
select job_id Job,
sum(case department_id when 20 then salary end) Dept20,
sum(case department_id when 50 then salary end) Dept50,
sum(case department_id when 80 then salary end) Dept80,
sum(case department_id when 90 then salary end) Dept90,
sum(salary) Total
from employees
group by Job;

#6-1
select last_name, hire_date
from employees
where department_id = (select department_id from employees where last_name = 'Zlotkey')
and not last_name = 'Zlotkey';

#6-2
select employee_id, last_name, salary
from employees
where salary > (select avg(salary) from employees)
order by salary;

#6-3
select employee_id, last_name
from employees
where department_id in (select department_id from employees where last_name like '%u%');

#6-4
select last_name, department_id, job_id
from employees
where department_id in (select department_id from departments where location_id = 1700);

#6-5
select last_name, salary
from employees
where manager_id in (select employee_id from employees where last_name = 'King');

#6-6
select department_id, last_name, job_id
from employees
where department_id = (select department_id from departments where department_name = 'Executive');

#6-7
select employee_id, last_name, salary
from employees
where salary > (select avg(salary) from employees)
and department_id in (select department_id from employees where last_name like '%u%');