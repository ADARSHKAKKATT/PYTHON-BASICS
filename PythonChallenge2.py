#!/usr/bin/env python
# coding: utf-8

# # python function

# In[ ]:


def string(s1,s2):
    a=len(s1)
    b=len(s2)
    if a>b:
        print(s1)
    elif (a<b):
        print(s2)
    else:
        print(s1)
        print(s2)
        
    
    
        
        
string("amal","Akhil")


# In[ ]:


def oddeven(p):
    if (p%2==0):
        print("It is even number")
    else:
        print("It is odd number")
        
        
oddeven(12)


# In[ ]:


def dicts():
    d=dict()
    d[1]=1
    d[2]=2**2
    d[3]=3**2
    print(d)
dicts()
    


# In[ ]:


def dictt():
    q=dict()
    for i in range(1,21):
        q[i]=i**2
    print(q)
    
dictt()


# In[ ]:


def dictval():
    r=dict()
    for i in range(1,21):
        r[i]=i**2
    print(r.values())
    
    
dictval()


# # python basic challenge

# In[ ]:


t1=(1,2,3,4,5,6,7,8,9,10)
print(t1[5:])
print(t1[:5])


# In[ ]:


l=[]
for i in t1:
    if(i%2==0):
        l.append(i)
t=tuple(l)
print(t)


# In[ ]:


a=input()
if (a=="yes" or a=="YES" or a=="Yes"):
    print("Yes")
else:
    print("No")


# In[ ]:


ls=[1,2,3,4,5,6,7,8,9,10]
a=list(filter(lambda x:(x%2==0),ls))
print(a)


# In[ ]:


a=list(map(lambda x:(x*x),ls))
print(a)


# In[ ]:


l2=[1,2,3,4,5,6,7,8,9,10]
b=list(map(lambda x:x**2,filter(lambda x:x%2==0,l2)))
print(b)


# In[ ]:


l3=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
a=list(filter(lambda y:y%2==0,l3))
print(a)


# In[ ]:


a=list(map(lambda x:x*2,l3))
print(a)


# # python challenge2

# In[2]:


l=[1,2,'hai',2.3]
l[2]


# In[ ]:


l1=[9,8,7,6,5,4,3,2,86,34]
l1[2:7]


# In[ ]:


t=(5,6,7,8,9,3,2,4)
l2=list(t)
print(l2)


# In[ ]:


l2.append(77)
print(l2)


# In[ ]:


l2.insert(2,33)
print(l2)


# In[ ]:


s=set([1,2,3,4,5,6,7])
print(s)


# In[ ]:


s.add(8)
print(s)


# In[ ]:


s.remove(4)
print(s)


# In[ ]:


#BMI Calculator
def bmi(w,h):
    print(w/(h/100)**2)
    
bmi(60,163)


# # python challenge1

# In[ ]:


for i in range(2000,3200+1):
    if i%7==0 and i%5!=0:
        print(i)


# In[ ]:


a=int(input("Enter the limit: "))
lst={}
for i in range(1,a+1):
    lst[i]=i*i
print(lst)


# In[ ]:


v=input("Enter comma sepparated numbers: ")
list=v.split(",")
tuple=tuple(list)
print(list)
print(tuple)


# In[ ]:


a=input()
b=input()
print(a.upper())
print(b.upper())


# In[3]:


p=input("Enter comma sepparated words")
q=p.split(",")
q.sort()
print(q)


# In[ ]:




