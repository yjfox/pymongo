"""
Aim to insert the file movies.dat into mongoDB

Created on Sep 26th, 2013

"""
from pymongo import MongoClient

client = MongoClient()
db = client.test
movies=db.movies
fileOpen = open('movies.dat','rb')
f=fileOpen.read().split('\n')

for line in f:
    list={}
    try:
        list['_id'],list['name'],list['genre']=line.split('::')
    except ValueError:
        continue
    id=movies.insert(list)
    print(id)

fileOpen.close()

