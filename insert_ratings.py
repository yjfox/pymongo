"""
Aim to insert the file ratings.dat into mongoDB

Created on Sep 26th, 2013
"""
from pymongo import MongoClient

client = MongoClient()
db = client.test
users=db.users
fileOpen=open('ratings.dat','rb')
f=fileOpen.read().split('\n')
flag=0


for line in f:
    list={}
    try:
        list['_id'],list['movieId'],list['rate'],list['time']=line.split('::')
        listid=int(list['_id'])
        movieId=int(list['movieId'])
        rate=int(list['rate'])
    except ValueError:
        continue
    
    # variable "flag" used to indicate whether this id is a new user or already existed
        
    if(flag==listid):  
        users.update({"_id":listid},{"$push":{"movie":{"movieId":movieId,"rate":rate,"time":list['time']}}})
    else:
        users.insert({"_id":listid,"movie":[{"movieId":movieId,"rate":rate,"time":list['time']}]})
    flag=listid
    print(listid)
    
fileOpen.close()
