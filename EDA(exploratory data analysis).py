#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')
sns.set()


# In[5]:


titanic_data=pd.read_csv('https://raw.githubusercontent.com/insaid2018/Term-1/master/Data/Casestudy/titanic_train.csv')
titanic_test=pd.read_csv('https://raw.githubusercontent.com/insaid2018/Term-2/master/Data/test.csv')


# In[6]:


titanic_data.head()


# In[7]:


titanic_test.head()


# In[8]:


titanic_test.info()


# In[ ]:


titanic_test.

