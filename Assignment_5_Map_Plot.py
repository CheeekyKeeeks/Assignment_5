#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv('C:\data\AirQualityNo2.csv')


# In[3]:


df.head()


# In[4]:


air_quality = pd.read_csv('C:\data\AirQualityNo2.csv')


# In[5]:


air_quality.plot()


# In[6]:


air_quality["station_paris"].plot()


# In[ ]:




