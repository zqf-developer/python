# 外星人的颜色
alien_color = 'yellow'

if alien_color == 'green':
    print("Congratulations! Get 5 points.")
if alien_color != 'green':
    print()

if alien_color == 'green':
    print("shooting alien get 5 points")
if alien_color != 'green':
    print("shooting alien get 10 points")

if alien_color == 'green':
    print("shooting alien get 5 points")
else:
    print("shooting alien get 10 points")

# 打印三条信息
if alien_color == 'green':
    print("shooting alien get 5 points")
elif alien_color == 'yellow':
    print("shooting alien get 10 points")
else:
    print("shooting alien get 15 points")

# 打印一条信息
if alien_color == 'green':
    points = 5
elif alien_color == 'yellow':
    points = 10
else:
    points = 15
print("shooting alien get " + str(points) + " points")
