a=int(input("請輸入要判斷的第一數字"))
b=int(input("請輸入要判斷的第二數字"))
c=0
if (b-a)==2:
    for i in range(2,a-1):
        if a%i==0:
            c=1
    for j in range(2,b-1):
        if b%j==0:
            c=1    
    if c==1:
        print("No")
    else:
        print("Yes")
else:
    print("No")