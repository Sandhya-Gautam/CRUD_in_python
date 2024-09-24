from db.db import DBConn, Database

conn=DBConn("user1", "password123")
result = conn.create_conn()
print(result)

def create_database(name):
	if result:
		return conn.create_database(name)
	else:
		return "connection failed"
	
def update(db, key , value):
	if result:
		db1=Database(db,conn)
		print(db1.update(key,value))
		return "database updated"
	
def read(db):
	if result:
		db1=Database(db,conn)
		print(db1)
		return db1.read()
	else:
		return "connection failed"
	
def delete(db, key):
	if result:
		db1=Database(db,conn)
		db1.delete(key)
		return "key deleted"
	else:
		return "connection failed"

def get_database():
	return conn.get_database()

