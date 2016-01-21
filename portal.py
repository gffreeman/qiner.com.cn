from flask import Flask, render_template
from flask import redirect
from flask_moment import Moment
from flask.ext.bootstrap import Bootstrap
from datetime import datetime


app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)


@app.route('/')
def index():
    return render_template('index.html', current_time=datetime.utcnow())
    # return redirect('http://www.example.com')
    # return '<h1>Bad Request</h1>', 400


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


print(app.url_map)


if __name__ == '__main__':
    app.run(debug=True)
