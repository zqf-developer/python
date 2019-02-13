class Restaurant():
    """模拟餐厅营业"""

    def __init__(self, restaurant_name, cuisine_type):
        """初始化餐厅的属性"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """打印餐厅描述信息"""
        print(self.restaurant_name.title() + ' ' + self.cuisine_type.title())

    def open_restaurant(self):
        """打印餐厅正在营业"""
        print(self.restaurant_name.title() + " is opening now!")

    def read_restaurant(self):
        """打印有多少人就过餐"""
        print(str(self.number_served) + " people had eat in the " + self.restaurant_name.title())

    def set_number_served(self, number):
        """设置就餐人数"""
        self.number_served = number

    def increment_number_served(self, number_served):
        """可能的就餐人数"""
        self.number_served += number_served


restaurant = Restaurant('paria', '5A')
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.read_restaurant()
# 设置就餐人数
# restaurant.set_number_served(12)
# 打印信息
# restaurant.read_restaurant()
# 增加人数
restaurant.increment_number_served(20)
restaurant.read_restaurant()

restaurant_00 = Restaurant('frech', '4A')
restaurant_00.describe_restaurant()
restaurant_00.open_restaurant()

# print(restaurant.restaurant_name)
