#!/usr/bin/env python
# coding: utf-8

# In[9]:


def pluralize(s):    
    a = {}
    words = []
    with open('eg.txt') as f:
        for line in f:
            words.append(line.strip())
        if s.lower() in words:
            a = {"plural": s , "status" : "Proper_Noun"}
            return a
        elif s == '':
            a = {"plural": "" , "status" : "Empty_String"}
            return a
        elif s[-1] == 's':
            a = {"plural": s , "status" : "already_in_plural"}
            return a
        else:
            if s[-1] in 'a,e,i,o,u':
                s = s + 's'
                a = {"plural": s , "status" : "already_in_plural"}
                return a
            elif s[-1] in '0,1,2,3,4,5,6,7,8,9':
                a = {"plural": s , "status" : "ending_with_number"}
                return a
            elif s[-1] == 'y' and s[-2] not in 'a,e,i,o,u':
                s=s.replace(s[-1], 'ies')
                a = {"plural": s , "status" : "success"}
                return a
            elif s[-1] == 'f' and s not in words:
                s=s.replace(s[-1], 'ves')    
               # a["plural"] = s
                #a["status"] = "success"
                a = {"plural": s , "status" : "success"}
                return a
            elif s[-2:] in 'sh , ch, z':
                s = s + 'es'
                a = {"plural": s , "status" : "success"}
                return a
            else:
                s+='s'
                a = {"plural": s , "status" : "success"}
                return a
    pass


# In[10]:


TEST_CASES = """failure
food
Zulma
injury
elf
buzz
computers
PCs

highway
presentation
pouch
COVID-19
adam""".split('\n')

if __name__ == '__main__':

  for test_noun in TEST_CASES:

    print(test_noun,'-->',pluralize(test_noun))
    print('----')


