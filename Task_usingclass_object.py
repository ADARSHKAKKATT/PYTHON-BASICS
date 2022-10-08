#!/usr/bin/env python
# coding: utf-8

# In[3]:


class vehicle:
    def __init__(self):
        print("4wheels")
class car(vehicle):
    def color(self):
        print("red color")
        
        
obj=car()
obj.color()
        


# In[4]:


class vehcle:
    pass


# In[2]:


class vehicle:
    def __init__(self):
        print("4wheels")
    def tipe(self):
        print("model of vehicle")
        
class bus(vehicle):
    def color(self):
        print("color is blue")
        


obj=bus()
obj.tipe()
obj.color()


# In[26]:


class bus(vehicle):
    def seating_capacity(self,seating_capacity='seat capacity is 50'):
        print(seating_capacity)
obj=bus()
obj.seating_capacity()


# In[21]:


class travel:
    def __init__(self):
        print("hello")
    def use(self,purpose):
        self.usage=purpose
        print(format(self.usage))
class place(travel):
    def plac(self):
        print("wayanad")
        
        
obj=place()
obj.use("enjoy")
obj.plac()
    


# In[80]:


class teacher:
    def __init__(self):
        print("school")
    def purpose(self,purpose):
        self.purp=purpose
        print(format(self.purp))
class stud(teacher):
    def doing(self):
        print("studying")
        
obj=stud()
obj.purpose("Teaching")
obj.doing()
isinstance(obj,teacher)


# In[ ]:





# In[31]:


class school_bus(vehicle):
    def passengers(self):
        print("Childrens")
        
obj=school_bus()
obj.passengers()


# In[52]:


class printing:
    def usr(self,inputt):
        self.inpt=inputt
        print(type(inputt))
        print(format(self.inpt))
    def prnt(self):
        print("Direct print")
        
obj=printing()
obj.usr("From user")
obj.prnt()


# In[ ]:





# In[ ]:





# In[93]:


#basic calc
class calc:
    def __init__(self):
        print("Calculator")
    def add(self,first,second):
        #print(type(first))
        #print(type(second))
        self.frst=first
        self.scnd=second
        print((self.frst)+(self.scnd))
        
obj=calc()
obj.add(2,3)


# In[63]:


a="123"
print(type(a))
b=int(a)
print(type(b))


# In[14]:


#area of circle
class circle:
    def aria(self,area):
        #print(type(area))
        self.area=area
        #print(area)
        print(3.14*((self.area)*2))
              
obj=circle()
obj.aria(3)
              


# In[15]:


#area of rectangle
class rectangle:
    def rect(self,length,width):
        #print(type(area))
        self.len=length
        self.wid=width
        print((self.len)*(self.wid))
              
obj=rectangle()
obj.rect(2,2)
              


# In[19]:


class animal:
    def anim(self):
        print("Animal")
class dog(animal):
    def dogg(self):
        print("Dog")
class dogchild(dog):
    def child(self):
        print("dog child")
        
        
obj=dogchild()
obj.child()


# In[30]:


class calculation1:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        
class calculation0(calculation1):
    def add(self):
        print(self.a+self.b)       
        
class calculation2(calculation0):
    def mul(self):
        print(self.a*self.b)
class calculation3(calculation2):
    def div(self):
        print(self.a/self.b)
        
obj=calculation3(10,5)
obj.div()
obj.mul()
obj.add()


# In[ ]:




