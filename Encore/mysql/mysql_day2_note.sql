select last_name, department_id, department_name
from employees
natural join departments;

#4-9 (과제에 포함되지 않았던 부분)
select last_name, job_id, department_name, salary, gra
from employees join departments
using (department_id)
join job_grades
on salary between lowest_sal and highest_sal;

#그룹함수 - 집합으로 묶어서 하나의 아웃풋으로 처리
select avg(salary), max(salary), min(salary), sum(salary)
from employees
where job_id like '%REP%';

#단일행함수 - 한줄 한줄 마다 아웃풋 처리
select ucase(last_name), last_name
from employees;

select count(commission_pct)
from employees
where department_id=80;

#그룹함수는 널인값을 빼고 계산
#ifnull(p1, p2):p1 컬럼이 null이면 p2로 대체
select avg(ifnull(commission_pct, 0))
from employees;

select department_id, avg(salary)
from employees
group by department_id
order by avg(salary) desc;

select department_id, job_id, sum(salary)
from employees
group by department_id, job_id;

select department_id, count(last_name)
from employees
group by department_id;

select department_id, max(salary)
from employees
group by department_id
having max(salary) > 10000;

#단일행 서브쿼리 실행
select last_name, job_id, salary
from employees
where job_id = (select job_id from employees where employee_id = 141)
and salary > (select salary from employees where employee_id = 143);

#서브쿼리에서 그룹 함수 사용
select last_name, job_id, salary
from employees
where salary = (select min(salary) from employees);

#DDL: 데이터 정의어. create table, create view, create procedure,create function
#DML: 데이터 조작어. insert, update, delete => commit. 
#DCL: 데이터 제어어. grant, revoke 권한 부여, 빼앗음

#char(10)  #고정길이
#varchar(10)  #가변길이

create table test1(
id varchar(20) primary key,
pwd varchar(20) not null,
name varchar(20)  # not null 조건이 없고 프라이머리 키도 없기 때문에 값이 없어도 행 입력 가능
);

desc test1;
insert into test1 values('aaa', '111', 'nameA');  #테이블의 모든 컬럼에 값을 넣겠다고 선언.
insert into test1(name, pwd, id) values('nameB', '222', 'bbb');  #테이블의 지정 컬럼에 값을 넣겠다고 선언.
insert into test1(id, pwd) values('ccc', '333');  #name에는 자동으로 null 입력
insert into test1 values('ddd', '444', null);  #컬럼 이름을 명시하지 않은 경우 모든 값을 입력해줘야 하므로 null을 직접 입력

alter table test1
add column(hire_date date);

insert into test1 values('eee', '555', 'nameE', sysdate());
select * from test1; 

#다른 테이블의 구조를 복사해서 테이블 생성
create table emp
as
select * from employees where 1=0;  #'1=0': 불가능한 조건. 행은 복사하지 말고 테이블의 구조만 복사하라는 의미

insert into emp
select * from employees where job_id like '%REP%';

select * from emp;

# update 테이블 set 컬럼명=새값, 컬럼명=새값  # 이렇게만 쓰면 컬럼의 모든 값이 지정된 값으로 통일된다! WHERE 조건을 넣어줘서 그런 부분을 최소화
update test1 set name='nameC' where id='ccc';
update test1 set name='nameD', hire_date=sysdate() where id='ddd';
update test1 set hire_date=date('2020-05-05') where id='ddd';
select * from test1;

# delete from 테이블 where 조건;
# 다른 테이블을 기반으로 행 삭제도 가능 (서브쿼리 사용)
 
delete from test1 where id='ccc';
set sql_safe_updates = 0;  # 세이프모드 해제, 행 전체 변경 예방해제
delete from test1;  # 조건이 없으므로 모든 행을 삭제시킨다!
drop table test1;

create table test1(
id varchar(20) primary key,
pwd varchar(20) not null,
name varchar(20) default '아무개'  # null 대신 입력될 기본값 지정
);

insert into test1(id, pwd) values('aaa', '111');
insert into test1 values('bbb', '222', 'nameb');
update test1 set name=default where id='bbb';

select * from test1

# merge: 테이블 합병. A, B를 합친다 
# A에 합치는데 B에는 있는데 A에는 없는 줄은 A에 새로 추가하고 A, B 양쪽에 다 있는 줄은 A의 행을 B의 값으로 갱신
insert into emp
select * from employees as e
on duplicate key update emp.employee_id=e.employee_id,
emp.first_name=e.first_name,
emp.last_name=e.last_name,
emp.email=e.email,
emp.phone_number=e.phone_number,
emp.hire_date=e.hire_date,
emp.job_id=e.job_id,
emp.salary=e.salary,
emp.commission_pct=e.commission_pct,
emp.manager_id=e.manager_id,
emp.department_id=e.department_id;

