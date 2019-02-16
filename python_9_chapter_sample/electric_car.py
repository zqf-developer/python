"""一组可用于表示电动汽车的类"""

from python_9_chapter_sample.car import Car


class Battery(object):
    """一次模拟电动汽车电瓶的简单尝试"""

    def __init__(self, battery_size=70):
        """初始化电瓶的属性"""
        self.battery_size = battery_size

    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        """打印一条消息，指出电瓶的续航里程"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)


class ElectricCar(Car):
    """电动车的独特之处"""

    def __init__(self, make, model, year):
        """初始化父类的属性，再初始化电动车特有的属性"""
        super().__init__(make, model, year)
        self.battery = Battery()
        # self.battery_size = 70
        # super(ElectricCar, self).__init__(make, model, year) python 2.7必须这样添加实参

    def fill_gas_tank(self):
        """电动车没有油箱"""
        print("This car does't need a gas tank!")


