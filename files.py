#!/usr/bin/env python
# coding: utf-8

# In[2]:


f=open("demo.txt","x")
f.close()
f=open("demo.txt","r")
f.close()


# In[5]:


f=open("demo.txt","w")
f.write("anu")
f.close()


# In[7]:


f=open("demo.txt","r")
f.read()


# In[8]:


f.close()


# In[13]:


f=open("demo.txt","a")
f.write("hai")
f.close()


# In[21]:


f=open("demo.txt","r")
f.readline()
f.close()


# In[31]:


f=open("demo.txt","r")
f.readline()
f.readline()
f.readline()
f.readline()
f.readline()
f.readline()


# In[ ]:




