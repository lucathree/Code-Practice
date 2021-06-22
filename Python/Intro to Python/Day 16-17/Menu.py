import member.memModel as mem
import member.boardModel as b

class Menu:
    def __init__(self):
        self.memService = mem.MemService()
        self.boardService = b.BoardService()

    def run(self):
        while True:
            m = input('1.회원관리 2.게시판 3.종료')
            if m == '1':
                self.memRun()
            elif m == '2':
                if mem.MemService.login_id == None:
                    print('로그인 후 사용 가능합니다')
                else:
                    self.boardRun()
            elif m == '3':
                break

    def memRun(self):
        while True:
            m = input('1.회원가입 2.로그인 3.내정보확인 4.내정보수정 5.로그아웃 6.탈퇴 7.메뉴나감')
            if m=='1':
                self.memService.join()
            elif m=='2':
                self.memService.login()
            elif m=='3':
                self.memService.printMyInfo()
            elif m=='4':
                self.memService.editMyInfo()
            elif m=='5':
                self.memService.logout()
            elif m=='6':
                self.memService.delMyInfo()
            elif m=='7':
                break

    def boardRun(self):
        while True:
            m = input('1.글작성 2.글목록 3.번호로검색 4.작성자로검색 5.제목으로검색 6.내용으로검색 7.글수정 8.글삭제 9.메뉴나감')
            if m=='1':
                self.boardService.addBoard()
            elif m=='2':
                self.boardService.getAll()
            elif m=='3':
                self.boardService.getByNum()
            elif m=='4':
                self.boardService.getByWriter()
            elif m=='5':
                self.boardService.getByTitle()
            elif m=='6':
                self.boardService.getByContent()
            elif m=='7':
                self.boardService.editBoard()
            elif m=='8':
                self.boardService.delBoard()
            elif m=='9':
                break