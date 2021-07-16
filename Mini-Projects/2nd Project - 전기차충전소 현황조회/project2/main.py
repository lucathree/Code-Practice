import tkinter as tk
from tkinter import messagebox
import userModel as um
import stationModel as stm


class Root(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)
        self.title('전기차 충전소 현황')
        self.geometry('1200x800+400+150')
        self.resizable(True, False)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()


class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="전기차 충전소 현황 확인", font=('Helvetica', 18, "bold")).grid(row=0, column=2, columnspan=6, pady=5)

        tk.Label(self, text="아이디:").grid(row=2, column=3, pady=10)
        self.entry_id = tk.Entry(self, width=20)
        self.entry_id.grid(row=2, column=4)

        tk.Label(self, text="비밀번호").grid(row=3, column=3, pady=10)
        self.entry_pwd = tk.Entry(self, width=20)
        self.entry_pwd.grid(row=3, column=4)

        btn = tk.Button(self, text="로그인", command=self.check_user)
        btn.grid(row=4, column=2, columnspan=3)

        tk.Button(self, text="회원가입",
                  command=lambda: master.switch_frame(RegisterPage)).grid(row=5, column=3, pady=20, sticky='e')
        tk.Button(self, text="종료",
                  command=lambda: exit()).grid(row=5, column=4, pady=20)

    def check_user(self):
        user_id = self.entry_id.get()
        pwd = self.entry_pwd.get()
        ud = um.UserDao()
        vo = ud.select(user_id)
        if vo == None:
            messagebox.showinfo("로그인 에러", "회원정보가 존재하지 않습니다")
        else:
            if pwd == vo.pwd:
                um.UserService.login_id = user_id
                r = Root()
                r.switch_frame(SearchPage)
            else:
                messagebox.showinfo("로그인 에러", "비밀번호가 틀립니다")


class RegisterPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="회원가입", font=('Helvetica', 18, "bold")).grid(row=0, column=2, columnspan=6, pady=5)

        tk.Label(self, text="아이디:").grid(row=2, column=3, pady=10)
        self.entry_id = tk.Entry(self, width=20)
        self.entry_id.grid(row=2, column=4)

        tk.Label(self, text="비밀번호").grid(row=3, column=3, pady=10)
        self.entry_pwd = tk.Entry(self, width=20)
        self.entry_pwd.grid(row=3, column=4)

        tk.Label(self, text="닉네임").grid(row=4, column=3, pady=10)
        self.entry_nickname = tk.Entry(self, width=20)
        self.entry_nickname.grid(row=4, column=4)

        btn1 = tk.Button(self, text="회원가입", command=self.register)
        btn1.grid(row=5, column=2, columnspan=3)

        btn2 = tk.Button(self, text="돌아가기", command=lambda: master.switch_frame(StartPage))
        btn2.grid(row=6, column=2, columnspan=3)

    def register(self):
        user_id = self.entry_id.get()
        pwd = self.entry_pwd.get()
        nickname = self.entry_nickname.get()
        ud = um.UserDao()
        try:
            ud.insert(um.UserVo(user_id, pwd, nickname))
        except Exception as e:
            messagebox.showinfo("회원가입에러", e)
        else:
            messagebox.showinfo("Success", "회원가입이 완료되었습니다!")


class SearchPage(tk.Frame):
    df = []

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="지역별 전기차 충전소 현황 검색",
                 font=('Helvetica', 18, "bold")).grid(row=0, column=2, columnspan=7, pady=5)
        tk.Label(self, text="검색할 지역:").grid(row=1, column=3, pady=10)
        self.entry_area = tk.Entry(self, width=20)
        self.entry_area.grid(row=1, column=4)
        self.entry_area.bind('<Return>', self.search_cs)

        self.listbox = tk.Listbox(self, width=40, height=15, justify='center')
        self.listbox.bind('<<ListboxSelect>>', self.onselect)
        self.listbox.grid(row=2, column=0, columnspan=5, sticky='ne')

        self.label1 = tk.Label(self, text='충전소명:\n충전기ID:\n충전기타입:\n주소:\n상태:', justify='left')
        self.label1.grid(row=2, column=6,columnspan=2, sticky='ne')

        self.label2 = tk.Label(self, text='검색된 충전소 수:')
        self.label2.grid(row=3, column=4)

    def search_cs(self, e):
        if self.listbox is not None:
            self.listbox.delete(0, 'end')
            area = self.entry_area.get()
            s = stm.StationDao()
            self.df = s.make_df(area)
            for i in range(0, len(self.df['충전소명'])):
                self.listbox.insert(i, self.df['충전소명'][i])
            res = '검색된 충전소 수: '+ str(len(self.df['충전소명']))
            self.label2.config(text=res)

    def onselect(self, e):
        selection = e.widget.curselection()
        index = selection[0]
        res = self.df.iloc[index]
        print(res)
        cpid = res.values[0]
        csnm = res.values[1]
        cpnm = res.values[2]
        addr = res.values[3]
        status = res.values[4]
        msg = f'충전소명: {csnm}\n충전기ID: {cpid}\n충전기타입: {cpnm}\n주소: {addr}\n상태: {status}'
        self.label1.config(text=msg)


if __name__ == "__main__":
    window = Root()
    window.mainloop()
