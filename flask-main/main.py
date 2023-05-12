""" read from a SQLite database and return data """

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os.path
from flask_bootstrap import Bootstrap5
from sqlalchemy.orm import relationship, Session
from sqlalchemy import ForeignKey



# this variable, db, will be used for all SQLAlchemy commands
db = SQLAlchemy()
# create the app
app = Flask(__name__)
# change string to the name of your database; add path if necessary
db_name = 'mikka.db'
# note - path is necessary for a SQLite db!!!
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, db_name)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# initialize the app with Flask-SQLAlchemy
db.init_app(app)


# Bootstrap-Flask requires this line
bootstrap = Bootstrap5(app)


# each table in the database needs a class to be created for it
# this class is named Sock because the database contains info about socks
# and the table in the database is named: socks
# db.Model is required - don't change it
# identify all columns by name and their data type


class Church(db.Model):
    __tablename__ = "church"
    id = db.Column(db.Integer, primary_key=True, index=True)
    name = db.Column(db.String)
    city = db.Column(db.String)
    color = db.Column(db.Integer)
    # description = db.Column(db.String)
    # country_id = db.Column(db.Integer, ForeignKey("country.id"))
    # religion_id = db.Column(db.Integer, ForeignKey("religion.id"))
    date_of_construction = db.Column(db.Integer)
    # country = relationship("Country", back_populates="users")
    # relig = relationship("religion", back_populates="user")

# class Sock(db.Model):
#     __tablename__ = 'socks'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String)
#     style = db.Column(db.String)
#     color = db.Column(db.String)
#     quantity = db.Column(db.Integer)
#     price = db.Column(db.Float)
#     updated = db.Column(db.String)

#routes

@app.route('/')
def index():
    # get a list of unique values in the style column
    cityes = db.session.execute(db.select(Church)
        .with_only_columns(Church.city).distinct())
    return render_template('index.html', cityes=cityes)


@app.route('/inventory/<city>')
def inventory(city):
    try:
        church = db.session.execute(db.select(Church)
            .filter_by(city=city)
            .order_by(Church.name)).scalars()
        return render_template('list.html', church=church, city=city)
    except Exception as e:
        # e holds description of the error
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = '<h1>Something is broken.</h1>'
        return hed + error_text


if __name__ == '__main__':
    app.run(debug=True)
    # app.run(host='0.0.0.0', port=4999, debug=True)