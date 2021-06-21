CREATE DEFINER=`root`@`localhost` PROCEDURE `p10`(x int)
BEGIN
	declare y int default 1;
    while y<=x do
		select y;
        set y=y+1;
	end while;
END