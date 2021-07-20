from dotenv import load_dotenv
import os

load_dotenv()

HOST_MONGO = os.getenv("HOST_MONGO")
USER_MONGO = os.getenv("USER_MONGO")
PASSWORD_MONGO = os.getenv("PASSWORD_MONGO")
SERVER_MONGO = os.getenv("SERVER_MONGO")
DATABASE_MONGO = os.getenv("DATABASE_MONGO")
