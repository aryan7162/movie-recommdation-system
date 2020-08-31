#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as pld


# In[9]:


ratings = pd.read_csv('Downloads/ml-latest-small/ml-latest-small/ratings.csv')


# In[11]:


ratings.head(10)


# In[13]:


movies = pd.read_csv('Downloads/ml-latest-small/ml-latest-small/movies.csv')


# In[14]:


movies.head(10)


# In[15]:


links = pd.read_csv('Downloads/ml-latest-small/ml-latest-small/links.csv')


# In[16]:


links.head(10)


# In[17]:


ratings.columns


# In[18]:


tags = pd.read_csv('Downloads/ml-latest-small/ml-latest-small/tags.csv')


# In[21]:


tags.head(10)


# In[23]:


movies.columns


# In[24]:


ratings.info()


# In[25]:


movies.info()


# In[29]:


merged_data = pd.merge(ratings,movies)


# In[31]:


merged_data.head(10)


# In[ ]:





# In[ ]:




