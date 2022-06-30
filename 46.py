list=['金','銀','銅','優']
n=int(input('輸入比數'))
dict={}
for i in range(0,n):
    c=int(input(list[i]))
    dict[list[i]]=c
for a,b in dict.items():
    print(a+'牌得到',n,'面')