from fastapi import FastAPI, HTTPException 


app = FastAPI

@app.post("/set/")
def set_item(item:dict):
	name=item["name"]
	key=item["key"]
	value=item["value"]
	if not name and not key and  not value : 
		raise HTTPException(status_code=400, detail="name, key and value  of database is required")
	try:
		msg=set(name,key,value)
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

@app.get("/get/")
def get_item(item:dict):
	key=item["key"]
	delete(key)

	