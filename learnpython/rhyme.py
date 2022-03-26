rhyme = (1,2,3,4,5,"上山打老虎")
# 元组定义是也可以不带括号
rhyme = 1,2,3,4,5,"上山打老虎"
print(rhyme[0])
print(rhyme[-1])
#不支持修改，只支持查询
nums = 3,1,8,6,8,3,5,3
print(nums.count(3))
heros = "黑寡妇","绿巨人","蜘蛛侠"
heros.index("黑寡妇")
s = (1,2,3)
t = (1,2,3)
w=s,t
for each in s:
    print(each)
for i in w:
    for each in i:
        print(each)
        s = (1,2,3,4,5)
[each*2 for each in s]
#[2,4,6,8,10]
print((each *2 for each in s))
#??
x=(520,)
print(type(x))
#打包和解包
t = (123,"Fishc",3.14)
print(t)
x,y,z = t
print(x)
print(y)
print(z)
for i in "FishC":
    print(i)
# 字符串
# 判断是否为回文数
x="12321"
"是回文数" if x == x[::-1] else "不是回文数"


