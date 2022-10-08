#!/usr/bin/env python
# coding: utf-8

# In[1]:


l=[1,2,3,4,5]
print(l)


# In[2]:


t=tuple(l)
print(t)


# In[3]:


a=2
b=3
c=4
if (a==b==c):
    print((a+b+c)*3)
else:
    print(a+b+c)


# In[10]:


p="hai"
q="hello"
c=(p+"  "+q)
print(c)


# In[13]:


c.title()


# In[14]:


s1="hello you all"
s1.split()


# In[23]:


def mul():
    l1=[1,2,3]
    a=1
    for i in l1:
        a=a*i
    print("Result of given list is:",a)
    
mul()


# In[19]:


#list given by user

def mul():
    l1=input("no:")
    a=1
    for i in l1:
        a=a*i
    print("Result of given list is:",a)
    
mul()


# In[ ]:


print(end="Enter the Size: ")
numsSize = int(input())

nums = list()
print(end="Enter " +str(numsSize)+ " Elements: ")
for i in range(numsSize):
  nums.append(int(input()))

print(end="\nEnter a Number to Multiply: ")
val = int(input())

newnums = list()
for i in range(numsSize):
  newnums.append(val*nums[i])

print("\nThe New List is:")
for i in range(numsSize):
  print(end=str(newnums[i])+ " ")
print()


# In[8]:


l1=[8,7,6,5]
s1=set(l1)
#com=l1.intersection(l)
print(s1)
s2=set(l)
print(s2)
s=s1.intersection(s2)
print(s)


# In[9]:


firstname="Adarsh"
lastname="Kakkatt"
print(lastname+" "+firstname)


# In[13]:


color_list_1=set(['black','white','violet'])
print(color_list_1)


# In[12]:


color_list_2=set(['violet','indigo','blue','green'])
print(color_list_2)


# In[14]:


color_list_1.difference(color_list_2)


# In[ ]:




