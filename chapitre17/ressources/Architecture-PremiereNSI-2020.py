#!/usr/bin/env python
# coding: utf-8

# In[1]:


import dis


# In[2]:


help(dis)


# ## Exercice 2

# In[3]:


import dis 

code_source = """
a = 5
a = a + 3
"""

dis.dis(code_source)


# In[4]:


list(dis.get_instructions(code_source))


# In[5]:


code = compile(code_source, '<string>','exec')
for octet in code.co_code:
    print(octet, end = ' ')


# ## Boucle en assembleur

# In[1]:


code_ascii = 32
while code_ascii < 127:
    print(chr(code_ascii), end =' ')
    code_ascii = code_ascii + 1
print()

