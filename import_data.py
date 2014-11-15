import csv
import FoodPlay

infile = "/Users/emma/Downloads/seasonalfooddb.csv"

with open(infile, 'r') as f:
    data = [row for row in csv.reader(f.read().splitlines())]

for row in data:
    food = row[0].strip()
    season = row[1].strip()
    place = row[2].strip()

    FoodPlay.insertLink(place,season,food)