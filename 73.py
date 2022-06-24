list1 = list(input("請輸入時間1(時:分:秒):").split(":"))
yy = input("請輸入時間2(秒):")
list2 = ['0','0','0']
a = int(list1[0])*3600+int(list1[1])*60+int(list1[2])
list2[0] = int(yy)//3600
list2[1] = (int(yy)-(list2[0]*3600))//60
list2[2] = int(yy)-list2[0]*3600-list2[1]*60
print("時間1("+list1[0]+':'+list1[1]+':'+list1[2]+')格式轉換後為'+str(a)+'秒')
print("時間2("+str(yy)+"秒)="+str(list2[0])+':'+str(list2[1])+':'+str(list2[2]))