# -*- coding: utf-8 -*-

d={}
while True:
    print('功能->')
    print('1:單字')
    print('2:輸出字典裡的內容')
    print('3:查字典(英翻中)')
    print('4:查字典(中翻英)')
    print('5:離開系統')
   
    A=int(input('欲使用的功能?'))
    if A==1:
        num=input('多少個單字?')
        for i in range(int(num)):
            
            a=input('英文')                                                                                                   
            b=input('中文')
            d[a]=b
    if A==2:
        print(d)
    if A==3:
        c=input('查甚麼字?(英文)')
        if c==a:
            print(b)
    if A==4:
        D=input('查甚麼字?(中文)')
        if b==D:
            print(a)
    if A==5:
        break

for k,v in d.items():
    score=0
    print(v,':')
    ans=input()
    if ans==k:
        score+=1
        print()




















