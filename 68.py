a = input("請輸入第一組數字:(最少兩位最多六位)")
aa = len(a)
b = input("請輸入第二組數字:(最少兩位最多六位)")
A = 0
B = 0
if len(a) == len(b) and len(a)>=2 and len(a)<=6:
    while aa > 0:
        for i in range(aa-1):
            for j in range(aa-i-1):
                if a[i] == a[i+j+1] and b[i] == b[i+j+1]:
                    print("一組數字內有相同數字，請重新輸入")
                    break;
        aa-=1
    else:
        for i in range(len(a)):
            if a[i] in b and a[i] == b[i]:
                A = A + 1
            elif a[i] in b:
                B = B + 1
        if A == 4:
            print(str(A)+"A"+str(B)+"B 全對")
        elif A < 4 :
            print(str(A)+"A"+str(B)+"B 加油")
else:
    print("數量不相等或是少於2位或大於6位，請重新輸入")