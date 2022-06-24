CREATE DEFINER=`root`@`localhost` PROCEDURE `p6`(enum int)
BEGIN
	declare dept varchar(20);
    declare dept_id int;
    select department_id into dept_id from employees where employee_id=enum;
    case
		when dept_id = 10 then set dept = '개발1팀';
		when dept_id = 20 then set dept = '개발2팀';
		when dept_id = 30 then set dept = '개발3팀';
		when dept_id = 40 then set dept = '개발4팀';
		else set dept_id = '개발팀';
    end case;
    select dept;
END