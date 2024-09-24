import json

class DBConn:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.conn = None
        self.databases = [] 
    
    def create_conn(self):
        with open('users.json', 'r') as json_file:
            data = json.load(json_file)
        
        if self.username in data.keys():
            value = data[self.username]
            if value == self.password:
                
                self.conn = True
                with open('database.json', 'r') as json_file:
                    data = json.load(json_file)
                if not self.username in data.keys():
                    data.update({self.username:value})
                    with open('database.json', 'w') as json_file:
                        json.dump(data, json_file, indent=4)
                    self.databases=[]
                else:
                    self.databases=data[self.username]
                return "Connection successful"
            else:
                return "Invalid password"
        else:
            return "No such username"
    
    def close_conn(self):
        if self.conn:
            self.conn = False
            self.update_relationalDatabase()
            return "Connection closed"
        else:
            return "No active connection to close"
    
    def is_present(self, name):
        with open('database.json', 'r') as json_file:
            data = json.load(json_file)
        if name in data[self.username]:
            return True
        else:
            return False
      
    def update_relationalDatabase(self):
        with open('database.json', 'r') as json_file:
            data = json.load(json_file)
        data.update({self.username:self.databases})
        with open('database.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)
            
                        
    def create_database(self, name):
        if self.conn:
            self.update_relationalDatabase()
            if not name in self.databases:
                with open(name + '.json', 'w') as json_file:
                    json.dump({}, json_file, indent=4)
                self.databases.append(name)
                self.update_relationalDatabase()
                return Database(name, self)
            else:
                return f"Database '{name}' already exists"
        else:
            return "No active connection. Cannot create database."
    
    def get_database(self):
        if self.conn:
            return self.databases
        else:
            return "Connection failed. Cannot access database."


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
        return "database updated"

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
        return "key '{key}' deleted"
        
        	
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

def create_acc(username, password):
    with open('users.json', 'r') as json_file:
        data = json.load(json_file)
    data[username]=password
    with open('users.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)








