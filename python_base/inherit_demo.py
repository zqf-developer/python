"""
类的继承
1. 一定要用 super(Student, self).__init__(name, gender)
去初始化父类，否则，继承自 Person 的 Student 将没有 name 和 gender。
Author:轻风
Version:v1
"""


class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def who_am_i(self):
        print('I am a Person, my name is %s' % self.name)


class Student(Person):
    def __init__(self, name, gender, score):
        super(Student, self).__init__(name, gender)
        self.score = score


class Teacher(Person):
    def __init__(self, name, gender, course):
        super(Teacher, self).__init__(name, gender)
        self.course = course


def is_special_attr(attr):
    return "__" not in attr


p = Person('Mike', 'Male')
s = Student('Bob', 'Male', 99)
t = Teacher('Alice', 'Female', 'English')
print(isinstance(p, Person))  # 这说明在继承链上，一个父类的实例不能是子类类型，因为子类比父类多了一些属性和方法。
print(isinstance(p, Student))
print(isinstance(p, Teacher))

print(isinstance(s, Person))  # 一个实例可以看成它本身的类型，也可以看成它父类的类型。
print(isinstance(s, Student))
print(isinstance(s, Teacher))

print(type(p))
# print(dir(p))
print(list(filter(is_special_attr, dir(p))))

print(getattr(s, 'scotttre', 'not Exist'))

