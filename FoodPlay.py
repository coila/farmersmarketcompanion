import psycopg2
from DB import *

#instantiate connection object
conn = DB()

#check to see if an item already exists in DB, (eg a food called "Apples")
#returns the item's ID if it exists or -1 if it is not present
def check(thistype, thislabel):

    #does this item already exist?
    thisID = conn.query("SELECT id" + thistype + " from " + thistype + " where " + thistype + "name = '" + thislabel + "';")

    if thisID:
        return thisID[0][0]
    else:
        return -1

#insert a new item into the DB and return its ID
def insertOne(thistype, thislabel):

    #if this item already exists, return its ID
    returnID = check(thistype,thislabel)

    if returnID > 0:
        return returnID
    #otherwise, need to insert this item and create a new ID
    else:

        thisID = conn.query("insert into " + thistype + " (" + thistype + "name) values ('" + thislabel + "') returning id" + thistype + ";")
        return thisID[0][0]

#create linking record between a place, season, food pairing
def insertLink(place, season, food):
    idFood = insertOne("food",food)
    idPlace = insertOne("place",place)
    idSeason = insertOne("season",season)
    sqlstring = "INSERT INTO linkedData (fkFood, fkPlace, fkSeason) VALUES (" + str(idFood) + "," + str(idPlace) + "," + str(idSeason) + ")"
    # print sqlstring
    conn.query(sqlstring)

#given a place (eg "California") and a season [eg "July (late)" or "August (early)"] return a list of foods that are in season
def getAll(place, season):

    query = conn.query("SELECT foodname FROM \"foodQ\" where placename = '" + place + "' and seasonname = '" + season + "';")
    results = []
    for record in query:
        results.append(record[0])
    return results

