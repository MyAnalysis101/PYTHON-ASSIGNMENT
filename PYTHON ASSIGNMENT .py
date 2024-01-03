#!/usr/bin/env python
# coding: utf-8

# # DATA CLEANING AND ANALYZING USING Panda

# In[ ]:





# In[1]:


import pandas as pd
df = pd.read_csv('boat_data.csv')
df.head()


# In[2]:


df["Price"].max()


# In[7]:


df['Number of views last 7 days'].max()


# In[8]:


df['Number of views last 7 days'].min()


# In[9]:


df.info()


# In[10]:


df.isnull().sum()


# In[11]:


df.columns


# In[24]:


df['Manufacturer'].unique()


# In[25]:


df['Boat Type'].unique()


# In[32]:


df['Location'].unique()


# In[33]:


df['Material'].unique()


# In[49]:


df['Manufacturer'].value_counts()


# In[27]:


df['Boat Type'].value_counts()


# In[34]:


df['Location'].value_counts()


# In[28]:


df['Length'].max()


# In[29]:


df['Length'].min()


# In[30]:


df['Width'].max()


# In[31]:


df['Width'].min()


# In[37]:


df[df['Width']==4]


# In[38]:


df[df['Location']== 'France']


# In[69]:


df.groupby(["Manufacturer"]).sum().sort_values("Boat Type", ascending=False)


# In[ ]:





# # DATA ANALYZING USING NUMPY and MATPLOTLIB

# In[57]:


import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.plot(x,y)

plt.show()


# In[47]:


import numpy as np
import matplotlib.pyplot as plt

x = np.array(['B_pb', 'J_pb', 'Sun_pb', 'Ps_pb', 'SR_pb', 'AY_pb', 'ISAY_pb', 'Cou_pb', 'PNS_pb', 'Ht_pb'])           
y = np.array([631,537,383,241,239,1,1,1,1,1])

plt.plot(x, y)
plt.title("Boat Company Data")
plt.xlabel("Manufacturer")
plt.ylabel("Number of products")
plt.show()


# In[74]:


import matplotlib.pyplot as plt
import numpy as np
x = np.array(["NET", "CRO", "ITA", "FRA", "SPA", "SWI", "SWE"])
y = np.array([304, 244, 328, 152, 2, 2, 1])
plt.plot(x, y)
plt.title("Company Location")
plt.xlabel("Location")
plt.ylabel("Total Number of Boats Sold")
plt.show()


# In[ ]:




