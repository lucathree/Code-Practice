import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# 폰트 한글로 설정
plt.rcParams['font.family'] = 'Malgun Gothic'


df = pd.read_csv('static/data/bikedata_merge.csv',
                 header=0, encoding='utf8')
# 대여소 데이터 불러오기


# 연령대
age_list = df['age'].unique().tolist()
gender_list = df['gender'].unique().tolist()

# 단순 평균 구하기 함수


def get_mean_by(user_info, target, column):
    mean_target = df.groupby(target)[column].mean()
    return mean_target


# 평균 함수=> (데이터프레임,원하는 카테고리 별,특정컬럼) 내림차순
def getMeanByTarget(dataframe, target, column):
    mean_target = dataframe.groupby(
        target)[column].mean().sort_values(ascending=False)
    return mean_target

# 평균 groupby 데이터 받아서 그래프로 출력하는 함수
# x


def getGraph(mean_data, x, y):

    graph_bar = mean_data.plot.bar()

    graph_bar.set_xlabel(x)
    graph_bar.set_ylabel(y)
    graph_bar.set_title('%s 별 %s' % (x, y))
    plt.show()


def getPlot(mean_data, x, y):

    plt.figure(figsize=(12, 6))
    plt.plot(mean_data)
    plt.xlabel(x)
    plt.ylabel(y)
    plt.title('%s 별 %s' % (x, y))
    plt.show()


# 여러개 그래프 한꺼번에
def mean_graph_list():
    target_list = ['amount', 'carbon', 'distance', 'use_time']
    name_list = ['평균 운동량', '평균 탄소감축량', '평균 이동거리', '평균 사용 시간']
    for i in range(len(target_list)):
        plt.subplot(2, 2, i+1)
        getGraph(getMeanByTarget(
            df, 'age', target_list[i]), x='연령대', y=name_list[i])


# 요일 컬럼에 순서를 준다  reindex() 사용
weekday_index = ['Monday', 'Tuesday', 'Wednesday',
                 'Thursday', 'Friday', 'Saturday', 'Sunday']


def getCountByTarget(dataframe, target, column):

    count_val = dataframe.groupby(target)[column].count()
    return count_val


def getSumByTarget(dataframe, target, column):

    sum_val = dataframe.groupby(target)[column].sum()
    return sum_val

# 대여일별 대여건수 그래프 (요일별로)


def plot_count_weekday():
    getPlot(getSumByTarget(df, 'weekday', 'count').reindex(
        weekday_index), x='요일별', y='사용건수')


age_index = ['~10대', '20대', '30대', '40대', '50대', '60대', '70대~']

# 요일별 평균 운동량 그래프


def plot_mean_amount_weekday():
    # 요일별 평균 운동량
    mean_amount_week = getMeanByTarget(
        df, 'weekday', 'amount').reindex(weekday_index)
    getPlot(mean_amount_week, '요일', '평균 운동량')

# 요일별 평균 사용시간 함수 + 그래프


def plot_mean_time_week():
    # 요일 별 평균 사용시간
    mean_time_week = getMeanByTarget(
        df, 'weekday', 'use_time').reindex(weekday_index)
    # 요일 별 평균 사용시간 그래프
    getPlot(mean_time_week, x='요일', y='평균 사용시간')

# 시간대별 평균 대여수


def plot_mean_count_hour():
    # 평균 대여수 : 시간대별 이용건수 / 1월달 일자
    mean_count_time = getSumByTarget(
        df, 'rent_hour', 'count')/len(df['date'].unique())
    # 평균 대여수 그래프
    getPlot(mean_count_time, '시간대', '평균 대여건수')


# 자치구별 총 이용자 함수 + 그래프
def graph_total_user():
    # 1달 자치구 별 총 이용자
    count_region = getCountByTarget(
        df, 'region', 'count').sort_values(ascending=False)
    getGraph(count_region, '자치구', '총 이용자 수')


# target 에는 연령별, 시간대별, 요일별 등등
# my_info 에는 데이터프레임 한줄, 즉 특정유저데이터 프레임 한줄
# x에는 주석을 달아주는거니까 target에 해당하는걸 한글로 age 라면 연령대
# y에는 column에 해당하는걸 한글로 amount 라면 운동량


def compare_amount_age(my_info):
    mean_data = df.groupby('age')['amount'].mean()

    img_path = 'static/graph/비교 1'

    plt.figure(figsize=(10, 5))
    mean_data.plot.bar()
    plt.xlabel('연령별')
    plt.ylabel('평균운동량')
    plt.title('연령별 평균 운동량과 내 운동량 비교')
    plt.axhline(my_info['amount'], linewidth=2,
                color='red', label='내 운동량')
    plt.axhline(df[df['age'] == my_info['age']]['amount'].mean(
    ), color='green', label='나와 비슷한 연령대 운동량')
    plt.legend()
    plt.savefig(img_path)
    plt.close()


