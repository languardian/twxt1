a=int(input("國文"))
b=int(input("英文"))
c=int(input("微積分"))
d=int(input("體育"))
e=int(input("程式設計"))

f=[a,b,c,d,e]
f1=["國文","英文","微積分","體育","逞式設計"]
g=f.copy()
g.sort()
l=f.index(g[0])
l1=f.index(g[-1])
r=(a+b+c+d+e)/5

print("平均分數{:.2f}".format(r))
print("最高分科目%s%d分"%(f1[l1],g[-1]))
print("最低分科目%s%d分"%(f1[l],g[0]))