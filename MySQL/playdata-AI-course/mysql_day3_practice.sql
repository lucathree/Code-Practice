#게시판 만들기 - 게시판, 회원정보
#회원정보 테이블 생성
create table members(
id varchar(20) primary key, #행 대표값
pwd varchar(20) not null,
name varchar(20) not null,
email varchar(100) unique  #중복허용안함
);

#3명 회원가입
insert into member values('aaa', '111', 'name_a', 'aaa@mail.com');
insert into member values('bbb', '222', 'name_b', 'bbb@mail.com');
insert into member values('ccc', '333', 'name_c', 'ccc@mail.com');

#게시판 테이블 생성
create table board(
num int auto_increment primary key,
writer varchar(20),
w_date datetime,
title varchar(50),
content varchar(500),
constraint foreign key(writer) references members(id) on delete cascade  #members 테이블의 id를 외부 키로 참조하겠다. members의 참조 값이 사라지면 board의 행도 삭제
);

#게시판 글 작성
insert into board(writer, w_date, title, content) values('aaa', sysdate(), 'title1', 'hello world');
# insert into board(writer, w_date, title, content) values('abc', sysdate(), 'title2', 'hello world2');  #writer의 값이 members 테이블에서 참조할 수 없기 때문에 에러발생. 에러때문에 num 값은 한번 건너뜀
insert into board(writer, w_date, title, content) values('bbb', sysdate(), 'title3', 'hello world3');

#회원탈퇴
delete from members where id='bbb';  # foreign key로 연결되어있는 글이 있으면 삭제 불가. 글을 먼저 삭제 시키고 멤버에서 삭제시켜야 한다

#글 삭제 없이 회원탈퇴를 시켜주는 법
drop table board;
create table board(
num int auto_increment primary key,
writer varchar(20),
w_date datetime,
title varchar(50),
content varchar(500),
constraint foreign key(writer) references members(id) on delete set null  #members의 참조 값이 사라지면 board의 행에서 writer 값만 null로 바꾸고 나머지 행은 그대로 둔다
);

insert into board(writer, w_date, title, content) values('ccc', sysdate(), 'title', 'hello world');
delete from members where id='ccc';
select * from board;  #memebers에서 ccc의 행이 삭제되었지만 board의 글은 writer만 null로 바뀐채로 남아있다