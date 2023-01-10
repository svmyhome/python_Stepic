

def city_transform(city, country, count=''):
    if count:
        city_country = f'{city}, {country}, {count}'
    else:
        city_country = f'{city}, {country}'
    return city_country.title()
