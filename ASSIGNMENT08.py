#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().run_line_magic('pinfo', 'PyInputPlus')


# In[ ]:


ANSWER:pyInputPlus is not included in the python standard library
    


# In[ ]:


get_ipython().run_line_magic('pinfo', 'pypi')


# In[ ]:


ANSWER:it is an alias of PyInputPlus 


# In[ ]:


3. How do you distinguish between inputInt() and inputFloat()?

ANSWER:inputInt()accepts the integer value and returns the integer value whereas inputFloat() accepts the numeric value of number and retus the same numeric value
# In[ ]:


4. Using PyInputPlus, how do you ensure that the user enters a whole number between 0 and 99?


# In[ ]:


pypi.inputint(min=1,max=100)


# In[ ]:


get_ipython().run_line_magic('pinfo', 'blockRegexes')


# In[ ]:


ANSWER:We can also use regular expressions to specify whether an input is allowed or not. The allowRegexes and blockRegexes
keyword arguments take a list of regular expression strings to determine what the PyInputPlus function will accept or reject as valid input


# In[ ]:


get_ipython().run_line_magic('pinfo', 'do')


# In[ ]:


ANSWER:the function will raise retrylimit exception error


# In[ ]:


7. If blank input is entered three times, what does inputStr(limit=3, default=&#39;hello&#39;) do?


# In[ ]:


ANSWER:if we use default value the it will not raise exception and it try to print the default value

