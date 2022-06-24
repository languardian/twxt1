list1 = []
a = list(input("請輸入(NxM)").split())
h,r = int(a[1]),int(a[0])
for i in range(0,int(a[0])):
    list1.append(input("請輸入矩陣數值第"+str(i+1)+"列為:").split())
list2 =[[0]*r for _ in range(h)]#創建一個二維陣列
if a[0]=="0" or a[1]=="0":
    print("結束程式")
else:
    for i in range(0,int(a[1])):
        ans = ''
        for j in range(0,int(a[0])):
            list2[i][j] = list1[j][i]
            ans = ans + list2[i][j]
            if j != len(list2):
                ans+= ' '
            if j == len(list2)-2:
                print("輸出矩陣數值第"+str(i+1)+"列為:"+ans)
