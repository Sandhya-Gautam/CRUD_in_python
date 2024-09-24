from fastapi import FastAPI
from database.database import create_database, update, read, delete, get_database

app = FastAPI()


@app.post("/create/")
def create_data(item:dict):
	name=item["name"]
	db=create_database(name)
	return {"msg": "database created","database":db }

@app.post("/update/")
def update_item(item:dict):
	db=item["database"]
	key=item["key"]
	value=item["value"]
	msg=update(db,key,value)
	return {"msg": msg }

@app.post("/delete/")
def delete_item(item:dict):
	db=item["database"]
	key=item["key"]
	msg= delete(db, key)
	return {"msg":msg}
    

@app.get("/read/{name}")    
def read_item(name: str):
	data=read(name)
	return data 

@app.get("/get_databases/")    
def read_item():
	data=get_database()
	return data   

