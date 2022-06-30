a=input("輸入一串小寫英文")
print(len(a))

for i in range(len(a)):
    a=a.replace("a",".")
    a=a.replace("e",".")  
    a=a.replace("i",".")
    a=a.replace("o",".")  
    a=a.replace("u",".") 

print(a)