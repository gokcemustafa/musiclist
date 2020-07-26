#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


df_raw=pd.read_csv(r'./exhibitA-input.csv', sep='\t')


# In[3]:


df_raw.head()


# In[4]:


df=df_raw[['SONG_ID','CLIENT_ID','PLAY_TS']]


# In[5]:


df.head()


# In[6]:


df['PLAY_TS'] = df['PLAY_TS'].str.slice(0, 10)


# In[7]:


df.head()


# In[8]:


df_grp=df.groupby(['PLAY_TS','CLIENT_ID']).nunique()['SONG_ID'].values


# In[9]:


cnt=0
searchval=346

for val in df_grp:
    if val == searchval:
        cnt += 1

print (cnt)


# In[10]:


df_grp.max()


# In[ ]:




