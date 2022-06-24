a = int(input("輸入整數n(基數)"))
c = 1
b = a // 2
for i in range(1,a,2):
    if i < a:
        for j in range(b):
            print(" ",end='')
        print(str(i),end='')
        print()
for i in range(a):
    if i < a/2:
        print(str(c),end='')
        c+=2
    if c == a+2:
        c-=4
    if i > a/2:
        print(str(c),end='')
        c-=2
print()
for i in range(a,0,-2):
    if i < a:
        for j in range(b):
            print(" ",end='')
        print(str(i),end='')
        print()
