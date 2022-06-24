ac = ['123','456','789','336','775','566']
pd = ['456','789','888','558','666','221']
money = [9000,5000,6000,10000,12000,7000]
a = int(input("輸入查詢組數N為:"))
b = []
for i in range(a):
    b.append(input("帳號與密碼:").split())

for i in range(a):
    for j in range(len(ac)):
        if (b[0] == ac[j]) and (b[1] == pd[j]):
            print(str(money[j]))

