import json

class DBConn:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.dbname = None
        self.conn = None
        self.databases = {}  
    
    def create_conn(self):
        with open('users.json', 'r') as json_file:
            data = json.load(json_file)
        if self.username in data.keys():
            value = data[self.username]
            if value == self.password:
                self.conn = True
                return "Connection successful"
            else:
                return "Invalid password"
        else:
            return "No such username"
    
    def close_conn(self):
        if self.conn:
            self.conn = False
            return "Connection closed"
        else:
            return "No active connection to close"
    
    def create_database(self, name):
        if self.conn:
            if name not in self.databases:
                self.databases[name] = Database(name, self)
                with open(name + '.json', 'w') as json_file:
                    json.dump({}, json_file, indent=4)
                return self.databases[name]
            else:
                return f"Database '{name}' already exists"
        else:
            return "No active connection. Cannot create database."
    
    def get_database(self, name):
        if self.conn:
            if name in self.databases:
                return self.databases[name]
            else:
                return f"Database '{name}' not found"
        else:
            return "Connection failed. Cannot access database."
    
    def get_databases(self):
    	for i in self.databases:
    		print(i)

class Database:
    def __init__(self, name, connection):
        self.name = name
        self.data = {}
        self.connection = connection
        
    def update(self, key, value):
        if not self.connection.conn:
            print("No active database connection")
            return
        if self.name not in self.connection.databases:
            print("No such database in connection")
            return
        with open(self.name + '.json', 'r') as json_file:
            data = json.load(json_file)
        data.update({key: value})
        with open(self.name + '.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)

    def delete(self, key):
        if not self.connection.conn:
            print("No active database connection")
            return
        if self.name not in self.connection.databases:
            print("No such database in connection")
            return
        with open(self.name + '.json', 'r') as json_file:
            data = json.load(json_file)
        if key in data:
            del data[key]
        with open(self.name + '.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)

    def read(self):
        if not self.connection.conn:
            print("No active database connection")
            return
        if self.name not in self.connection.databases:
            print("No such database in connection")
            return
        with open(self.name + '.json', 'r') as json_file:
            data = json.load(json_file)
        return data

conn=DBConn("abc", "123")
conn.create_conn()
db=conn.create_database("xyz")

print(db.read())

conn1=DBConn("user1", "password")
db1=conn.create_database("xyy")
db1.update("light","moon")
print(db1.read())
