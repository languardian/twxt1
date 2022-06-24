b = 0
while True:
    b+=1
    c = input("請輸入事項(若已無事項，請輸入end):")
    if c == 'end':
        break;
    else:
        print(str(b)+"."+str(c))