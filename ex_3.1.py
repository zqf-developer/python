names = ['Amy','Elic','Kathy','Unice']
print(names[0])
print(names[1])
print(names[2])
print(names[3])

print(names[-4])
print(names[-3])
print(names[-2])
print(names[-1])

for name in names:
	print("Hello "+name+",Nice to meet you !\n")

trans_style = ['motorcycle','car','metre','bus']

message_motorcycle = "I like to bike " + trans_style[-4] + "\n"
print(message_motorcycle)

message_car = "I want to buy a " + trans_style[1] + " next year" + "\n"
print(message_car)

message_metre = "SomeTimes i will to take a " + trans_style[-2] + "\n"
print(message_metre)

message_bus = "I will take a " + trans_style[-1] + " everytime" +"\n"
print(message_bus)

