#!/usr/bin/env python
# coding: utf-8

# In[242]:


import re
def function_renamer(code):
    d = {}
    ind = 0
    match = re.findall(r'def ([\w]+)', code)
    match.sort()
    for words in match:
        if words[0] == "_":
            code_n = code.replace(str(words.lstrip('_')), "".join(words.title().split("_")))   
        elif '_' in words[1:]:
            code_n = code.replace(words, "".join(words.title().split("_")))
        else:
            words = words
            
    match1 = re.findall(r'def ([\w]+)', code_n)
    match1.sort()
    for i in match:
        d[i] = {'hash' : hash(i), 'camelcase': match1[ind], 'allcaps' : i.upper()}
        ind+=1
        
    print(d,"\n", code_n)


# In[244]:


code='''
def _major_split(*args):
    return (args[:2], args[2:]) 
    
def CheckTruth(t = True):
    print(’t is’, t)
    return _major_split([t]*10)   
    
x, y = _major_split((10, 20, 30, 40, 50))
CheckTruth(len(x) == 10)
'''

code1 ='''
def add_two_numbers(a, b):
    return a + b
    
print(add_two_numbers(10, 20))
'''

function_renamer(code)
