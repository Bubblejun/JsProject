#!/usr/bing/python
#coding=utf-8
# _*_ coding : utf-8 _*_

#创建一个类
class aniamal():
    def eat(self):
        print ("eat something!")
    def drink(self):
        print ("drink something!")
#创建一个对象
dog = aniamal()
#调用dog指向的对象中的方法
dog.eat()
dog.drink()
#给tom指向的对象添加2个属性
dog.name = "qiutian"
dog.age = 5

print ("%s的年龄是:%d"%(dog.name,dog.age))
