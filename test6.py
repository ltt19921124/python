#for循环主要用于遍历/循环 序列或者集合、字典中，组概念的数据都可以用for循环，遍历----for循环。
# 定义一个序列
c = 3
a = [['apple','orange','banana','grape'],[1,2,3]]

for x in a:
    if 'banana' in x:
        break
    for y in x:
            if y == 'orange':
                    break
            print(y)
else:
    print('fruit is gone') #什么时候执行else语句，当元素遍历结束的时候执行。
