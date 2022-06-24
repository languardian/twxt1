M = int(input("請輸入階層值"))
n = 1
N = 1
while True:
    N = N * n
    if N >= M:
        break;
    n+=1
print("超過M為"+str(M)+"的最小階層N值為:"+str(n))