# def compare_graph(target, my_info, x, img_path_list):
#     df = pd.read_csv('models/bikedata_merge.csv', encoding='utf8')
#     column_list = ['amount', 'carbon', 'distance', 'use_time']
#     y = ['운동량', '탄소감축량', '이동거리', '사용시간']
#     for i in range(len(column_list)):
#         mean_data = getMeanByTarget(df, target, column_list[i])

# #       fig, ax = plt.subplots(1,len(my_info),i+1,figsize=(15,6))
#         plt.figure(figsize=(15, 6))
#         plt.subplot(2, 2, i+1)

#         mean_data.plot.bar()
#         plt.xlabel(x)
#         plt.ylabel(y[i])
#         plt.title('%s 별 평균 %s' % (x, y[i]))
#         plt.axhline(my_info[column_list[i]], linewidth=2,
#                     color='red', label='내 {}'.format(y[i]))
#         plt.axhline(df[df[target] == my_info[target]][column_list[i]].mean(
#         ), color='green', label='나와 비슷한 {} {}'.format(x, y[i]))
#         plt.legend()
#         plt.savefig(img_path_list[i])
#         plt.close()


# 성별별 연령별 평균 데이터 컬러로
def graph_list_by_type():
    target_list = ['amount', 'carbon', 'distance', 'use_time']
    name_list = ['평균 운동량', '평균 탄소감축량', '평균 이동거리', '평균 사용 시간']
    for i in range(len(target_list)):
        #       fig,axes=plt.subplots(1,4)
        plt.subplots(figsize=(15, 6))
        ax = sns.barplot(data=df, x='gender', y=target_list[i], hue='age')
        ax.set(xlabel='성별', ylabel=name_list[i],
               title='성별별 연령별 %s' % (name_list[i]))
        plt.show()

# 요일별 연령별 사용건수


def graph_count_day_age():
    plt.figure(figsize=(15, 6))
    ax = sns.barplot(data=df, x='weekday', y='count', hue='age', estimator=sum)
    ax.set(xlabel='요일별', ylabel='사용건수', title='요일별 연령별 평균 사용건수')
    plt.show()


def graph_count_day_gender():
    plt.figure(figsize=(15, 6))
    ax = sns.barplot(data=df, x='weekday', y='count',
                     hue='gender', estimator=sum)
    ax.set(xlabel='요일별', ylabel='사용건수', title='요일별 성별별 평균 사용건수')
    plt.savefig('요일별 성별별 평균 사용건수')


class Bike:
    def __init__(self, date=None, rent_hour=None, st_id=None, st_name=None,
                 gender=None, age=None, count=None, amount=None, carbon=None,
                 distance=None, use_time=None, weekday=None, region=None,
                 latitude=None, longitude=None):
        self.date = date
        self.rent_hour = rent_hour
        self.st_id = st_id
        self.st_name = st_name
        self.gender = gender
        self.age = age
        self.count = count
        self.amount = amount
        self.carbon = carbon
        self.distance = distance
        self.use_time = use_time
        self.weekday = weekday
        self.region = region
        self.latitude = latitude
        self.longitude = longitude

    def __str__(self):
        res = ''
        res += 'date' + self.date
        res += 'rent_hour' + self.rent_hour
        res += 'st_id' + self.st_id
        res += 'st_name' + self.st_name
        res += 'gender' + self.gender
        res += 'age ' + self.age
        res += 'count ' + self.count
        res += 'amount ' + self.amount
        res += 'carbon ' + self.carbon
        res += 'distance ' + self.distance
        res += 'use_time ' + self.use_time
        res += 'weekday ' + self.weekday
        res += 'region ' + self.region
        res += 'latitude ' + self.latitude
        res += 'longitude ' + self.longitude

        return res


class BikeDao:
    def __init__(self,):
        self.conn = None


class BikeService:

    def __init__(self):
        self.df = df

    # 이용자 전체 평균 데이터 보기
    # 운동량,탄소감축량,이동거리,사용시간
    def compare_amount_age_service(self, my_info):
        compare_amount_age(my_info)

    def getAvgService(self, target, my_info):
        column_list = [
            'amount', 'carbon', 'distance', 'use_time']

        avg_target_list = []

        for column in column_list:
            mean_target = df.groupby(
                target)[column].mean().round(2)[my_info[target]]
            avg_target_list.append(mean_target)
        return avg_target_list

    def getAvgTotal(self):
        column_list = [
            'amount', 'carbon', 'distance', 'use_time']
        avg_list = []
        for col in column_list:
            mean_col = round(df[col].mean(), 2)
            avg_list.append(mean_col)
        return avg_list

    # user_info 파라메터로 넣어줘야됨
    # my_data 객체로 불러와서
    # 밑에 넣어다 주면 됨

    def getMyValList(self):
        my_val_list = df.loc[5][9:13]
        return my_val_list
