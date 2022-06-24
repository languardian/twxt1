a = int(input("請輸入所使用的度數:"))

if a <= 120:
    print("Summer months:"+str('{:.2f}'.format(a*2.10,2)))
    print("Non-Summer months:"+str('{:.2f}'.format(a*2.10,2)))
elif a <= 330:
    print("Summer months:"+str('{:.2f}'.format(120*2.10+(a-120)*3.02,2)))
    print("Non-Summer months:"+str('{:.2f}'.format(120*2.10+(a-120)*2.68,2)))
elif a <= 500:
    print("Summer months:"+str('{:.2f}'.format(120*2.10+(330-120)*3.02+(a-330)*4.39,2)))
    print("Non-Summer months:"+str('{:.2f}'.format(120*2.10+(330-120)*2.68+(a-330)*3.61,2)))
elif a <= 700:
    print("Summer months:"+str('{:.2f}'.format(120*2.10+(330-120)*3.02+(500-330)*4.39+(a-500)*4.97,2)))
    print("Non-Summer months:"+str('{:.2f}'.format(120*2.10+(330-120)*2.68+(500-330)*3.61+(a-500)*4.01,2)))
elif a > 700:
    print("Summer months:"+str('{:.2f}'.format(120*2.10+(330-120)*3.02+(500-330)*4.39+(700-500)*4.97+(a-700)*5.63,2)))
    print("Non-Summer months:"+str('{:.2f}'.format(120*2.10+(330-120)*2.68+(500-330)*3.61+(700-500)*4.01+(a-700)*4.50,2)))