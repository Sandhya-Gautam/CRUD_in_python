import json

class DBConn:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.conn = None
        self.databases = [] 
    # to create the connection for authentication
    def create_conn(self):
        #opening the validated user database file 
        try:
            with open('users.json', 'r') as json_file:
                data = json.load(json_file)
        except FileNotFoundError:
            return "user detail file not found"
        except Exception as e:
            return "An unexpected error occurred: {str(e)}"
        
        #checking if the provided username is present or not    
        if self.username in data.keys():
            value = data[self.username]
            #checking if the password matches or not 
            if value == self.password:
                self.conn = True
                try:
                    #opening the user and associated database record file 
                    with open('database.json', 'r') as json_file:
                        data = json.load(json_file)
                except FileNotFoundError:
                    return "user-database file not found"
                except Exception as e:
                    return "An unexpected error occurred: {str(e)}"
                #checking if username is present in user and associated database record file 
                if not self.username in data.keys():
                    data.update({self.username:value})
                    #writing if username isnot present 
                    with open('database.json', 'w') as json_file:
                        json.dump(data, json_file, indent=4)
                    self.databases=[]
                else:
                    self.databases=data[self.username]
                return "Connection successful"
            else:
                raise ValueError("Invalid input")
        else:
            raise ValueError("Invalid input")
    
    def close_conn(self):
        if self.conn:
            self.conn = False
            self.update_relationalDatabase()
            return "Connection closed"
        else:
            return "No active connection to close"
    
    def is_present(self, name):
        try:
            with open('database.json', 'r') as json_file:
                data = json.load(json_file)
        except FileNotFoundError:
            return "user-database file not found"
        except Exception as e:
            return "An unexpected error occurred: {str(e)}"
        
        if name in data[self.username]:
            return True
        else:
            return False
      
    def update_relationalDatabase(self):
        try:
            with open('database.json', 'r') as json_file:
                data = json.load(json_file)
        except FileNotFoundError:
            return "user-database file not found"
        except Exception as e:
            return "An unexpected error occurred: {str(e)}"
        
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
                raise ValueError( f"Database '{name}' already exists")
        else:
            raise ConnectionError("No active connection. Cannot create database.")
    
    def get_database(self):
        if self.conn:
            return self.databases
        else:
            raise ConnectionError("Connection failed. Cannot access database.")


class Database:
    def __init__(self, name, connection):
        self.name = name
        self.data = {}
        self.connection = connection
        
    def update(self, key, value):
        if not self.connection.conn:
            raise ConnectionError("No active database connection")
        if self.name not in self.connection.databases:
            raise ValueError("No such database in connection")
            
        try:
            with open(self.name+'.json', 'r') as json_file:
                data = json.load(json_file)
        except FileNotFoundError:
            return "file not found"
        except Exception as e:
            return "An unexpected error occurred: {str(e)}"
        
        data.update({key: value})
        with open(self.name + '.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)
        return "database updated"

    def delete(self, key):
        if not self.connection.conn:
            raise ConnectionError("No active database connection")
        if self.name not in self.connection.databases:
            raise ValueError("No such database in connection")
        try:
            with open(self.name+'.json', 'r') as json_file:
                data = json.load(json_file)
        except FileNotFoundError:
            return "file not found"
        except Exception as e:
            return "An unexpected error occurred: {str(e)}"
        with open(self.name + '.json', 'r') as json_file:
            data = json.load(json_file)
        if key in data:
            del data[key]
        with open(self.name + '.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)
        return "key '{key}' deleted"
        
        	
    def read(self):
        if not self.connection.conn:
            raise ConnectionError("No active database connection")
        if self.name not in self.connection.databases:
            raise ValueError("No such database in connection")
        try:
            with open('database.json', 'r') as json_file:
                data = json.load(json_file)
        except FileNotFoundError:
            return "file not found"
        except Exception as e:
            return "An unexpected error occurred: {str(e)}"
        
        with open(self.name + '.json', 'r') as json_file:
            data = json.load(json_file)
        return data

def create_acc(username, password):
    try:
        with open('users.json', 'r') as json_file:
            data = json.load(json_file)
    except FileNotFoundError:
        return "user-database file not found"
    except Exception as e:
        return "An unexpected error occurred: {str(e)}"
    data[username]=password
    with open('users.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)








