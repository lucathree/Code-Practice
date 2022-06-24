import myReview.add_search_del as asd

def main():
    asd.addNum1()
    asd.addNum1()
    asd.addNum2(3)
    asd.addNum2(6)
    asd.printNums()

    asd.searchNum1()
    asd.searchNum2(3)
    asd.searchNum3(2)
    asd.searchNum4(4)
    asd.searchNum5()

    asd.delNum1()
    asd.printNums()

    asd.delNum2(5)
    asd.printNums()


main()
