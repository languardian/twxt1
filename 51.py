a=input("輸入自傳")
b=[]
b1=[]

for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]==a[j]:           
            b.append(a[i])
            break
    for u in range(len(b)):
        for h in range(u+1,len(b)):
            if b[u]==b[h]:
                b.remove(b[u])
                break                
print(b)