CREATE DEFINER=`root`@`localhost` PROCEDURE `p4`(enum int)
BEGIN
	declare sal int default 0;
    declare msg varchar(20);
    select salary into sal from employees where employee_id=enum;
    if sal > 10000 then set msg='10000 초과';
    else set msg='10000 이하';
    end if;
    select msg;
END