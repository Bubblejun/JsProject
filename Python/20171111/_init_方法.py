#!/usr/bing/python
#coding=utf-8
# _*_ coding : utf-8 _*_

#创建一个类
class aniamal():
    #初始化对象
    def __init__(self,new_name,new_age,new_aet):
        # print("这是初始化的对象")
        self.name = new_name
        self.age = new_age
    def eat(self):
        print ("eat something!")
    def drink(self):
        print ("drink something!")
    def intrdouce(self):
        print ("%s的年龄是:%d"%(self.name,self.age))
#创建一个对象
dog = aniamal("秋天",10)
#调用dog指向的对象中的方法
dog.eat()
dog.drink()
#给tom指向的对象添加2个属性
#dog.name = "qiutian"
#dog.age = 5
dog.intrdouce()
#print ("%s的年龄是:%d"%(dog.name,dog.age))

cat = aniamal("蓝猫",6)
cat.eat()
cat.drink()
#cat.name = "汤姆"
#cat.age = 6
cat.intrdouce()
