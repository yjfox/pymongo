"""
Extra Query 1:
Function: Input a movie ID, return feedbacks about the users who ever add tags and their content

Created on Sep 27th, 2013
"""
from pymongo import MongoClient

client = MongoClient()
db = client.test
tags=db.tags
userIdlist=tags.distinct("_id")

targetId=raw_input("Movie ID is:")

for uid in userIdlist:
    userId=int(uid)
    
    # result=users.find({"_id":userId},{"movie":{"$elemMatch":{"movieId":int(targetId)}}})  
    # This method above only return one column for one userID, while sometimes a user may add two or more tags on one movie.
    # So I modify the sentence. The new one showed as follow may reduce the efficiency, but the output 100% correct
    
    result=tags.find({"_id":userId},{"movie.movieId":int(targetId),"movie.tag":1})   

    for info in result:
        if 'movie' in info.keys():    # what the mongodb returned is already type 'dict', no need to use json to read 
            for i in info['movie']:
                if(i['movieId']==int(targetId)):
                    print "User ",userId," ever added a tag ",i['tag']