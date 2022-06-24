a = list(input("請輸入月租費型式(186,386,586,986),通話時間(sec)為").split(","))
aa = [186,386,586,986]
b = [0.09,0.08,0.07,0.06]
c = [0.9,0.8,0.7,0.6,0.5]
d = 0
while True:
    if int(a[0]) == aa[d]:
        break;
    if d > 3:
        break;
    d += 1

e = round(int(a[1]) * b[d],0)

if e <= aa[d]:
    print("通話費為:"+str(aa[d]))
elif e <= aa[d]*2:
    e = round(e * c[d])
    print("通話費為:"+str(e))
elif e >= aa[d]*2:
    e = round(e * c[d+1])
    print("通話費為:"+str(e))