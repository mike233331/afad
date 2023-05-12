import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
# from sqlalchemy.orm import DeclarativeBase
# from sqlalchemy.orm import relationship, Session




basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
           'sqlite:///' + os.path.join(basedir, 'dadada.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.app_context().push()


db = SQLAlchemy(app)



class Church(db.Model):
    __tablename__ = "church"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    city = db.Column(db.Text)
    # coordinates = db.Column(db.Text)
    # description = db.Column(db.String)
    # country_id
    # religion_id
    # date_of_construction = db.Column(db.Integer)
    # country = relationship("Country", back_populates="users")
    religion_id = db.Column(db.Integer, db.ForeignKey('religion.id'))

    # def __repr__(self):
    #     return f'<Church "{self.city}">'



class Religion(db.Model):
    __tablename__ = "religion"
    id = db.Column(db.Integer, primary_key=True, index=True)
    name = db.Column(db.Text)
    # title = db.Column(db.String(100))
    relig = db.relationship('Church', backref='religion')

    # def __repr__(self):
    #     return f'<Religion "{self.name[:20]}...">'


db.drop_all()
db.create_all()

post1 = Religion(name='Россия')
post2 = Religion(name='Франция')
post3 = Religion(name='Белгия')

comment1 = Church(city='Россия', name="церковь пресвятого михайло", religion_id=1)
comment2 = Church(city='Бельгия', name="церковь святых носков", religion_id=3)
comment3 = Church(city='Белгия', name="церковь святых турников", religion_id=3)
comment4 = Church(city='Франция', name="храм наисвещенных брусьев", religion_id=2)


db.session.add_all([post1, post2, post3])
db.session.add_all([comment1, comment2, comment3, comment4])


db.session.commit()
