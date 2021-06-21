CREATE DEFINER=`root`@`localhost` PROCEDURE `p8`(x int)
BEGIN
	declare y int default 1;
    l1:loop
		select y;  # y 출력
        set y=y+1;  # y 1증가
        if y<=x then iterate l1;  # 반복할 조건
        end if;
        leave l1;
	end loop;
END