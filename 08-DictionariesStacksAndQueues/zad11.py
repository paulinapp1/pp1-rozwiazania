import json
favorite_movie = {
    "title": "Mamma Mia",
    "year": 2008,
    "actor": {"leading": "Amanda Seyfried", "supporting": "Meryl Streep"},
    "oscar": False,
    "genre": ["Musical", "Romance"]
}

with open("favorite.json", "w") as file:
    json.dump(favorite_movie, file, indent=6)


#codewars stad programy na kolokwia