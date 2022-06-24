a = int(input("請輸入n:"))
b = int(input("請輸入k:"))
c = a
d = a//b
while d != 0:
    c = c + d
    d = d // b

print("Peter可以抽"+str(c)+"隻紙菸")