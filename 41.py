a = int(input("搭了幾次電梯:"))
b=[]
for i in range(a):
    b.append(input("樓層為:"))
c = 1
d = 0
for i in range(len(b)):
    while c != int(b[i]):
        if c < int(b[i]):
            d+=20
            c+=1
        elif c > int(b[i]):
            d+=10
            c-=1
print(str(d)+'元')