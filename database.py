from db.db import DBConn, Database
from functools import wraps


def check_connection(cls):
	conn=DBConn(cls.username, cls.password)
	if conn:
		return cls
	else: 
		return False


@check_connection
class DatabaseManager:
	def __init__(self, username, password):
		self.username=username
		self.password=password

	def update(self,db, key , value):
			db1=Database(db,self.conn)
			return db1.update(key,value)
	
	def read(self, db):
		db1=Database(db,self.conn)
		print(db1)
		return db1.read()
	
	def delete(self,db, key):
		db1=Database(db,self.conn)
		db1.delete(key)
		return True
		