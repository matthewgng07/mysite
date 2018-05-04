
# A very simple Flask Hello World app for you to get started with...

from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
import constants

app = Flask(__name__)
app.config.from_object('config.BaseConfig')
db = SQLAlchemy(app)

'''
@app.route('/')
def hello_world():
    return ''
'''


'''
@app.route('/about_me')
def about_me():
    return app.send_static_file('about_matthew.html')
'''



@app.route('/about_me')
def about_me():
    return render_template('about_matthew.html',
                           courses=constants.COURSES)




'''
@app.route('/class_schedule')
def class_schedule():
    return app.send_static_file('class_schedule.html')
'''
@app.route('/class_schedule')
def class_schedule():
    return render_template('class_schedule.html',
                           courses=constants.COURSES)


'''
@app.route('/register')
def register():
    return app.send_static_file('register.html')
'''

@app.route('/register')
def register():
    return render_template('register.html',
                           courses=constants.COURSES)


@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/top_ten_songs')
def top_ten_songs():
    return render_template('top_ten_songs.html', songs=constants.TOP_TEN_SONGS)


