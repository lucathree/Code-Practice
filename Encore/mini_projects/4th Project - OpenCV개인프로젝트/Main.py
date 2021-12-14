import AppWindow as a
import tkinter as tk

def main():
    win = tk.Tk()#윈도우창
    app = a.AppWin(win, '700x580+300+200')  #가로700x세로600 크기의 창을 화면 x축:100, y출:100 위치에서 출력
    win.mainloop()

main()