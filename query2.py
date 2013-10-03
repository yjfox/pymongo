"""
Query 2:
Write a query that finds users who are similar to a given user (target user), 
the id of the target user is an input parameter.  
Users are similar to the target user if they rate the same movies.

Created on Sep 27th, 2013
"""
from pymongo import MongoClient 
import numpy

client = MongoClient()
db = client.test
users=db.users
movies=db.movies
movieIdlist=movies.distinct("_id")    
userIdlist=users.distinct("_id")

#get target user's rating movies

targetId=raw_input("Target user id:")
result=users.find({"_id":int(targetId)})
for info in result:
    targetlist=[]
    for i in info["movie"]:    # what the mongodb returned is already type 'dict', no need to use json to read 
        targetlist.append(i["movieId"])
print "User",targetId,"hass rated movies:",targetlist

#get other users' rating movies and compare with target user

for uid in userIdlist:
    movielist=[]
    userId=int(uid)
    result=users.find({"_id":userId})
    for info in result:
        for i in info["movie"]:    # what the mongodb returned is already type 'dict', no need to use json to read 
            movielist.append(i["movieId"])
    if numpy.array_equal(targetlist,movielist):  #"numpy" is a module that provides a function to judge whether these two arrays are equal
        print "The movies rated by user",userId,"is equal to user",targetId
