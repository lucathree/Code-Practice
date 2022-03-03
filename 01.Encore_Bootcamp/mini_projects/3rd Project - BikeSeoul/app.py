from flask import Flask, render_template
import routes.member_route as rm
import routes.board_route as rb
import routes.bikedata_route as rbike
import routes.history_route as rhis
#import routes.myData_route as rmd

app = Flask(__name__)
app.secret_key = 'odifshks'


app.register_blueprint(rm.bp)
app.register_blueprint(rb.bp)
app.register_blueprint(rbike.bp)
app.register_blueprint(rhis.bp)
#app.register_blueprint(rmd.bp)


@app.route('/')
def root():
    return render_template('index.html')

'''
@app.route('/map')
def map():
    return render_template('map.html')
'''

if __name__ == '__main__':
    app.run()