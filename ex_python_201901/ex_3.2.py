# 练习列表各种操作
invite_persons = ['zhangyu','zhuozhiying','lihuoxiang','zhangwen','huanghaiting']
print("Dear " + invite_persons[0].title() + " ! I want to invite you to dinner.")
print("Dear " + invite_persons[1].title() + " ! I want to invite you to dinner.")
print("Dear " + invite_persons[2].title() + " ! I want to invite you to dinner.")
print("Dear " + invite_persons[3].title() + " ! I want to invite you to dinner.")
print("Dear " + invite_persons[4].title() + " ! I want to invite you to dinner.")

not_join_persons = 'zhangwen'
print(not_join_persons + " can't make an appointment")
invite_persons[-2] = 'zhangyi'  
print("Dear " + invite_persons[0].title() + " ! I want to invite you to dinner.")
print("Dear " + invite_persons[1].title() + " ! I want to invite you to dinner.")
print("Dear " + invite_persons[2].title() + " ! I want to invite you to dinner.")
print("Dear " + invite_persons[3].title() + " ! I want to invite you to dinner.")
print("Dear " + invite_persons[4].title() + " ! I want to invite you to dinner.")

print("I found a bigger table !")
invite_persons.insert(0,'zhangtian')
print(invite_persons)
invite_persons.insert(3,'mijijun')
print(invite_persons)
invite_persons.append('ligang')
print(invite_persons)
print("Dear " + invite_persons[0].title() + " ! I want to invite you to dinner.")
print("Dear " + invite_persons[1].title() + " ! I want to invite you to dinner.")
print("Dear " + invite_persons[2].title() + " ! I want to invite you to dinner.")
print("Dear " + invite_persons[3].title() + " ! I want to invite you to dinner.")
print("Dear " + invite_persons[4].title() + " ! I want to invite you to dinner.")
print("Dear " + invite_persons[5].title() + " ! I want to invite you to dinner.")
print("Dear " + invite_persons[6].title() + " ! I want to invite you to dinner.")
print("Dear " + invite_persons[7].title() + " ! I want to invite you to dinner.")
print("I am very sorry, I can only invite two guests to dinner.")
pop_person_one = invite_persons.pop()
print(pop_person_one.title() + " I am very sorry!")
print(invite_persons.pop().title() + " I am very sorry!")
print(invite_persons.pop().title() + " I am very sorry!")
print(invite_persons.pop().title() + " I am very sorry!")
print(invite_persons.pop().title() + " I am very sorry!")
print(invite_persons.pop().title() + " I am very sorry!")
print(invite_persons)
print(invite_persons[0].title() + "I still want to invite you to dinner.")
print(invite_persons[1].title() + "I still want to invite you to dinner.")
del invite_persons[0]
invite_persons.remove('zhangyu')
print(invite_persons)

