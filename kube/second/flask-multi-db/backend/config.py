class Config:
    # MySQL Configuration
    MYSQL_USER = "root"
    MYSQL_PASSWORD = "password"
    MYSQL_HOST = "mysql"  # ✅ FIXED! Changed from 'mysql_db' → 'mysql'
    MYSQL_DB = "users_db"
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DB}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # PostgreSQL Configuration
    POSTGRES_USER = "postgres"
    POSTGRES_PASSWORD = "password"
    POSTGRES_HOST = "postgres"  # ✅ Correct
    POSTGRES_DB = "users_db"
    POSTGRES_URI = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}/{POSTGRES_DB}"

    # MongoDB Configuration
    MONGO_HOST = "mongo"  # ✅ FIXED! Changed from 'mongo_db' → 'mongo'
    MONGO_PORT = "27017"
    MONGO_DB = "users_db"
    MONGO_URI = f"mongodb://{MONGO_HOST}:{MONGO_PORT}/"

