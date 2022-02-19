# import psycopg2

# # establishing the connection
# conn = psycopg2.connect(
#     database="postgres",
#     user="postgres",
#     password="postgres",
#     host="localhost",
#     port="5438",
# )
# # Creating a cursor object using the cursor() method
# cursor = conn.cursor()

# # Executing an MYSQL function using the execute() method
# cursor.execute("select version()")

# # Fetch a single row using fetchone() method.
# data = cursor.fetchone()
# print("Connection established to: ", data)

# # Closing the connection
# conn.close()


from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@localhost:5438/emptycabinet"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
