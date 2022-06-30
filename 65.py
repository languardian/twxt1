a=input("請輸入A的好友").split(" ")
b=input("請輸入B的好友").split(" ")
c=0

for i in range(len(a)):
    for j in range(len(b)):
        if a[i]==b[j]:
            c=c+1

print(c)