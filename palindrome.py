#!/usr/bin/env python
# coding: utf-8

# In[4]:


def ispalindrome(s):
             
    rev = ''.join(reversed(s))
     
    if (s == rev): 
        return True
    return False
  

s = str(input("Please enter a word to check whether it is palindrome or not \t"))
ans = ispalindrome(s) 
  
if (ans): 
    print("Yes") 
else: 
    print("No") 


# In[ ]:




