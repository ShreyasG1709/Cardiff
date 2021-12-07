#!/usr/bin/env python
# coding: utf-8

# In[61]:


def isGreaterThan(dict1,dict2):   
    counter = 0
    if len(dict1) == len(dict2) and dict1.keys() == dict2.keys():
        for i in range(len(dict1)):
            if list(dict1.values())[i] > list(dict2.values())[i]:
                counter = 1
            elif list(dict1.values())[i] < list(dict2.values())[i]:
                counter = 0
            else:
                if counter == 1:
                    counter = 1
                else:
                    counter = 0  
    else:
        x = set(dict1).intersection(set(dict2))
        if len(x) == 0:
            counter = 0      
        else:
            for i in range(len(dict1)):
                if list(dict1.keys()) not in list(dict2.keys()):
                    if list(dict1.values()) >= list(dict2.values()):
                        counter = 1
                    else:
                        counter = 0
                
                
    if counter == 1:
        return True
    else:
        return False
    
dict1={'a':1,'b':1}
dict2={'c':0,'d':0}
isGreaterThan(dict1,dict2)
.................................................

dict1={'a':1,'b':2, 'c':-10}
dict2={'a':1,'b':1}
#dict1={'a':1,'b':1}
#dict2={'c':0}
x = set(dict1).intersection(set(dict2))
print(x, type(x))

