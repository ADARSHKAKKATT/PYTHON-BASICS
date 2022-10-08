#!/usr/bin/env python
# coding: utf-8

# # Pattern

# In[ ]:


n=5
for i in range(0,n):
    for j in range(0,i+1):
        print("*",end=" ")
    print("\r")
    


# In[ ]:


for i in range(n,0,-1):
    for j in range(0,i-1):
        print("*",end=" ")
    print("\r")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


for i in range(0,n):
    for j in range(0,i):
        print("*",end="")
    


# In[ ]:


n = 5
k = 2 * n - 2
for i in range(0, n):
    for j in range(0, k):
        print(end=" ")
    k = k - 2
    for j in range(0, i + 1):
        print("* ", end="")
    print("\r")


# In[ ]:


n=5
for i in range(0,n):
    for j in range(0,i+1):
        print("*",end=" ")
    print("\r")
    


# In[ ]:


for i in range(n,0,-1):
    for j in range(0,i-1):
        print("*",end=" ")
    print("\r")


# In[31]:


n=6
for i in range(0,n):
    for j in range(0,i+1):
        print("*",end=" ")
    print("\r")
for i in range(n,0,-1):
    for j in range(0,i-1):
        print("*", end=" ")
    print("\r")


# In[29]:


for i in range(1,11):
    for j in range(1,i+1):
        print(j,end=" ")
    print("\r")


# In[23]:


for i in range(0,11):
    for j in range(0,i+1):
        print(i+j,end=" ")
    print("\r")


# In[21]:


for i in range(1,11):
    for j in range(1,i+1):
        print(i,end=" ")
    print("\r")


# In[ ]:


for i in range(10,1,-1):
    for j in range(0,i-1):
        print(i, end=" ")
    print("\r")


# In[ ]:


for i in range(0,11):
    for j in range(0,i+1):
        print(i,end=" ")
    print("\r")
for i in range(10,0,-1):
    for j in range(0,i-1):
        print(i, end=" ")
    print("\r")


# In[ ]:


for i in range(1,11):
    for j in range(1,i+1):
        print(j,end=" ")
    print("\r")


# In[20]:


#reverse pyramid
num=5
for i in range(1,(num+1)):
    print(" "*(num-i)+ " * " * i)


# In[17]:


totrow=int(input())
for row in range(1,(totrow+1)):
    for space in range(1,(totrow-row)+1):
        print(" ",end=" ")
    print()


# In[ ]:




