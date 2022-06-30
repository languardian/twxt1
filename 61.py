a=input("請輸入遊戲時間").split(":")
a=int(a[0])*60+int(a[1])

b=0
c=a-75
b=b+6
b=b+int(c/30)*6+int(((c/30)+1)/3)-int(((c/30)+1)/2)

print(b)