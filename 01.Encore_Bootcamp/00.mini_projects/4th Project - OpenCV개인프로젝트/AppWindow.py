import tkinter as tk
import cv2, threading
from PIL import Image
from PIL import ImageTk
from datetime import datetime


class AppWin(tk.Frame):  #AppWin 객체는 Frame(위젯을 배치하는 판). "tk.Frame" 클래스를 상속하는 객체
    def __init__(self, root=None, geo=None): # AppWin 객체의 멤버변수 정의. root:Tk()객체 geo=창 위치
        #fr = tk.Frame(self.root)
        super().__init__(root)      # 부모 생성자의 기본 윈도우 전달. =부모클래스 tk.Frame의 멤버변수를 가져옴
        self.root = root            # 기본 윈도우를 멤버변수로 저장. root = tk.TK()
        self.root.geometry(geo)     # 윈도우의 크기 및 위치 설정
        self.root.resizable(True, True)  # 윈도우의 가로, 세로 크기 재조정 가능으로 설정
        self.pack()                 # 프레임을 윈도우에 부착

        self.sub_fr = None          # 버튼 배치할 하위 프레임
        self.img_src = None         # 레이블에 출력할 이미지 값
        self.img_label = None       # 이미지 출력할 레이블
        self.ent_title = None
        self.fileName_ent = None    # 이미지 저장시 파일명 입력받을 엔트리

        self.flag = True    # 동영상 저장 실행/중지 제어
        self.flag2 = False
        self.create_widgets()

    #카메라 실행시키기
    def read_cam(self, flag, flag2):
        cap = cv2.VideoCapture(0)
        cap.set(3, 640)
        cap.set(4, 480)

        bs = cv2.createBackgroundSubtractorMOG2()

        vid_count = 1
        rec = False
        timer = 0

        codec = cv2.VideoWriter_fourcc(*'DIVX')
        out = cv2.VideoWriter('vid/cat' + str(vid_count) + '.avi', codec, 25.0, (640, 480))
        while flag():
            ret, frame = cap.read()

            if not ret:
                print('Video capture error!')
                break

            if flag2():
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                fgmask = bs.apply(gray, learningRate=-1)  # 배경과 전경 구분을 위한 마스크

                # 레이블링을 이용하여 바운딩 박스 표시
                cnt, _, stats, _ = cv2.connectedComponentsWithStats(fgmask)

                movement = False
                for i in range(1, cnt):
                    x, y, w, h, s = stats[i]

                    if s < 2000:
                        continue

                    cv2.rectangle(frame, (x, y, w, h), (0, 0, 255), 2)
                    movement = True

                time = str(datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
                cv2.putText(frame, time, (440, 460), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (10, 10, 10), 2)

                if timer == 75:
                    out.release()
                    self.write_add(time+' cat'+str(vid_count)+'.avi 움직임 녹화 완료')
                    vid_count += 1
                    timer = 0
                    rec = False
                    out = cv2.VideoWriter('vid/cat' + str(vid_count) + '.avi', codec, 25.0, (640, 480))
                elif movement == False and rec == True:
                    out.write(frame)
                    timer += 1
                elif movement == False and rec == False:
                    pass
                elif movement == True:
                    cv2.putText(frame, 'rec', (595, 440), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
                    out.write(frame)
                    timer = 0
                    rec = True

            img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # opencv[b, g, r] => tkinter:[r, g, b]
            img = Image.fromarray(img)  # opencv용 이미지배열값을 필로우용 이미지로 변환
            self.img_src = ImageTk.PhotoImage(image=img)
            self.img_label.configure(image=self.img_src)
            self.img_label.image = self.img_src
        out.release()
        cap.release()

    def start_preview(self):    #미리보기 함수. 프로그램 시작시 호출
        self.flag = True
        #쓰레드 생성
        th = threading.Thread(target=self.read_cam, args=(lambda:self.flag, lambda:self.flag2))
        th.start()  #쓰레드 시작

    def write_new(self):
        file = open('log/'+str(datetime.now().strftime("%Y-%m-%d"))+'.txt', 'w', encoding='utf-8')
        file.write(str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")+' 기록 시작\n'))
        file.close()

    def write_add(self, text):
        file = open('log/' + str(datetime.now().strftime("%Y-%m-%d")) + '.txt', 'a', encoding='utf-8')
        file.write(text+'\n')
        file.close()

    def btn1_handler(self):
        self.flag2 = True
        self.write_new()

    def btn2_handler(self):
        self.flag2 = False
        self.flag = False
        self.write_add(str(datetime.now().strftime("%Y/%m/%d %H:%M:%S")+' 기록 종료'))

    def btn3_handler(self):
        self.start_preview()

    def create_widgets(self):  # 원하는 구성요소 부착
        self.img_label = tk.Label(self, image=self.img_src)
        self.img_label.pack(pady=20)
        self.sub_fr = tk.Frame(self)
        self.sub_fr.pack()
        self.start_preview()

        self.btn1 = tk.Button(self.sub_fr, text='CCTV 촬영시작')
        self.btn2 = tk.Button(self.sub_fr, text='촬영종료')
        self.btn3 = tk.Button(self.sub_fr, text='재시작')

        #버튼 그리드 배치
        self.btn1.grid(row=0, column=0)
        self.btn2.grid(row=0, column=1)
        self.btn3.grid(row=0, column=2)

        #버튼에 핸들러 등록
        self.btn1['command'] = self.btn1_handler
        self.btn2['command'] = self.btn2_handler
        self.btn3['command'] = self.btn3_handler