# import test10 as tf
# from test10 import Student

# student = Student() 
# student.do_homework()
# student.print_file()
# a = student.__init__()
# print(a)
# print(type(a))
c = 50

# def add(x,y):
#      c = x + y
#      print(c)

# add(1,2)
# print(c)

class Student():
    sum = 0
    name = 'qiyue'
    age = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__class__.sum += 1
        print('当前班级学生总数为：' + str(self.__class__.sum))
    def do_homework(self):
        print('do homework')

student1=Student('小明', 18)
student1=Student('小明', 18)
student1=Student('小明', 18)
student1=Student('小明', 18)

