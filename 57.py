b = [0,72,62,82,44,60]
qus1 = input("請選擇主餐及升級的套餐:")
qus2 = input("是否升級成大杯飲料:")
qus3 = input("是否換成大薯:")
ans = 0
for i in range(5):
    if int(qus1[0]) == i+1:
        ans += b[i+1]
        if qus1[1] == 'A':
            ans+=55
        elif qus1[1] == 'B':
            ans+=68
if qus2 == "是":
    ans += 7
if qus3 == "是":
    ans += 13
print("總共為"+str(ans)+"元")