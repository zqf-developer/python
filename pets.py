"""
pet_name,animal_type 是形参，传入的值是实参
"""


def describe_pet(pet_name, animal_type):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


describe_pet('hamster', 'harry')  # 调用方法上面要两个空行
describe_pet(animal_type='dog', pet_name='willie')

