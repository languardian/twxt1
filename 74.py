a = input("依序輸入四個顏色:").split()
anslist = ['red','blue','red','green']
for i in range(len(a)):
    if a[i] in anslist and a[i] == anslist[i]:
        print("1",end='')
    elif a[i] in anslist:
        print('2',end='')
    else:
        print("3",end='')