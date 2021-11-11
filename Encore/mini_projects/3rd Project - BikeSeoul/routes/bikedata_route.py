from models import bikedata as bike
from flask import Blueprint, render_template, request, redirect, session

bike_service = bike.BikeService()
bp = Blueprint('bikedata', __name__, url_prefix='/bikedata')
df = bike.df


@bp.route('/')
def home():
    return render_template('/bikedata/button.html')


@bp.route('/graph/mean_by_age')
def GraphMeanByAge():
    img_path1 = '/static/graph/연령대 별 평균 사용 시간.png'
    img_path2 = '/static/graph/연령대 별 평균 운동량.png'
    img_path3 = '/static/graph/연령대 별 평균 탄소감축량.png'
    img_path4 = '/static/graph/연령대 별 평균 이동거리.png'

    return render_template('/bikedata/meanByAge.html', img_path1=img_path1,
                           img_path2=img_path2, img_path3=img_path3,
                           img_path4=img_path4)


@bp.route('/graph/mean_by_day')
def GraphMeanByDay():
    img_path1 = '/static/graph/요일별 별 사용건수.png'
    img_path2 = '/static/graph/요일 별 평균 운동량.png'
    img_path3 = '/static/graph/요일 별 평균 사용시간.png'
    img_path4 = '/static/graph/요일별 연령별 평균 사용건수.png'
    img_path5 = '/static/graph/요일별 성별별 평균 사용건수.png'

    return render_template('bikedata/meanByDay.html', img_path1=img_path1,
                           img_path2=img_path2, img_path3=img_path3,
                           img_path4=img_path4, img_path5=img_path5)


@bp.route('/graph/mean_by_hour')
def GraphMeanByHour():
    img_path1 = '/static/graph/시간대 별 평균 대여건수.png'
    img_path2 = '/static/graph/시간대 별 평균 사용시간.png'

    return render_template('bikedata/meanByHour.html', img_path1=img_path1,
                           img_path2=img_path2)


@bp.route('/graph/region')
def graphRegion():
    # img_path1 = '/static/graph/자치구 별 총 이용자 수.png'
    img_path1 = '/static/graph/자치구 별 총 이용자 수 11.png'
    img_path2 = '/static/graph/자치구 별 탄소감축량.png'
    return render_template('bikedata/region.html', img_path1=img_path1,
                           img_path2=img_path2)


@bp.route('/upload', methods=['POST'])
def upload():
    upload_path = 'static/img/'
