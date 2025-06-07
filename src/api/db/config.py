from decouple import config as decouple_config

DATABSE_URL = decouple_config("DATABASE_URL", default="")


