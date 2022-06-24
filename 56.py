a = input("請輸入一個正整數(<10):")
if int(a) <= 10 :
    for i in range(int(a)):
        for j in range(i+1):
            print((i+1)*(j+1),end=' ')
        print()
else:
    print("輸入數字超過10")