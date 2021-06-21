CREATE DEFINER=`root`@`localhost` PROCEDURE `p9`(x int)
BEGIN
	declare y int default 1;
    repeat
		select y;
        set y=y+1;
        until y>x end repeat;  #조건 만족시 반복 끝
END