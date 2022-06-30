a=input("輸入")
b=[]

for i in range(0,len(a)-4,5):
    c=0
    for j in range(i,i+5,1):
        if a[j]==".":
            c=c+1
    b.append(c)

for k in range(len(b)):
    print(b[k],end="")