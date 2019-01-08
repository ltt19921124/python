# 面向对象
# 有意义的面向对象的代码
# 类 = 面向对象
# 类的实例化
# 类的最基本作用就是封装代码
# 在模块里定义函数和在类里定义有什么区别？
#     在类中定义的方法(方法)要加self
#     使用变量要加self.",在实际开发中，不建议在一个模块中既定义类又去做类的实例化，以及类中方法的调用，应该把对类的使用放在另外的模块中
# 类的定义：类是现实世界或思维世界中的实体在计算机中的反映，它将数据以及这些数据上的操作封装在一起。
# 对象的行为与特征
# 类只是一类事物的总称，并不是一个具体的集合，具体的对象表示具体的类的一个实例，类的实例化就生成一个对象。


class Student():

    sum = 0
    

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__score = 0

    def marking(self,score):
        if score < 0:
            return '分数不合法，请重新打分'
        self.__score = score
        print(self.name + '同学本次考试分数为:' + str(self.__score))
    
    
    @staticmethod
    def add(x,y):
        print(Student.sum)
        print('This is a static method')

student1=Student('小明', 18)
student2=Student('小兰', 18)
result = student1.marking(59)
student1.__score = -1
print(student1.__score)
print(student2._Student__score)
# print(student1.__dict__)

# print(student2.__score)


