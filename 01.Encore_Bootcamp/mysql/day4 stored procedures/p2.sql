CREATE DEFINER=`root`@`localhost` PROCEDURE `p2`(enum int, out ename varchar(20))
BEGIN
	select last_name into ename from employees
    where employee_id = enum;
END