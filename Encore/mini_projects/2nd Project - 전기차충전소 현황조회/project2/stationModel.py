import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

class StationVo:
    def __init__(self, cpid=None, csNm=None, cpNm=None, addr=None, cpStat=None):
        self.cpid = cpid
        self.csNm = csNm
        self.cpNm = cpNm
        self.addr = addr
        self.cpStat = cpStat

    def __str__(self):
        return f"충전소ID:{self.cpid}\n충전소명:{self.csNm}\n충전기타입:{self.cpNm}\n주소:{self.addr}\n상태:{self.cpStat}"


class StationDao:
    def __init__(self):
        self.url = "http://openapi.kepco.co.kr/service/EvInfoServiceV2/getEvSearchList"
        self.key = "1vpUi9jK%2B%2FJBVqaJ6TDWANcFxIFeuXBQRAljiZth0kzAvawz7gHoAgqwY3hDOFDi0SAcOe5Vz%2BE3ErfXvypDWw%3D%3D"

    def get_root(self, page_no, num_row, area):
        html = requests.get(self.url + '?pageNo=' + str(page_no) + '&numOfRows=' + str(
            num_row) + '&ServiceKey=' + self.key + '&addr=' + area).text
        root = BeautifulSoup(html, 'lxml-xml')
        return root

    def get_total(self, area):
        r = self.get_root(1, 10, area)
        total = r.select('totalCount')[0].string
        return total

    def get_cslist(self, area):
        page = 1
        cs_list = []

        while True:
            r = self.get_root(page, 200, area)
            lis = r.find_all('item')
            if len(lis) == 0:
                break
            for i in lis:
                if i.cpStat.string == '1':
                    row = [i.cpId.string, i.csNm.string, i.cpNm.string, i.addr.string, '충전가능']
                elif i.cpStat.string == '2':
                    row = [i.cpId.string, i.csNm.string, i.cpNm.string, i.addr.string, '충전중']
                elif i.cpStat.string == '3':
                    row = [i.cpId.string, i.csNm.string, i.cpNm.string, i.addr.string, '고장/점검']
                elif i.cpStat.string == '4':
                    row = [i.cpId.string, i.csNm.string, i.cpNm.string, i.addr.string, '통신장애']
                elif i.cpStat.string == '5':
                    row = [i.cpId.string, i.csNm.string, i.cpNm.string, i.addr.string, '통신미연결']
                else:
                    row = [i.cpId.string, i.csNm.string, i.cpNm.string, i.addr.string, '알수없음']
                cs_list.append(row)
            page += 1
        return cs_list

    def make_df(self, area):
        lst = self.get_cslist(area)
        columns = ['ID', '충전소명', '충전기타입', '주소', '상태']
        return pd.DataFrame(lst, columns=columns)

    def draw_status(self, area):
        df = self.make_df(area)
        s = df['상태']
        vc = s.value_counts()
        val = vc.values
        idx = vc.index

        plt.rcParams['font.family'] = 'Malgun Gothic'
        plt.rcParams['axes.unicode_minus'] = False
        plt.bar(idx, val)

        plt.xlabel('충전소 상태')
        plt.ylabel('충전소 수')
        plt.title(f'{area} 지역 충전소 상태 현황')
        return plt.show()


class StationService:
    def __init__(self):
        self.dao = StationDao()

    def print_detail(self):
        area = input('검색할 지역:')
        self.dao.draw_status(area)
        df = self.dao.make_df(area)
        print(df[['ID', '충전소명']])
        cpid = input('상세 내역을 볼 충전소 ID:')
        res = df[df['ID'] == cpid]
        v = StationVo(res.values[0][0], res.values[0][1], res.values[0][2], res.values[0][3], res.values[0][4])
        print(v)

s = StationService()
s.print_detail()
