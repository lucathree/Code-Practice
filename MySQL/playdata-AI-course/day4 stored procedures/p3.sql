CREATE DEFINER=`root`@`localhost` PROCEDURE `p3`(dept_id int)
BEGIN
	declare dept_avg int default 0;
    select avg(salary) into dept_avg from employees
    group by department_id
    having department_id = dept_id;
    select dept_avg;
END