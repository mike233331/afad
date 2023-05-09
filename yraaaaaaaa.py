from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import relationship, Session

sqlite_database = "sqlite:///mikka.db"
engine = create_engine(sqlite_database)


class Base(DeclarativeBase): pass



class Sock(Base):
    __tablename__ = "socks"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    style = Column(String)
    color = Column(String)
    quantity = Column(String)
    price = Column(Integer)
    updated = Column(String)





Base.metadata.create_all(bind=engine)

with Session(autoflush=False, bind=engine) as db:
    # создаем пользователей
    q1 = Sock(name="miska", style="misha", color="blue", quantity="24", price="2.99", updated="01-23-2016")
    q2 = Sock(name="mika", style="misha", color="bluee", quantity="16", price="7.99", updated="01-11-2020")
    q3 = Sock(name="misa", style="misha", color="blue", quantity="24", price="1.00", updated="01-21-2016")

        # устанавливаем для компаний списки пользователей
    # добавляем компании в базу данных, и вместе с ними добавляются пользователи
    db.add_all([q1, q2, q3])
    db.commit()