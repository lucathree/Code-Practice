CREATE DEFINER=`root`@`localhost` PROCEDURE `cursor_test`()
BEGIN
	declare enum int;
    declare ename varchar(20);
    declare sal int;
    #cursor: 여러줄, 여러컬럼으로 구성된 검색결과
    declare done tinyint default 0;
    declare c1 cursor for select employee_id, last_name, salary from employees;
    declare continue handler for not found set done=1;  #반복조건으로 사용
    # cursor에서 한 줄씩 fetch. 언제까지? not found(커서에 읽을 줄이 더 없다)까지.
    # open => fetch(한줄씩출력):반복 => not found 도달 => close
    # 1:True(값이 있을 때), 0:False
    open c1;
    l1:loop
		fetch from c1 into enum, ename, sal;  #커서 c1에서 한 줄씩 읽음
        if done then leave l1;  #not found이면 루프 빠져나감
        end if;
        select enum, ename, sal;  #변수값 출력
	end loop;
    close c1;
END