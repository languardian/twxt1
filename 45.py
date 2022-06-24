a = int(input("輸入月:"))
b = int(input("輸入日:"))
s = (a*2+b)%3
if s == 0:
    print("普通")
elif s == 1:
    print("小吉")
else:
    print("大吉")