# from qwsa import db, Church, Religion
#
# db.drop_all()
# db.create_all()
#
# post1 = Religion(name='Россия')
# post2 = Religion(name='Франция')
# post3 = Religion(name='Белгия')
#
# comment1 = Church(city='Россия', name="церковь пресвятого михайло", religion_id=1)
# comment2 = Church(city='Бельгия', name="церковь святых носков", religion_id=3)
# comment3 = Church(city='Белгия', name="церковь святых турников", religion_id=3)
# comment4 = Church(city='Франция', name="храм наисвещенных брусьев", religion_id=2)
#
#
# db.session.add_all([post1, post2, post3])
# db.session.add_all([comment1, comment2, comment3, comment4])
#
#
# db.session.commit()