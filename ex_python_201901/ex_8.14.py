def make_car(manufacturer, model, **car_info):
    car = {}
    car['car_manufacturer'] = manufacturer
    car['car_model'] = model
    for key, value in car_info.items():
        car[key] = value
    return car


car = make_car('subaru', 'outback',
               color='blue',
               tow_package=True)
print(car)
