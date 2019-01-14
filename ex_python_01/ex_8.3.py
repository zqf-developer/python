def make_shirt(shirt_word, shirt_size):
    """显示T恤的字样"""
    print("T-shirt size is " + shirt_size)
    print("T-shirt have a sentence '" + shirt_word.title() + "'.")


make_shirt(shirt_size='XL', shirt_word='I love Python')


def describe_city(city_name, city_country='Iceland'):
    """显示城市名字和所属国家"""
    print(city_name.title() + " is in " + city_country.title() + ".")


describe_city('reykjavik')
describe_city('beijing', 'china')
