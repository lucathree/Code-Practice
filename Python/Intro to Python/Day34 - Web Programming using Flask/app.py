from flask import Flask, render_template
import Routes.member_route as rm
import Routes.board_route as rb

app = Flask(__name__)
app.secret_key = 'affdasdf'

#생성한 블루프린트 등록
app.register_blueprint(rm.bp)
app.register_blueprint(rb.bp)

@app.route('/')
def root():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()#flask 서버 실행