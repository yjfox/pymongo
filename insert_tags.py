"""
Aim to insert the file tags.dat into mongoDB

Created on Sep 27th, 2013

"""
from pymongo import MongoClient

client = MongoClient()
db = client.test
tags=db.tags
fileOpen=open('tags.dat','rb')
f=fileOpen.read().split('\n')
flag=0

for line in f:
    list={}
    try:
        list['_id'],list['movieId'],list['tag'],list['time']=line.split('::')
        listid=int(list['_id'])
        movieId=int(list['movieId'])
    except ValueError:
        continue
        
    # variable "flag" used to indicate whether this id is a new user or already existed

    if(flag==listid):
        tags.update({"_id":listid},{"$push":{"movie":{"movieId":movieId,"tag":list['tag'],"time":list['time']}}})
    else:
        tags.insert({"_id":listid,"movie":[{"movieId":movieId,"tag":list['tag'],"time":list['time']}]})
    flag=listid
    print(listid)
    
fileOpen.close()