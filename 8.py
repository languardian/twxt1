m = int(input("輸入第一行正整數為:"))
n = list(input("第二行中數列中的數字為:").split())
nn=[];nnn=[]

for i in range(m):
    a=0
    for j in range(len(n)):
        if n[i] == n[j]:
            a+=1
    nn.append(a)

for i in range(len(n)):
    b=0
    for j in range(len(n)):
        if n[i] == n[j]:
            b+=1
    if b == max(nn):
        if n[i] not in nnn:
            nnn.append(n[i])

if max(nn) == '1':
    print("每個數字剛好只出現1次")
else:
    ans=''
    for i in range(len(nnn)):
        ans = ans + nnn[i]
        if i != (len(nnn)-1):
            ans = ans + "、"
    print("最大出現次數的數字為:"+ans)
    print("出現次數為:"+str(max(nn)))