#!/usr/bin/env python
# coding: utf-8

# In[2]:


# change this value for a different result
# nterms = 1000


nterms = int(input("How many terms? "))


def fib2(nterms):
# first two terms
    n1 = 0
    n2 = 1
    count = 0

# check if the number of terms is valid
    if nterms <= 0:
        
        print("Please enter a positive integer")
    elif nterms == 1:
        print("Fibonacci sequence upto",nterms,":")
        print(n1)
    else:
        
    
         print("Fibonacci sequence upto",nterms,":")
    while count < nterms:
        
        print(n1,end=' , ')
        nth = n1 + n2
       # update values
        n1 = n2
        n2 = nth
        count += 1
fib2(nterms)

# In[ ]:




