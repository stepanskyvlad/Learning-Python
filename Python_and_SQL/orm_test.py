import sqlalchemy
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

print(sqlalchemy.__version__)

engine = sqlalchemy.create_engine('postgresql+psycopg2://postgres:yourpassword#@localhost:5432/testdb')

connection = engine.connect()

result = connection.execute("SELECT * FROM book")
for row in result:
    print('title', row['title'])

result.close()

trans = connection.begin()
try:
    connection.execute("INSERT INTO book(book_id, title, isbn, publisher_id, weight) VALUES (35, 'worst book', 12345, 2, 10)")
    trans.commit()
except:
    trans.rollback()
    raise

with connection.begin() as trans:
    connection.execute("INSERT INTO book(book_id, title, isbn, publisher_id, weight) VALUES (65, 'best book', 12345, 1, 10)")

result = connection.execute("SELECT * FROM book")
for row in result:
    print('title', row['title'])

Base = declarative_base()


class Author(Base):
    __tablename__ = 'author'

    author_id = Column(Integer, promary_key=True)
    full_name = Column(String)
    rating = Column(Float)


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

session = Session()

author = Author(author_id=18, full_name='Dan Brown', rating=4.7)
session.add(author)

session.commit()

print()
for item in session.query(Author).order_by(Author.rating):
    print(item.full_name, ' ', item.rating)

print()

for item in session.query(Author).filter(Author.rating > 4.5):
    print(item.full_name, ' ', item.rating)
