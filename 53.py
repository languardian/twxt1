a = input("請輸入n值:")
list1 = []
list2 = []
for i in range(int(a)):
    list1.append(input("請輸入姓名"))
    list2.append(input("請輸入電子郵件"))

found1 = input("請輸入要查詢的電子郵件名稱:")
for i in range(len(list1)):
    if found1 == list1[i]:
        print(list1[i]+"電子郵件帳號為:"+list2[i])