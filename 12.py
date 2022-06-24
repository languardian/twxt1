number1 = list(input("輸入一整數序列為:").split())
a = []
for i in range(len(number1)):
    b = 0
    for j in range(len(number1)):
        if number1[i] == number1[j]:
            b+=1
    a.append(b)

if max(a) > ((len(number1))/2):
    print("過半元素為:"+str(number1[max(a)]))
else:
    print("過半元素為:NO")
