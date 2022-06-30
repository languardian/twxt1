a=int(input("小明身上有幾元"))
b=int(input("販賣機有幾種飲料"))
c=[]
e=0

for i in range(b):
    c.append(input("輸入飲料價格"))
c.sort()

for j in range(len(c)):
    if int(c[j])<=a:
        e=e+1
    else:
        break
print(e)