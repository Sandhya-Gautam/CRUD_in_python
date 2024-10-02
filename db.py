import json 
import os
from functools import wraps

def open_database(cls):
    instances={}  

    @wraps(cls)
    def get_instance(*args,**kwargs):
        if not os.path.isfile("databases.json"):
            data={}
            with open("databases.json", 'w') as json_file:
                json.dump(data, json_file, indent=4)  
        else:
            try:
                with open('databases.json', 'r') as json_file:
                    data = json.load(json_file)
            except FileNotFoundError:
                print("file not found")
                return None
            except Exception as e:
                print("An unexpected error occurred: {str(e)}")
                return None
            
        if cls not in instances:
            username = (args[0] if len(args) > 0 else None)
            password = (args[1] if len(args) > 1 else None)
            if username=="localhost" and password=="123":
                instances[cls]=cls(*args,**kwargs,data=data)
                return instances[cls]
            else:
                print("invalid input")
                return None
    return get_instance 

        

@open_database
class DBConn:
    def __init__(self, username, password, data):
        self.username=username
        self.password=password
        self.conn=True
        self.data=data
    
    def set(self, key, value):    
        self.data.update({key: value})
        with open( 'databases.json', 'w') as json_file:
            json.dump(self.data, json_file, indent=4)
        return True   

    def get(self, key):
        return self.data[key]
        
    
    def delete(self, key):
        self.data.delete(key)
        with open( 'databases.json', 'w') as json_file:
            json.dump(self.data, json_file, indent=4)
        return True


    def lpush(self, key, value):
        # import ipdb; ipdb.set_trace()
        if key in  self.data.keys():
            if value not in self.data[key]:
                self.data[key].append(value)
            else:
                print("value already present")
        else :
            self.data[key]=[value]

        with open( 'databases.json', 'w') as json_file:
            json.dump(self.data, json_file, indent=4)
        return True  

    def lpop(self, key, value):
        if value in self.data[key]:
            self.data[key].remove(value)
        with open( 'databases.json', 'w') as json_file:
            json.dump(self.data, json_file, indent=4)
        return True  



        
    
db=DBConn("localhost", "123")
db.set("star", 123)
db.lpush("planet","earth")
db.lpush("planet","jupiter")
db.lpop("planet", "earth")

