list1 = list(input("輸入值為:").split(","))
for i in range(len(list1)-1):
    for j in range(len(list1)-i-1):
        if int(list1[j])>int(list1[j+1]):
            aa = list1[j]
            list1[j] = list1[j+1]
            list1[j+1] = aa
a=""
b=""
for i in range(len(list1)):
    a = str(a) + list1[i]
    b = str(b) + list1[len(list1)-i-1]
a = int(a)
b = int(b)
b = b-a
print(b)