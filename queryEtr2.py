"""
Extra Query 2:
Output a list of popular movies. 
criteria: judged by the number of users who added tags.

Created on Sep 27th, 2013
"""
from pymongo import MongoClient

client = MongoClient()
db = client.test
tags=db.tags
movieIdlist=tags.distinct("movie.movieId")    
userIdlist=tags.distinct("_id")
max=raw_input("The number of list:")   #How many movies you want be showed on the list
popmovieList=[0]*int(max)
movietagNum=[0]*int(max)

#This function aim to sort the list and make sure it contains the movies of Top "max" (max could be 5,10 or any integer)

def sortlist(movieId,num):
    flag=1
    for i in range(int(max)):
        if(num<movietagNum[i]):
            flag=0
            popmovieList.insert(i,movieId)
            popmovieList.pop(0)
            movietagNum.insert(i,num)
            movietagNum.pop(0)
            break
    if flag:  #mean this num is bigger than anyone in the movietagNum list, so append it to the end of list
            popmovieList.append(movieId)
            popmovieList.pop(0)
            movietagNum.append(num)
            movietagNum.pop(0)

    
for movieId in movieIdlist:
    num=0
    for userId in userIdlist:
        result=tags.find({"_id":userId},{"movie":{"$elemMatch":{"movieId":movieId}}})
        for info in result:
            if 'movie' in info:
                num+=1
    sortlist(movieId,num)
    print "The Top",max,"popular movies:",popmovieList
    print "The number of their tags: ",movietagNum
            
