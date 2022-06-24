a = ('紅豆生南國春來發幾枝願君多采擷此物最相思')
b = ('春眠不覺曉處處聞啼鳥夜來風雨聲花落知多少')
ans = ''
for i in range(20):
    for j in range(20):
        if a[i] == b[j]:
            if a[i] not in ans:
                ans+=a[i]
print(ans)