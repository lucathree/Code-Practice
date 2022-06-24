CREATE DEFINER=`root`@`localhost` PROCEDURE `p5`(enum int)
BEGIN
	declare dept varchar(20);
    declare dept_id int;
    select department_id into dept_id from employees where employee_id=enum;
    if dept_id = 10 then set dept = '개발1팀';
	elseif dept_id = 20 then set dept = '개발2팀';
    elseif dept_id = 30 then set dept = '개발3팀';
    elseif dept_id = 40 then set dept = '개발4팀';
    else set dept_id = '개발팀';
    end if;
    select dept;
END