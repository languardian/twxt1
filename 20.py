group = int(input("組數為:"))
num = []
for i in range(group):
    num.append(input("第"+str(i+1)+"組:").split())
for i in range(group):
    print("第"+str(i+1)+"組應收費用:"+str(250*int(num[i][0])+125*int(num[i][1])))