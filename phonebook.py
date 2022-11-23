from cs50 import get_string

 people = {
     "Ilaria": "3208730487",
     "Marco" : "3288996072",

 }
name = get_string("Name: ")
if name in people:
    print(f"Number: {people[name}")