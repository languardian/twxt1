a = input("請輸入路程公里數(km):")

b = (float(a)-1.5)//0.25
if ((float(a)-1.5)%0.25) != 0:
    b+=1
print('所需車資為:'+str(75+(5*b)))