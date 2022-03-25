#列表增删改查#
import copy

heros = ["iron man", "green"]
heros.append("black")
#append方法一次只能添加一个元素#
heros.extend(["1","2","3"])
#extend一次可以添加多个#
s = [1,2,3,4,5]
s[len(s):] = [6]
print(s)
s[len(s):] = [7,8,9]
print(s)
#insert在列表中插入数，语法为insert(插入位置，插入的数)#
s.insert(0,0)
print(s)
#remove方法可以删除列表中得元素
#当列表中有多个相同元素时，他只会删除第一个
# 如果列表中没有，那么报错#
heros.remove("green")
print(heros)
#pop删除特定位置的方法
heros.pop(1)
print(heros)
#clear清除列表中全部元素
heros[1] = "dog"
#替换元素内容
heros[3:] = ["q","w","e"]
print(heros)
#1.将赋值号（=）左边指定内容删除
#2.将包含在赋值号（=）右边的可迭代对象中片段插入左边被删除的位置#
nums = [3,5,6,7,8,3]
#将nums里面的元素按大小排序
# sort从小到大
# reverse从大到小#
nums.sort()
print(nums)
nums.reverse()
print(nums)
nums = [3,5,6,7,8,3,2]
nums.sort(reverse=True)
#查找列表中有多少个元素#
nums.count(3)
#查找列表中元素索引
nums.index(2)
#index(x,start,end)查找指定位置的元素值
nums.index(3,1,4)
nums_copy1 = nums.copy()
print(nums_copy1)
nums_copy2 = nums[:]
print(nums_copy2)
#列表乘法，就是将二者合并
s=[1,2,3]
t=[4,5,6]
print(s+t)
matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
for i in matrix:
    for each in i:
        print(each,end = '')
print(matrix(0))
#is 运算符 检测元素地址是否相同
x=[[1,2,3],
   [4,5,6],
   [7,8,9]]
#y=x.copy()
#print(x)
#int(y)
#浅拷贝和深拷贝
y= copy.deepcopy(x)
#列表推导式
oho = [1,2,3,4,5]
oho = [i*2 for i in oho]
print[oho]
#[expression for targrt in iterable]
matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]

col2 = [row[1]for row in matrix]
diag = [matrix[i][i]for i in range(len(matrix))]
print(diag)
diag = [matrix[i][2-i]for i in range(len(matrix))]
#
even = [i for i in range(10) if i%2==0]
