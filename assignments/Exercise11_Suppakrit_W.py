num = int(input("Input your rows: "))
star = 1
space = num - 1
for i in range(num):
    print(f"{space * ' '}{star * '*'}")
    space -= 1
    star += 2