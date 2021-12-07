#!/usr/bin/env python
# coding: utf-8

# In[9]:


def freeFall(val,isD):
    g = 9.81
    if isD in ("True","true"):
        d = val
        t = round((2*d/g)**(0.5), 2)
        return t
    else:
        t = val
        d = round((0.5*g*t*t),2)
        return d

val = float((input("Input value")))
tf = input("True/False?")
print(val,tf)
freeFall(val,tf)


# In[10]:


def RPS(s):
    dictionary = {'R':'P', 'P':'S', 'S':'R'}
    transt = s.maketrans(dictionary)
    s = s.translate(transt)
    return s

RPS('PRSPRR')


# In[11]:


def lts(s):
    s = str(s)
    rem = s.maketrans(' ',' ',",'")
    s=s.translate(rem)
    #print(s)
    s = "".join(s.split())
    return s

lts(['a',['b','c']])


# In[12]:


def textPreprocessing(s):
    final = []
    sw = ('i', 'a', 'about', 'am', 'an', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'how', 'in', 'is', 'it', 'of', 'on','or', 'that', 'the', 'this', 'to', 'was', 'what', 'when', 'where', 'who', 'will', 'with')
    rem = s.maketrans(' ',' ',"(.?)!,:;-[']{}")
    s=s.translate(rem)
    #print(s)
    s = (s.lower().split()) 
    print(s)
    for words in list(s):
        if words in sw:
            s.remove(words)
    #print(s)
    for word in list(s):
        if word[-1]== 's':
            word = word.replace("s","")
            final.append(word)
        elif word[-2:] == 'ed':
            word = word.replace("ed","")
            final.append(word)
        elif word[-3:] == 'ing':
            word = word.replace("ing","")
            final.append(word)
        else:
            final.append(word) 
    return list(final)

textPreprocessing('I am thinking, therefore I am.')


# In[ ]:





# In[ ]:




