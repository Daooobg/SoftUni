countries = input().split(', ')
capitals = input().split(', ')

countries_capitals = {country: capital for country, capital in zip(countries, capitals)}

for country, capital in countries_capitals.items():
    print(f'{country} -> {capital}')