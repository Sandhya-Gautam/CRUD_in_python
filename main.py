from fastapi import FastAPI
import database.py as ds

app = FastAPI()


@app.post("/create/")
def create_item(item:dict):
	name=item["name"]
	ds.create(name)
	return {"msg": "database created" }

@app.post("/update/")
def update_item(item:dict):
	name=item["name"]
	key=item["key"]
	value=item["value"]
	ds.create(name,key,value)
	return {"msg": "database updated" }

@app.post("/delete/")
def delete_item(item:dict):
	name=item["name"]
	ds.create(name)
	return {"msg": "database created" }
    

@app.get("/read/")    
def read_item(items:dict):
	data=ds.read(items["name"])
	return data 
    

