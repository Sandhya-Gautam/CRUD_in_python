from db.db import DBConn, Database

conn=DBConn("user1", "password123")
result = conn.create_conn()
print(result)

def create_database(name):
	try:
		if result:
			return conn.create_database(name)
		else:
			raise ConnectionError("No established connection")
	except ValueError as e:
		return "An unexpected error occurred: {e}"
	except ConnectionError as e:
		return "An unexpected error occurred: {e}"

	
def update(db, key , value):
	try:
		if result:
			db1=Database(db,conn)
			return db1.update(key,value)
		else:
			raise ConnectionError("No established connection")
	except ValueError as e:
		return "An unexpected error occurred: {e}"
	except ConnectionError as e:
		return "An unexpected error occurred: {e}"

def read(db):
	try:
		if result:
			db1=Database(db,conn)
			print(db1)
			return db1.read()
		else:
			raise ConnectionError("No established connection")
	except ValueError as e:
		return "An unexpected error occurred: {e}"
	except ConnectionError as e:
		return "An unexpected error occurred: {e}"

	
def delete(db, key):
	try:
		if result:
			db1=Database(db,conn)
			db1.delete(key)
			return "key deleted"
		else:
			raise ConnectionError("No established connection")
	except ValueError as e:
		return "An unexpected error occurred: {e}"
	except ConnectionError as e:
		return "An unexpected error occurred: {e}"


def get_database():
	return conn.get_database()

