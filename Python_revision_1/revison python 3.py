#!/usr/bin/env python
# coding: utf-8

# In[1]:


def add(a,b):
    print(a+b)


# In[2]:


print(add(5,12))


# In[3]:


def add(a,b):
    return a+b


# In[4]:


print(add(5,12))


# In[33]:


def make_upper(a):
    return a.upper()
print(make_upper('moon'))
    


# In[34]:


def reverse_string(d):
    return d [-1::-1]
print(reverse_string("hello"))


# In[35]:


def power_of(a,b):
    return a**b
print(power_of(5,3))


# In[ ]:





# In[41]:


def odd_or_even(n):
    if n%2==0:
        return "even"
    else:
        return "odd"
print(odd_or_even(22))


# In[44]:


def case_by_len(s):
    if len(s)%2!=0:
        return s.upper()
    else:
        return s.lower()
print(case_by_len("abc"))
print(case_by_len("ABC"))


# In[49]:


def is_it_integer(a):
    if type(a) is int:
        return True
    else:
        return False
print(is_it_integer(123))
print(is_it_integer(1.234))
print(is_it_integer("1234"))


# In[50]:


def is_it_integer(a):
        return type(a) is int
print(is_it_integer(123))
print(is_it_integer(1.234))
print(is_it_integer("1234"))


# In[51]:


l3=[1,"sad",1.234,(1,2,3),4,8.88]
list(filter(is_it_integer,l3))


# In[55]:


def palindrome(s):
    if s==s[-1::-1]:
        return f"{s}is a palindrome"
    else:
        return f"{s} is not a palindrome"
    
l4=["abcd",'abcda',"motor","madam","malayalam"]
list(map(palindrome,l4))


# In[61]:


def factorial(n):
    f = 1
    for i in range(n,0,-1):
        f=f*i
    return f
l5=[0,1,2,3,4,5,6,7]
list(map(factorial,l5))
    


# In[ ]:


# using recurison


# In[62]:


def factorial(n):
    if n<=1:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))


# In[42]:


l1=[1,2,3,4,5,6,7]
list(map(odd_or_even,l1))


# In[43]:


l2=["a","b","dinesh","king"]
list(map(len,l2))


# In[65]:


n=5
a,b=0,1
print(a)
print(b)
for i in range(1,n):
    c=a+b
    print(c)
    a=b
    b=c


# In[66]:


l1=[0,1]
n=10
for i in range(2,10):
    l1.append(l1[i-2]+l1[i-1])
print(l1)


# In[68]:


def string_summary(s):
    capital_count = 0
    small_count = 0 
    vowel_count = 0
    consonant_count = 0
    for i in s:
        if i.isupper():
            capital_count+=1
        elif i.islower():
            small_count+=1
        if i in "aeiouAEIOU":
            vowel_count+=1
        elif i.isalpha():
            consonant_count+=1
    print(f"capital:{capital_count}\nsmall:{small_count}")
    print(f"vowels:{vowel_count}\nconsant:{consonant_count}")
    


# In[69]:


string_summary("Welcome To Python Programming!")


# In[ ]:


a="5"
print(id(a))
a= a*5


# In[71]:


def unique_list(l1):
    return (list(set(l1)))
print(unique_list([1,2,3,2,1,1,4,5,5,7,8,9]))


# In[73]:


def unique_list(l1):
    op_list=[]
    for i in l1:
        if i not in op_list:
            op_list.append(i)
    return op_list
print(unique_list([1,2,3,2,1,1,4,5,5,7,8,9]))
    


# In[94]:


l1=[1,2,4,2,7,4,3,2,5]


# In[103]:


def square_sort(w1):
    w1=list(map(lambda x: x**2,w1))
    w1.sort()
    return w1
print(square_sort([1,2,4,2,7,4,3,2,5]))


# In[99]:


l=[1,2,4,2,7,4,3,2,5]
list(map(lambda x: x**2,l))
e=sorted(l)
e


# In[106]:


def sort_colors(s):
    l1.split('-')
    l1.sort()
    return '-'.join(l1)
print(sort_colors('red-green-blue-yellow-orange-brown'))


# In[159]:


p=[i for i in range(2001,2050) if i%4==0]
p
    


# In[ ]:


#19) create the following dictionaries emp_data


# In[160]:


k1=['city','headcount','seats']
k2=[["chennai","pune",'banglore','mumbai','mysore','coimbatore'],[25000,10000,30000,25000,15000,8000],
    [28000,10000,30000,25000,15000,8000]]

li={i:j for i,j in zip(k1,k2)}
li


# In[161]:


w1=["city","state","buildings"]
w2=["chennai","pune",'banglore','mumbai','mysore','coimbatore']
w3= ['TN','MH','KA','MH','KA','TN']
w4=[10,2,4,6,9,8]
oo={i:j for i,j in zip(w1,[w2,w3,w4])}
oo


# In[162]:


import pandas as pd


# In[163]:


emp_data=pd.DataFrame(li)
emp_data


# In[164]:


df2=pd.DataFrame(oo)
df2


# In[165]:


emp_data.head(3)


# In[166]:


emp_data.iloc[0:3,0:2]


# In[167]:


df2["state"].unique()


# In[168]:


emp_data[['headcount','seats']].sum()


# In[169]:


emp_data.merge(df2)


# In[170]:


emp_data[emp_data["city"].apply(lambda x: x[0].lower()=='m')]


# In[ ]:


emp_data[emp_data.city.apply(lambada x : x[0].lower()=='m')]


# In[ ]:


emp_data[emp_data.city.str.startswith('m')]


# In[ ]:


emp_data[emp_data.city.str.get(0)=="m"]


# In[151]:


d['occupation'=]


# In[171]:


emp_data.groupby("state")[["headcount","seats"]].sum()


# In[1]:


emp_data[(emp_data["seats"].apply(lambda x:x%2000==0))&(emp_data["occupation"].apply(lambda x:x<1))]


# In[ ]:


emp_data[(emp_data.seats%2000==0)&(emp_data.occupation<1)]


# In[ ]:


emp_data.city.str.


# In[ ]:


emp_data.city.str.


# In[ ]:


pd.pivot_table(df2,index="state",values=["headcount",'seats'].aggfunc="sum")


# In[ ]:


df.sort_values(by="occupation",ascending=False)


# In[ ]:


comp_df['seats_needed']=comp_df["headcount"]-comp_df["seats"]


# In[ ]:


comp_df["seats_needed"][comp_df["seats_needed"]<0]=0


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




