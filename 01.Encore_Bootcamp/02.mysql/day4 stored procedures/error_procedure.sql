CREATE DEFINER=`root`@`localhost` PROCEDURE `errorProc`()
BEGIN
	declare i int;
    declare hap int;
    declare saveHap int;
    
    declare exit handler for 1264
    begin
		select concat('int 오버플로 직전의 합계 --> ', saveHap);
        select concat('1+2+3+...+',i ,'=오버플로');
	end;
    
    set i = 1;
    set hap = 0;
    
    while (true) do
		set saveHap = hap;
        set hap = hap + i;
        set i = i + 1;
	end while;
END