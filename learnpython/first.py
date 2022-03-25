""""用python设计第一个游戏"""
import random
counts = 3
Random = random.randint(1,10)
while counts > 0:
    temp = input("不妨猜一下小甲鱼现在心里想的是哪个数字")
    guess = int(temp)
    if guess == Random:
        print("你是小甲鱼心里的蛔虫吗")
        print("猜对了也没奖励")
        break
    else:
        if guess < Random:
            print("小啦")
        else:
            print("大啦")
    counts = counts - 1
print("游戏结束，不玩啦")
score=66
level=('D'if 0 <=score <60 else
       'C'if 60 <=score <80 else
       'B'if 80 <=score <90 else
       'A'if 90 <=score <100 else
       'S'if score == 100 else
       "请输入1-100之间的分值")
#求10以内的素数#
for n in range(2,10):
    for x in range(2,n):
        if n%x ==0:
            print(n,"=","*",n//x)
            break
    else:
        print(n,"是一个素数")
        array=[1,2,3,4,5,'上山打老虎']
        for each in array:
            print(each)
    lenth = len(array)
    print(array[lenth-1])
    print(array[0:3])