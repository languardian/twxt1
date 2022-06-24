list1 = ['金','銀','銅','優']
list2 = []
a = int(input("輸入比數n:"))
for i in range(4):
    list2.append(input(list1[i]+' '))
for i in range(4):
    if a < int(list2[i]):
        list2[i] = a
for i in range(4):
    print(list1[i]+'牌得到'+str(list2[i])+'面')