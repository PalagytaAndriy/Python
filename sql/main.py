from getpass import getpass
from mysql.connector import connect, Error

from sql_scripts import CREATE_TABLE_MOVIE, CREATE_TABLE_REVIEWER, CREATE_TABLE_RATING

try:
	with connect(
		host='localhost',
		user='root',
		password='Aa11!!az',
		database='p22'
	) as conn:
		with conn.cursor() as cur:
			cur.execute(CREATE_TABLE_MOVIE)
			cur.execute(CREATE_TABLE_REVIEWER)
			cur.execute(CREATE_TABLE_RATING)
			conn.commit()
			# for db in cur:
			# 	print(db)
except Error as e:
	print(e)