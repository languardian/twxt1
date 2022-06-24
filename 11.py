star = ['無','魔羯','水瓶','雙魚','牡羊','金牛','雙子','巨蟹','獅子','處女','天秤','天蠍','射手','魔羯']
day = [0,20,18,20,20,21,21,22,23,23,23,22,21]
list1 = list(input("輸入月及日為:").split())
for i in range(13):
    if int(list1[0]) == i and int(list1[1]) <= day[i]:
        print(star[i])
    elif int(list1[0]) == i and int(list1[1]) >= day[i]:
        print(star[i+1])