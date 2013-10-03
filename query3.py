"""
Query 3:
Write a query that finds to number of movies in each genre.

Created on Sep 27th, 2013

"""
from pymongo import MongoClient 

client = MongoClient()
db = client.test
movies=db.movies
movieIdlist=movies.distinct("_id")

#genrelist[0]:numlist[0],genrelist[1]:numlist[1]....which means the movie number of every genre is stored in the list "numlist"

genrelist=["Action","Adventure","Animation","Children","Comedy","Crime","Documentary","Drama","Fantasy","Film-Noir","Horror","Musical","Mystery","Romance","Sci-Fi","Thriller","War","Western"]
numlist=[0]*18

for mid in movieIdlist:    
    result=movies.find({"_id":mid})
    for info in result:
        i=0
        for genre in genrelist:
            if genre in info["genre"]:
                numlist[i]+=1
            i+=1

#print outcomes

i=0
for genre in genrelist:
    print "Genre of",genre,"has",numlist[i],"movies"
    i+=1            
        