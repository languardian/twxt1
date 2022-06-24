a = (int(input("輸入一數字，輸出菱形(基數):"))+1)/2

for i in range(int(a)+1):
    if i < a:
        for j in range(int(a)-i):
            print(' ',end='')
        for j in range((i*2)+1):
            print('*',end='')
        print() 
    else:
        for i in range(int(a)-1,0,-1):
            for j in range(int(a)-i+1):
                print(' ',end='')
            for j in range((i*2)-1):
                print('*',end='')
            print()



