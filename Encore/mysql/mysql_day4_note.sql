use encore;


#뷰 VIEW 생성
# create [or replace] view 뷰이름  #똑같은 이름의 뷰가 있을 경우 replace를 써서 기존 뷰를 날리고 새로운 뷰 생성
# as 서브쿼리
create or replace view view_80
as
select employee_id as emp_id, last_name as name, salary
from employees
where department_id=80;

select * from view_80;

update view_80 set name='viewww' where emp_id=145;
select * from view_80;

select last_name from employees where employee_id=145;

create or replace view emp_view
as
select last_name, department_name, city, salary
from employees join departments
using (department_id)
join locations
using (location_id);

select * from emp_view;


set @a=10; #변수 정의
select @a;

set @enum=(select employee_id from employees where last_name='Abel');
select @enum;

select employee_id, salary into @enum, @sal from employees where last_name='Abel';
select @enum, @sal;

call p1(100);

call p2(100, @ename);
select @ename;

call p3(80);

call p4(175);

call p5(202);
call p6(202);

call p7(8);
call p8(8);
call p9(8);
call p10(8);

call cursor_test();

set global log_bin_trust_function_creators=1;  #MySQL function 생성 제한 해제

select employee_id, f2(last_name, first_name) as name, salary
from employees;

/*
트리거: insert, update, delete 동작이 실행될 때마다 이 동작 전이나 후에 실행할 코드를 등록하는 방법
생성
create trigger 트리거이름
전후 (after/before) 동작(insert/update/delete)
on 테이블명
for each row
*/

select * from emp1;

#emp1에 insert할 때마다 실행
delimiter $$
create trigger insert_emp1_trig
after insert
on emp1
for each row
begin
	set @msg = concat(new.name, '님 새로 추가됨');
end$$
delimiter ;

insert into emp1 values(300, 'aaa', 10000, 80);
select @msg;

create table emp1_backup(
num int auto_increment primary key,
id int,
cmd varchar(20),
old_sal int,
new_sal int
);

delimiter $$
create trigger emp1_trig1
after insert
on emp1
for each row
begin
	insert into emp1_backup(id, cmd, new_sal) values(new.emp_id, 'insert', new.sal);
end$$
delimiter ;

insert into emp1 values(301, 'bbb', 15000, 80);
select * from emp1_backup

delimiter $$
create trigger emp1_trig2
after update
on emp1
for each row
begin
	insert into emp1_backup(id, cmd, old_sal, new_sal)
    values(old.emp_id, 'update', old.sal, new.sal);
end$$
delimiter ;

update emp1 set sal=24000 where emp_id=200;
select * from emp1_backup;