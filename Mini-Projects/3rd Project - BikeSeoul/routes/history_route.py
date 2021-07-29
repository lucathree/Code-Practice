from flask import Blueprint, render_template, request, redirect, session
import bikeseoul.models.history as his
import bikeseoul.models.member as mem
import bikeseoul.models.bikedata as bike

bp = Blueprint('history', __name__, url_prefix='/history')
history_service = his.HistoryService()
member_service = mem.MemberService()
bike_service = bike.BikeService()


@bp.route('/')
def write_history():
    if 'id' not in session:
        return redirect('/member/login')
    else:
        id = session['id']
        user = member_service.getMem(id)
        hist = history_service.getHistory(id)

        avg_total_list = bike_service.getAvgTotal()
        avg_age_list = bike_service.getAvgService('age', bike.df.loc[5])
        avg_gender_list = bike_service.getAvgService('gender', bike.df.loc[5])

        try:
            hour = history_service.getTotalHours(id)
            hour_by_min = history_service.getHoursByMin(id)
            favstn = history_service.getFavStn(id)
            carbon = history_service.getTotalCarbon(id)
            workout = history_service.getTotalWorkout(id)
            distance = history_service.getDistance(id)

            count = history_service.getCount(id)

            if user.gender == 'F':
                gender = '여성'
            else:
                gender = '남성'

            distance_rnd = round(distance * 0.001, 2)
            myavg_workout = round(workout / count, 2)
            myavg_carbon = round(carbon / count, 2)
            myavg_distance = round(distance / count, 2)
            myavg_hour = round(hour_by_min / count, 2)
            return render_template('history/list.html', user=user, hist=hist, hour=hour, favstn=favstn, carbon=carbon,
                               workout=workout, avg_total_list=avg_total_list, avg_age_list=avg_age_list,
                               avg_gender_list=avg_gender_list, gender=gender, myavg_hour=myavg_hour,
                               myavg_distance=myavg_distance, myavg_carbon=myavg_carbon, myavg_workout=myavg_workout,
                               count=count, distance=distance_rnd)
        except Exception:
            return render_template('history/list.html', user=user, hist=hist, hour=0, favstn=0, carbon=0,
                                   workout=0, avg_total_list=avg_total_list, avg_age_list=avg_age_list,
                                   avg_gender_list=avg_gender_list, gender=0, myavg_hour=0,
                                   myavg_distance=0, myavg_carbon=0, myavg_workout=0, count=0, distance=0)


@bp.route('/add')
def add_form():
    if 'id' not in session:
        return redirect('/member/login')
    else:
        stlst = history_service.getStationList()
        return render_template('history/add.html', stlst=stlst)


@bp.route('/add', methods=['POST'])
def add_history():
    member_id = session['id']
    rent_date = request.form['rent_date']
    rent_station = request.form['rent_station']
    return_station = request.form['return_station']
    rent_time = request.form['rent_time']
    return_time = request.form['return_time']
    distance = request.form['distance']

    h = his.History(member_id=member_id, rent_date=rent_date, rent_station=rent_station,
                    return_station=return_station, rent_time=rent_time, return_time=return_time, distance=distance)
    history_service.writeHistory(h)
    return redirect('/history')
