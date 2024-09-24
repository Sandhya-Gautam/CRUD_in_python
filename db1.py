import json 
class dbconn:
	def __init__(self, username, password):
		self.username= username
		self.password= password 
		self.dbname= None
		self.conn=None
	
	def create_conn(self):
		with open('record.json', 'r') as json_file:
        		data = json.load(json_file)
		if self.username in data :
           		value = data[self.username]
           		if value==self.password:
           			self.conn= True
           			return "Connection successful"
           		else:
           		return "Invalid"
		else:
           		return "no such username"
           		
		
	def close_conn(self):
		if self.conn:
			self.conn=False
			return
	
	
	def create_database(self):
		if self.conn:
			return database(self)
		else:
			return "connection worng"
			
		
	def get_database(self, name):
        	if self.conn:
            		return f"Accessing database: {name}"
        	else:
            		return "Connection failed. Cannot access database."
            		
class database:
	def __init__(self, connection):
		self.data=None
		self.connection= connection
	
	def is_present (self, db, name):
		with open('r.json', 'r') as json_file:
        		data = json.load(json_file)
		if name+'.json' in data[db]:
			return True
				
	def create_data(self,db, name):
		if not self.connection.conn:
            		print("No active database connection")
            		return
		if not is_present(db, name):
            		with open(name + '.json', 'w') as json_file:
				json.dump({}, json_file, indent=4)
        		with open('r.json', 'r') as json_file:
        			data = json.load(json_file)
        		data[db].append(value)
        		with open('r.json', 'w') as json_file:
				json.dump(data, json_file, indent=4) 	
        		
        	
	def update(self, name, key, value):
		if not self.connection.conn:
            		print("No active database connection")
            		return
            	if not is_present(db, name)
            		print("no such data in database")
            		return
		with open(name + '.json', 'r') as json_file:
        		data = json.load(json_file)
		data.update({key: value})
		with open(name + '.json', 'w') as json_file:
        		json.dump(data, json_file, indent=4)


	def delete(self, name, key):
		if not self.connection.conn:
            		print("No active database connection")
            		return
            	if not is_present(db, name)
            		print("no such data in database")
            		return
		with open(name + '.json', 'r') as json_file:
        		data = json.load(json_file)
		if key in data:
        		del data[key]
		with open(name + '.json', 'w') as json_file:
        		json.dump(data, json_file, indent=4)


	def read(self,name):
		if not is_present(db, name)
            		print("no such data in database")
            		return
		if not self.connection.conn:
            		print("No active database connection")
            		return
		with open(name + '.json', 'r') as json_file:
        		data = json.load(json_file)
		return data	

def create_acc(username, password):
		with open('record.json', 'r') as json_file:
        		data = json.load(json_file)
		data[username]=password
		with open('record.json', 'w') as json_file:
			json.dump(data, json_file, indent=4)
			

		
	
									
create_acc("abc", "123")
conn1=dbconn("abc", "123")
print(conn1.create_conn())
db= conn1.create_database()
db.create_data("aaa")
db.update("aaa","sun","moon")
print(db.read("aaa"))
conn1.close_conn()
create_acc("xyz", "345")
conn2=dbconn("xyz", "345")
print(conn2.create_conn())
db2= conn2.create_database()
print(db2.read("aaa"))

        	
