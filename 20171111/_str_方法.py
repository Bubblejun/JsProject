#!/usr/bing/python
#coding=utf-8
# _*_ coding : utf-8 _*_

#创建一个类
class aniamal():
    #初始化对象
    def __init__(self,new_name,new_age):
        # print("这是初始化的对象")
        self.name = new_name
        self.age = new_age
    def __str__(self):
        # return "哈哈"
        return ("%s的年龄是:%d"%(self.name,self.age))
    #__str__这个方法用来获取对象的描述信息
    def eat(self):
        print ("eat something!")
    def drink(self):
        print ("drink something!")
    def intrdouce(self):
        print ("%s的年龄是:%d"%(self.name,self.age))

#创建一个对象
dog = aniamal("秋天",10)
cat = aniamal("蓝猫",6)

print (dog)
print (cat)

