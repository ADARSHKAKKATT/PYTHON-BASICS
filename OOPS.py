#!/usr/bin/env python
# coding: utf-8

# # class

# In[2]:


class student:
    def __init__(self,name,age):
        self.names=name
        self.ages=age
    def display(self):
        print("My name is {}".format(self.names))
        print("My Name is ",self.names)
    def sing(self,song):
        self.song=song
        print('the song is {}'.format(self.song))
    
            
            
obj=student("Adarsh",24)
obj.display()
obj.sing('happy')


# In[4]:


class vehicle:
    def __init__(self):
        print("Print vehicle")
    def wheel(self):
        print("Vehicle has wheel")
class car(vehicle):
    def color(self):
        print("color is red")
        
obj=car()
obj.wheel()
obj.color()
        


# In[ ]:




