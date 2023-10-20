def forecast(*args):
    forecast_dict = {
        'Sunny': [],
        'Cloudy': [],
        'Rainy': []
    }

    for town, weather in args:
        if weather in forecast_dict.keys():
            forecast_dict[weather].append(town)

    result = ''
    for weather, locations in forecast_dict.items():
        if locations:
            for location in sorted(locations):
                result += f'{location} - {weather}\n'

    return result


print(forecast(
    ("Sofia", "Sunny"),
    ("London", "Cloudy"),
    ("New York", "Sunny")))

print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))

print(forecast(
    ("Tokyo", "Rainy"),
    ("Sofia", "Rainy")))
