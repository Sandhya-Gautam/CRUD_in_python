import redis

redis_client= redis.Redis(host="localhost", port= 6379,db=0)

redis_client.set("name", "John")
redis_client.set("Age", '15')
redis_client.set ("Age",'29')
name = redis_client.get("name")
age = redis_client.get("Age")
print(name.decode()) 
print(age.decode()) 

redis_client.lpush("nums", 1)
redis_client.lpush("nums", 2)
redis_client.lpush("nums", 3)
 
numbers = redis_client.lrange("nums", 3, -3)
print(numbers)