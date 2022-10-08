#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def some(a):
    if (a!=0):
        return a+some(a-1)
    else:
        return a
    
print("sum = ",some(4))


# In[ ]:


#sum of even numbers with argument
def evn(x):
    if(x==0):
        return x   
    elif(x%2==0):
        return x+evn(x-1)
    else:
        return evn(x-1)
            
x=int(input('end= '))
evn(x)


# In[ ]:


#factorial
def fat(f):
    if f==1:
        return 1     
    else:
        return f*fat(f-1)
       
        
    
f=int(input("No. "))
fat(f)


# In[ ]:


def pri(p):
    if p%2==0:
        return p%pri(p-1)
p=int(input())

pri(p)


# In[74]:


x=int(input())
def prm(x):
    f=0
    for i in range(2,x):
        if(x%i==0):
            f=2
            break
    if(f==0):
        print(' prime')
    else:
        print('not prime')
prm(x)


# In[ ]:




