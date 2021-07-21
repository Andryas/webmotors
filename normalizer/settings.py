from dotenv import load_dotenv
import os

load_dotenv()

HOST_MONGO = os.getenv("HOST_MONGO")
USER_MONGO = os.getenv("USER_MONGO")
PASSWORD_MONGO = os.getenv("PASSWORD_MONGO")
SERVER_MONGO = os.getenv("SERVER_MONGO")
DATABASE_MONGO = os.getenv("DATABASE_MONGO")

HOST_MSQL = os.getenv("HOST_MYSQL")
USER_MYSQL = os.getenv("USER_MYSQL")
PASSWORD_MYSQL = os.getenv("PASSWORD_MYSQL")
SERVER_MYSQL = os.getenv("SERVER_MYSQL")
DATABASE_MYSQL = os.getenv("DATABASE_MYSQL")