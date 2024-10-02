from fastapi import FastAPI, HTTPException 
from database.database import create_database, update, read, delete, get_database
app = FastAPI()


@app.post("/create/")
def create_data(item:dict):
	name=item["name"]
	if not name : 
		raise HTTPException(status_code=400, detail="name of database is required")
	try:
		db = create_database(name)
		return {"msg": db}
	except Exception as e:
		raise HTTPException(status_code=500, detail=str(e))
		

@app.post("/update/")
def update_item(item:dict):
	name=item["name"]
	key=item["key"]
	value=item["value"]
	if not name and not key and  not value : 
		raise HTTPException(status_code=400, detail="name, key and value  of database is required")
	try:
		msg=update(name,key,value)
		return {"msg": msg }
	except Exception as e:
		raise HTTPException(statue_code=500, detail=str(e))
	
@app.post("/delete/")
def delete_item(item:dict):
	name=item["database"]
	key=item["key"]
	if not name and not key: 
		raise HTTPException(status_code=400, detail="name, key and of database is required")
	try:
		msg= delete(name, key)
		return {"msg":msg}
	except Exception as e:
		raise HTTPException(statue_code=500, detail=str(e))

@app.get("/read/{name}")    
def read_item(name: str):
	if not name:
		raise HTTPException(status_code=400, detail="name of database is required")
	try:
		data=read(name)
		return data 
	except Exception as e:
		raise HTTPException(statue_code=500, detail=str(e))

@app.get("/get_databases/")    
def read_item():
	try:
		data=get_database()
		return data 
	except Exception as e:
		raise HTTPException(statue_code=500, detail=str(e))

