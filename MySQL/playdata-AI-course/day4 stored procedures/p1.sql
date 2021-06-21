CREATE DEFINER=`root`@`localhost` PROCEDURE `p1`(enum int)
BEGIN
	declare ename varchar(20); #변수선언
    select last_name into ename
    from employees where employee_id = enum;
    select ename;
END