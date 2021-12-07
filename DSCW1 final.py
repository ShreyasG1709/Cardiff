#!/usr/bin/env python
# coding: utf-8

# In[1]:


def do_arithmetic(a , b, op):
    if(op=='add' or op =='+'):
        return(float(a+b))
    elif(op=='subtract' or op =='-'):
        return(float(a-b))
    elif(op=='multiply' or op =='*'):
        return(float(a*b))
    elif(op=='divide' or op =='/'):
        if(a==0 or b==0):
            print("Division by 0!")
        else:
            return(float(a/b))
    elif op == '':
        return(float(a+b))
    else:
        return("Unknown operation")


# In[2]:


do_arithmetic(5,3,'')


# In[3]:

def sum_of_digits(s):
    num = [z for z in s if z.isdigit()]
    word = [z for z in s if not z.isdigit()]
    if s == '':
        print("Empty string entered!")
        return 0
    else:
        if(len(list(num)) == 0):  
            print("The sum of digits operation could not detect a digit!, \nThe returned input letters are:", list(word))
            return 0
        else:
            print("The sum of digits operation performs ", end='')
            print(*num, sep = "+") 
            print("The extracted non-digits are:", list(word))
            g = 0
            for ele in num:
                g = g + int(ele)
            return(g)
            
    pass


# In[4]:


sum_of_digits('abc-134')


# In[5]:


if __name__ == '__main__':
    testcases = {'do_arithmetic': [(24, -7, 'add'), (6, 6, 'multiply'), (4, 0, '/'), (3, 9, '-')],
    'sum_of_digits':[("123",), ("we10a20b",), ("united",), ("",)]}
    
    print('\n-- do_arithmetic testcases --')
    for args in testcases['do_arithmetic']:
        print('input:', str(args))
        print('output:', do_arithmetic(*args))
        print('-----------')
    
    
    print('\n-- sum_of_digits testcases --')
    for args in testcases['sum_of_digits']:
        print('input:', str(args))
        print('output:', sum_of_digits(*args))
        print('-----------')


# In[ ]:





# In[ ]:




