use encore;

select * from employees;

select * from departments;

select department_id, department_name
from departments
where department_id<50;

select last_name, 12*salary*commission_pct
from employees;

select last_name, salary, salary+300 as Salary2
from employees;

select distinct department_id from employees;  #중복값 정리하여 표시

desc employees;  #테이블 구조 표시

select employee_id, last_name, job_id, department_id
from employees
where department_id=90;

select employee_id, last_name, salary, manager_id
from employees
where manager_id in (100, 101, 201);  # IN 조건, 튜플을 사용해서 목록 내에 여러값이 있는지 한꺼번에 확인 가능

SELECT last_name
FROM employees
WHERE last_name LIKE 'W%';  # LIKE 조건, 문자 패턴이 일치하는 행을 선택 (문자검색). %의 자리에는 문자가 오지 않거나 여러개가 올 수 있고 _는 문자 하나만 와야 됨

SELECT employee_id, last_name, hire_date
FROM employees
WHERE hire_date LIKE '__05%';

SELECT employee_id, last_name, job_id, salary
FROM employees
WHERE salary >=10000
AND job_id LIKE '%man%';  
# SQL 에서도 AND / OR / NOT 조건 활용 가능
# 우선순위는 NOT > AND > OR 순. (헷갈릴 수 있으니 괄호를 사용할 것!)

SELECT last_name, job_id, department_id, hire_date
FROM employees
ORDER BY hire_date;  
# ORDER BY 조건을 사용하여 해당 열을 기준으로 행 정렬
# 별칭을 사용할 수도 있고, 여러 열을 기준으로 정렬할 수도 있다 (앞에 적는 조건 기준으로 순차적으로 정렬)

SELECT sysdate()  # 현재 시스템시간 출력
FROM DUAL;  # SQL 문법을 지키기 위한 구문, dual은 더미테이블

select * from locations;

select department_id, department_name, location_id, city
from departments
natural join locations;  # departments 와 locations 에서 location_id를 기준으로 조인

select employee_id, last_name, department_id, department_name
from employees
natural join departments;  # employees와 departments에서 department_id를 기준으로 조인

select employee_id, last_name, location_id, d.department_id
from employees e join departments d
using(department_id);  # using 을 사용

select employee_id, last_name, city, department_name
from employees e
join departments d
on e.department_id = d.department_id
join locations l
on d.location_id = l.location_id;

select e.last_name, e.department_id, d.department_name
from employees e
left outer join departments d
on (e.department_id = d.department_id);