from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os.path
from flask_bootstrap import Bootstrap5
from sqlalchemy.orm import relationship, Session
from sqlalchemy import ForeignKey
import sqlite3

basedir = os.path.abspath(os.path.dirname(__file__))


db = SQLAlchemy()
app = Flask(__name__)
db_name = 'mikka.db'
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, db_name)
con = sqlite3.connect('mikka.db')
cur = con.cursor()


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db.init_app(app)

bootstrap = Bootstrap5(app)


# each table in the database needs a class to be created for it
# this class is named Sock because the database contains info about socks
# and the table in the database is named: socks
# db.Model is required - don't change it
# identify all columns by name and their data type


class Church(db.Model):
    __tablename__ = "church"
    id = db.Column(db.Integer, primary_key=True, index=True)
    name1 = db.Column(db.String)
    city = db.Column(db.String)
    # color = db.Column(db.Integer)
    # description = db.Column(db.String)
    # country_id = db.Column(db.Integer, ForeignKey("country.id"))
    religion_id = db.Column(db.Integer, ForeignKey("religion.id"))
    # date_of_construction = db.Column(db.Integer)


class Religion(db.Model):
    __tablename__ = "religion"
    id = db.Column(db.Integer, primary_key=True, index=True)
    name = db.Column(db.Text)
    # title = db.Column(db.String(100))
    relig = db.relationship('Church', backref='religion')

app.app_context().push()
db.drop_all()
db.create_all()


post1 = Religion(name='Russia')
post2 = Religion(name='Georgia')

comment1 = Church(city='Подгорица', name1='цероквь 1', religion_id=2)
comment2 = Church(city='Будва', name1="церковь 2", religion_id=1)

db.session.add_all([post1, post2])
db.session.add_all([comment1, comment2])
db.session.commit()

price = cur.execute('''
SELECT name1, name 
FROM church 
LEFT JOIN religion
ON church.religion_id = religion.id;
''')
price = cur.fetchall()
print(price)



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
            .order_by(Church.name1)).scalars()
        return render_template('list.html', church=church, city=city)
    except Exception as e:
        # e holds description of the error
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = '<h1>Something is broken.</h1>'
        return hed + error_text


if __name__ == '__main__':
    app.run(debug=True)
    # app.run(host='0.0.0.0', port=4999, debug=True)
