movie={
    "title":"Mamma Mia",
    "year":"Whatever",
    "actor":{"leading": "someone","supporting":"someone else"},
    "oscar":False

}
import json
with open("favourite.json","w") as file:
    json.dump(movie,file)