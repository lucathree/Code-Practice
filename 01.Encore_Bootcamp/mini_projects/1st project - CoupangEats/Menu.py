# import libraries

from project1 import memModel as mem
from project1 import orderModel as order
from project1 import storeModel as store
from project1 import productModel as product
from project1 import reviewModel as review
from project1 import menusearchModel as menuSearch
from project1 import ordercheckModel as ordercheck


class Menu:

    # 로그인 아이디 설정
    # login_id = None

    def __init__(self):
        self.memService = mem.MemService()
        self.orderService = order.OrderService()
        self.storeService = store.StoreService()
        self.reviewService = review.ReviewService()
        self.productService = product.ProductService()
        self.menuSearchService = menuSearch.MenuSearchService()
        self.orderCheckService = ordercheck.OrdercheckService()
    # 큰 메뉴 설정

    def run(self):
        flag = True

        while True:
            menu = input('1.회원가입 2.로그인 3.종료')
            if menu == '1':
                self.memService.join()
            elif menu == '2':
                self.memService.login()
                if mem.MemService.login_id == None:
                    continue
                else:
                    self.MenuRun()

            elif menu == '3':
                print('서비스 이용해 주셔서 감사합니다')
                break

    # 로그인후 작은메뉴 설정

    def MenuRun(self):
        print('원하는 기능 선택')
        while True:
            menu = input('1. 주문하기, 2. 점포관리, 3.회원정보 수정, 4.회원탈퇴, 5. 로그아웃')
            if menu == '1':
                self.orderRun()
            elif menu == '2':
                self.storeRun()
            elif menu == '3':
                self.memService.editMyInfo()
            elif menu == '4':
                self.memService.delMyInfo()
            elif menu == '5':
                self.memService.logout()
                if mem.MemService.login_id == None:
                    break
                else:
                    continue

    # 가. 주문하기 기능

    def orderRun(self):
        while True:
            menu = input(
                '1 메뉴검색 2.점포목록 출력 3.점포검색 4. 음식타입검색 5.주문하기 6. 주문확인 7.주문취소 8.리뷰등록 9.리뷰목록출력 0.나가기')
            if menu == '1':  # 메뉴검색
                self.menuSearchService.getByName()
            elif menu == '2':  # 점포목록출력
                self.storeService.getStores()
            elif menu == '3':  # 점포검색
                self.storeService.getByStore()
            elif menu == '4':  # 음식타입검색
                self.menuSearchService.getByType()
            elif menu == '5':  # 주문하기
                self.orderService.addOrder()
            elif menu == '6':  # 주문확인
                self.orderService.getAllMyOrderDetails()
            elif menu == '7':  # 주문취소
                self.orderService.cancelMyOrder()
            elif menu == '8':  # 리뷰등록
                self.reviewService.addReview()
            elif menu == '9':  # 리뷰목록출력
                self.reviewService.printReview()
            elif menu == '0':  # 나가기
                break

    # 나, 점포관리 기능

    def storeRun(self):
        while True:
            menu = input(
                '1.점포등록 2.점포확인 3.상품확인 4.상품추가 5.상품수정 6.상품삭제 \
                    7.미확인주문내역 8.전체주문내역 9.상세 주문내역 확인 10.점포등록취소 0.나가기')
            if menu == '1':  # 1.점포등록
                self.storeService.addStore()
            elif menu == '2':  # .점포 확인
                self.storeService.printMyStore()
            elif menu == '3':  # 상품확인
                self.productService.printAll()
            elif menu == '4':  # 상품추가
                self.productService.addProduct()
            elif menu == '5':  # 상품수정
                self.productService.editProduct()
            elif menu == '6':  # 상품삭제
                self.productService.delProduct()
            elif menu == '7':  # 미확인주문내역
                self.orderCheckService.checkOrderStatus()
            elif menu == '8':  # 전체주문내역
                self.orderCheckService.checkAllOrder()
            elif menu == '9':  # 상세주문내역 확인
                self.orderCheckService.checkOrderDetail()
            elif menu == '10':  # 점포등록취소
                self.storeService.delStore()
            elif menu == '0':
                break
