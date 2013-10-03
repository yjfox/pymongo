"""
Query 1:
Write a query that finds average rating of each movie.

Created on Sep 26th, 2013
"""
from pymongo import MongoClient 

client = MongoClient()
db = client.test
users=db.users
movies=db.movies
movieIdlist=movies.distinct("_id")    
userIdlist=users.distinct("_id")

for mid in movieIdlist:
    sum=0
    num=0
    movieId=int(mid)
    for uid in userIdlist:
        userId=int(uid)
        result=users.find({"_id":userId},{"movie":{"$elemMatch":{"movieId":movieId}}})
        for info in result:
            if 'movie' in info.keys():    # what the mongodb returned is already type 'dict', no need to use json to read 
                sum+=info['movie'][0]['rate']
                num+=1
    if(sum!=0 and num!=0):
        rate=float(sum)/float(num)
        print "movie %d is rated at %.2f"%(movieId,rate)
