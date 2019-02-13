class User(object):
    """创建用户"""

    def __init__(self, first_name, last_name, age, sex):
        """初始化用户属性"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex

    def describe_user(self):
        """打印用户基本信息"""
        print("My full name is " + self.first_name.title() +
              ' ' + self.last_name.title() + " and age is " +
              str(self.age) + ' ' + self.sex)

    def great_user(self):
        """个性化问候"""
        print("Hello " + self.first_name.title() + ' ' + self.last_name.title() + "!")


user = User('helen', 'kathy', 22, 'women')
user.describe_user()
user.great_user()

user00 = User('bruce', 'li', 30, 'men')
user00.describe_user()
user00.great_user()
