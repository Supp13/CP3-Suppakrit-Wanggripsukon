s = int(input("Distance (km): "))
t = int(input("Time (hr): "))
if s%t == 0:
    print(int(s/t),"km/hr")
else:
    print(s/t,"km/hr")