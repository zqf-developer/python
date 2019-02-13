class Restaurant():
    """模拟餐厅营业"""

    def __init__(self, restaurant_name, cuisine_type):
        """初始化餐厅的属性"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """打印餐厅描述信息"""
        print(self.restaurant_name.title() + ' ' + self.cuisine_type.title())

    def open_restaurant(self):
        """打印餐厅正在营业"""
        print(self.restaurant_name.title() + " is opening now!")


restaurant = Restaurant('paria', '5A')
restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant_00 = Restaurant('frech', '4A')
restaurant_00.describe_restaurant()
restaurant_00.open_restaurant()

# print(restaurant.restaurant_name)
