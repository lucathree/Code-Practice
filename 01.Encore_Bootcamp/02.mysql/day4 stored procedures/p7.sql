CREATE DEFINER=`root`@`localhost` PROCEDURE `p7`(x int)
BEGIN
	declare y int default 1;
    l1:loop
		select y;  # y 출력
        set y=y+1;  # y 1증가
        if y>x then leave l1;  # y가 x보다 커지면 루프 종료
        end if;
	end loop;
END