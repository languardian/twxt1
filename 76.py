s = input("請輸入傳送密碼(6位數)")
a = ""
b = 0
for i in range(len(s)):
    for j in range(0,10):
        if int(s[i]) == ((j*4)%7):
            if int(s[i]) == ((j*4)%7) and j == 7:
                a = a + "(7)"
                b+=1
            elif int(s[i]) == ((j*4)%7) and j == 8:
                a = a + "(8)"
                b+=1
            elif int(s[i]) == ((j*4)%7) and j == 9:
                a = a + "(9)"
                b+=1
            else:
                a = a + str(j)
                b+=1
if b >= 6:
    print(a)
else:
    print("長度不足6個字元，請重新輸入")
14
21
35
42
56
63
70
84
91