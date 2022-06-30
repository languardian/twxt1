n=int(input('輸入筆數'))

dict={}

for i in range(0,n):
    a=input(i+1).split(' ')
    dict[a[0]]=a[1]

find=input('輸入欲查詢單字:')
print(find+'中文意思為'+dict.get(find))