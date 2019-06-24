"""
创建一个类
1.Python对属性权限的控制是通过属性名来实现的，如果一个属性由双下划线开头(__)，
该属性就无法被外部访问。
但是，如果一个属性以"__xxx__"的形式定义，那它又可以被外部访问了，
以"__xxx__"定义的属性在Python的类中被称为特殊属性，
有很多预定义的特殊属性可以使用，通常我们不要把普通属性用"__xxx__"定义。
以单下划线开头的属性"_xxx"虽然也可以被外部访问，但是，按照习惯，他们不应该被外部访问。

2.绑定在一个实例上的属性不会影响其他实例，
但是，类本身也是一个对象，如果在类上绑定一个属性，
则所有实例都可以访问类的属性，并且，
所有实例访问的类属性都是同一个！也就是说，
实例属性每个实例各自拥有，互相独立，而类属性有且只有一份。

3.当实例属性和类属性重名时，实例属性优先级高

4.直接把 lambda 函数赋值给 self.get_grade 和绑定方法有所不同，
函数调用不需要传入 self，但是方法调用需要传入 self。
Author:轻风
Version:v1
"""
# import types


class Person(object):
    count = 0
    address = 'Beijing'

    @classmethod
    def how_many(cls):
        return cls.count

    def __init__(self, name, gender, birth, score, **kwargs):
        self.name = name
        self.gender = gender
        self.birth = birth
        self.score = score
        self.get_grade = lambda: 'A'
        for k, v in kwargs.items():
            setattr(self, k, v)


def fn_get_grade(self):
    if self.score >= 80:
        return 'A'
    if self.score >= 60:
        return 'B'
    return 'C'


p1 = Person('Mike', 'Male', '1990-01-01', 90)
print(p1.get_grade)
print(p1.get_grade())
print(Person.how_many())
# print(p1.name + "," + p1.gender + "," + p1.job + "," + p1.address)
# p1.get_grade = types.MethodType(fn_get_grade, p1, Person)
# print(p1.get_grade())
# p1 = Person()
# p1.name = 'Bart'
#
# p2 = Person()
# p2.name = 'Adam'
#
# p3 = Person()
# p3.name = 'Lisa'
#
# L1 = [p1, p2, p3]
# print(L1[0].name)
# print(L1[1].name)
# print(L1[2].name)
