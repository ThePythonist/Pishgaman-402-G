# movie = {
#     "name": "interstellar",
#     "director": "nolan",
#     "release": 2014,
#     "genre": "science fiction",
#     "rate": 7.8
# }
#
# key = input("Search any key : ")
#
# if key in movie:
#     print("Found :", movie[key])
# else:
#     print("Key not found")


movies = [
    {"name": "inception", "rate": 8.0, "director": "nolan"},
    {"name": "pulp fiction", "rate": 8.0, "director": "tarantino"},
    {"name": "django unchained", "rate": 7.5, "director": "tarantino"},
    {"name": "se7en", "rate": 7, "director": "fincher"},
]

# print(movies[0]["rate"])

for movie in movies:
    if movie["director"] == "tarantino":
        print(movie)
