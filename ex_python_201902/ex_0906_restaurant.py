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


class IceCreamStand(Restaurant):
    """模拟冰淇淋小店"""

    def __init__(self, restaurant_name, cuisine_type):
        """初始化父类属性"""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = {'奶油冰淇淋', '草莓冰淇淋', '芒果冰淇淋'}

    def describe_iceCream(self):
        all_flavor = ''
        for flavor in self.flavors:
            all_flavor += "'" + flavor + "', "
        print("all ice cream " + all_flavor)


iceCream = IceCreamStand('wind', 'ice')
iceCream.describe_restaurant()
iceCream.describe_iceCream()
