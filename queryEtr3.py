"""
Extra Query 3:
Find out users who ever rated a movie and then added a tag on it as well.

Created on Sep 27th, 2013
"""
from pymongo import MongoClient 

client = MongoClient()
db = client.test
tags=db.tags
users=db.users
userIdlist=tags.distinct("_id")

for userId in userIdlist:
    resulttag=tags.find({"_id":userId})
    resultrate=users.find({"_id":userId})
    for inforate in resultrate:
        for irate in inforate["movie"]:
            movieId=irate["movieId"]
            for infotag in resulttag:
                for itag in infotag["movie"]:
                    if movieId==itag["movieId"]:
                        print "User",userId,"rated movie ID=",movieId,"at rate=",irate["rate"],"with a tag:",itag["tag"]       