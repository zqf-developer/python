def city_country(city_name, country_name):
    name = '"' + city_name.title() + ',' + country_name.title() + '"'
    return name


name_01 = city_country('santiago', 'chile')
print(name_01)
name_02 = city_country('beijing', 'china')
print(name_02)
name_03 = city_country('paris', 'french')
print(name_03)
