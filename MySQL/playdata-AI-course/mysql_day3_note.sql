use encore;

#DML문: insert, update, delete
#insert into 테이블명(컬럼명...) values(값들...);

create table emp1
as
select employee_id as emp_id, last_name as name, salary as sal, department_id as dept_id
from employees
where 1=0;

desc emp1;

#alter table: 테이블 구조를 수정. 컬럼추가, 삭제, 수정, 제약조건 추가
alter table emp1
add foreign key(dept_id) references departments(department_id);

#emp_id에 primary_key 제약조건 추가
alter table emp1
add primary key(emp_id);

delete from emp1 where dept_id<>80;

insert into emp1 values(200, 'aaa', 5000, 70);

select * from emp1;
select *from departments;

delete from departments where department_id = 70;

#UPDATE문
SET SQL_SAFE_UPDATES = 0;

update emp set salary = 15000
where last_name = 'Tucker';

delete from emp where deptartment_id = 70;

#트랜잭션
delete from emp1 where emp_id >= 200;
set autocommit = 0;  #자동커밋 해제
insert into emp1 values(200, 'bbb', 15000, 70);
insert into emp1 values(201, 'ccc', 5000, 90);
insert into emp1 values(202, 'ddd', 4000, 100);

select * from emp1;

savepoint a;

update emp1 set name='new bbb', sal='12345' where emp_id=200;

savepoint b;

delete from emp1 where emp_id=202;

rollback;

rollback to b;

/*
<테이블 생성>
create table 이름(
컬럼명 타입(크기) [제약조건],
컬럼명 타입(크기) [제약조건],
컬럼명 타입(크기) default '기본값'
);

<타입>
정수: int, integer
실수: float
문자: char(크기) - 고정크기 /  varchar(크기) - 가변크기
대용량 텍스트: longtext (4GB)
날짜: date - '년-월-일' / datetime - '년-월-일 시:분:초'
*/

create table test2(
num int auto_increment primary key, #auto_increment - 1씩 늘어나며 자동으로 입력
name varchar(20) not null,
home varchar(50) default '서울',
w_date datetime default now(),
msg varchar(200)
);

insert into test2(name, msg) values('aaa', 'hello');
insert into test2(name, home, msg) values('aaa', '안양', '안녕하세요');

#테이블 수정: 테이블 구조 변경, 컬럼추가, 컬럼삭제, 컬럼의 타입이나 크기 변경
/*
컬럼추가
alter table 테이블명
add (컬럼명 타입(크기))
*/

alter table test2
add (pwd varchar(10));

/*
컬럼변경 (타입이나 크기 변경)
alter table 테이블명
modify (컬럼명 새타입(크기))
*/

alter table test2
modify pwd varchar(20);

desc test2;

/*
컬럼삭제
alter table 테이블명
drop column 컬럼명

drop column으로는 한번에 컬럼 하나만 삭제가 가능하다
"drop column col1, col2" 사용불가
*/
alter table test2
drop column pwd;

alter table test2
add col1 varchar(10);

alter table test2
add col2 varchar(10);

#테이블 이름 변경
alter table test2
rename newtest;

#컬럼 이름 변경
alter table newtest
change col1 newcol varchar(10);

select * from newtest;
delete from newtest;
rollback;  #delete는 rollback 가능

truncate table newtest;
rollback;  #truncate(전체행 삭제)는 rollback 불가능