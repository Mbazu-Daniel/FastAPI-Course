from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config import settings


SQLACHEMY_DATABASE_URL = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"

engine = create_engine(SQLACHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# get the database
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


""" ø

Connecting to a database

"""
# while True:
# try:
#     conn = psycopg2.connect(
#         host="localhost",
#         database="fastapi",
#         user="postgres",
#         password="qwertyuiop",
#         cursor_factory=RealDictCursor,
#     )

#     cursor = conn.cursor()
#     print("database connection was successful")
#     break
# except Exception as error:
#     print("Connection to database failed")
#     print("Error: ", error)
#     time.sleep(2)
