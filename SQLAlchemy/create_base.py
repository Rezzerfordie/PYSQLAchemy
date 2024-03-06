import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# Устанавливаем соединение с postgres
connection = psycopg2.connect(user="postgres", password="1234")
connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

cursor = connection.cursor()
sql_create_database = cursor.execute('create database itmentorsqla')
# Закрываем соединение
cursor.close()
connection.close()

