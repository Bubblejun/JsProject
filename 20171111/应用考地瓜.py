#!/usr/bin/python
#coding = utf-8
# _*_ coding:utf-8 _*_
import time
class fruit:

    def __init__(self):
        self.level = 0
        self.cookString = "sheng de"
        self.zuoliao = []

    def __str__(self):
        return "%s already :%s and Add %s"%(self.name,self.cookString,','.join(self.zuoliao))

    def fire(self,time):
        self.level += time
        if self.level >= 0 and self.level < 3:
            self.cookString = "sheng de"
        elif self.level >= 3 and self.level < 5:
            self.cookString = "ban sehng bu shu"
        elif self.level >= 5 and self.level < 8:
            self.cookString = "shu tou le"
        elif self.level >= 8:
            self.cookString = "hu le e "

    def addZuoLiao(self,zuoliao):
        self.zuoliao.append(zuoliao)

digua = fruit()

digua.name = "xiang jiao"

digua.fire(1)
print digua
digua.fire(1)
digua.addZuoLiao("dasuan")
print digua
digua.fire(1)
digua.addZuoLiao("lajiao")
print digua
digua.fire(1)
digua.addZuoLiao("jiucai")
print digua
digua.fire(1)
print digua

time.sleep(30)