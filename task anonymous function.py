#!/usr/bin/env python
# coding: utf-8

# In[4]:


l=[1,2,3,4,5]
a=list(map(lambda x:x**2,l))
print(a)


# In[5]:


a=list(map(lambda x:x%2==0,l))
print(a)


# In[9]:


#1 to 20 numbers square using map and filter
for i in range(1, 21):
    x=lambda i:i**2
    print(x(i))


# In[19]:


l1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
y=list(map(lambda p:p**2,l1))
print(y)


# In[25]:


l1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
x=list(filter(lambda i:i%2==0,l1))
print(x)


# In[ ]:




