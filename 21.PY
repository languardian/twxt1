student = ['123','456','789','321','654']
name = ['Tom','Cat','Nana','Lim','Won']
cla = ['DTGT','CSIE','ASIE','DBA','FDD']
a = str(input("輸入查詢學號為:"))
for i in range(5):
    if a == student[i]:
        print(str(student[i])+str(name[i])+str(cla[i]))