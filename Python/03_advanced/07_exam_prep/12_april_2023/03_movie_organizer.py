def movie_organizer(*args):
    movie_dict = {}

    for movie_name, genre in args:
        if genre not in movie_dict.keys():
            movie_dict[genre] = []
        movie_dict[genre].append(movie_name)

    sorted_dict = {kvp[0]: kvp[1] for kvp in sorted(movie_dict.items(), key= lambda kvp: (-len(kvp[1]), kvp[0]))}

    result = ''
    for k, v in sorted_dict.items():
        result += f'{k} - {len(v)}\n'
        for movie in sorted(v):
            result += f'* {movie}\n'

    return result


print(movie_organizer(
    ("The Matrix", "Sci-fi")))
print(movie_organizer(
    ("The Godfather", "Drama"),
    ("The Hangover", "Comedy"),
    ("The Shawshank Redemption", "Drama"),
    ("The Pursuit of Happiness", "Drama"),
    ("The Hangover Part II", "Comedy")))

print(movie_organizer(
    ("Avatar: The Way of Water", "Action"),
    ("House Of Gucci", "Drama"),
    ("Top Gun", "Action"),
    ("Ted", "Comedy"),
    ("Duck Soup", "Comedy"),
    ("The Dark Knight", "Action"),
    ("A Star Is Born", "Musicals"),
    ("The Warrior", "Action"),
    ("Like A Boss", "Comedy"),
    ("The Green Mile", "Drama"),
    ("21 Jump Street", "Comedy")))

