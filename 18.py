poker = list(input("輸入5張牌，可能會有英文(A、J、Q、K)").split())
ans = ['1','2','3','4','5','6','7','8','9','10','11','12','13','A','J','Q','K']
anss = [1,2,3,4,5,6,7,8,9,10,11,12,13,1,11,12,13]

a=0
for i in range(len(poker)):
    for j in range(len(ans)):
        if poker[i] == ans[j]:
            a = a + anss[j]
print(a)