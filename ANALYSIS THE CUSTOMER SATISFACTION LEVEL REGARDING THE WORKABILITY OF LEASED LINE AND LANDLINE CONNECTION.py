#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import  matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


# In[11]:


project_Wireline = pd.read_excel('F:/Python/Neilson/project data.xlsx')


# In[6]:


project_Wireline.head()


# In[4]:


project_Wireline.info()


# In[7]:


project_Wireline.describe()


# In[8]:


project_Wireline.columns


# In[9]:


project_Wireline.isnull().sum()


# In[10]:


Total_Service = project_Wireline['Service Provider'].value_counts()


# In[132]:


Total_Service


# In[16]:


plt.title('Figure 1: Sample size for different service provider')
sns.countplot(x='Service Provider', data = project_Wireline, hue = 'Service Provider')


# In[18]:


project_Wireline.groupby('Service Provider')['Rating of Brands'].mean()


# In[20]:


plt.figure(figsize =(10,4))
plt.title('Figure 2: Customer Satisfaction level on Service Provider')
sns.barplot(x = 'Service Provider', y = 'Rating of Brands', data = project_Wireline, palette = 'hot', hue = 'Service Provider')


# In[28]:


plt.figure(figsize =(10,6))
plt.title('Figure 3 : Satisfaction level to connect with Sales Account Manager')
sns.barplot(x = 'Service Provider', y = 'Connection with sales manager', data = project_Wireline, hue = 'Service Provider')


# In[29]:


plt.figure(figsize =(10,6))
plt.title('Figure 5 : Satisfaction level to complete negotiation process with Sales Account Manager')
sns.barplot(x = 'Service Provider', y = 'Time taken to complete the negotiation process', data = project_Wireline, palette = 'cool', hue = 'Service Provider')


# In[32]:


project_Wireline.groupby('Service Provider')['Clarity in installation'].mean()


# In[33]:


plt.figure(figsize =(9,6))
plt.title('Figure 5: Customer Satisfaction level on Clarity in installation')
sns.barplot(x = 'Service Provider', y = 'Clarity in installation', data = project_Wireline)


# In[36]:


plt.figure(figsize =(9,6))
plt.title('Figutre 6: Customer Satisfaction level on Pro-activeness in installation plan')
sns.barplot(x = 'Service Provider', y = 'Pro-activeness in installation plan', data = project_Wireline, palette = 'cool', hue = 'Service Provider')


# In[37]:


plt.figure(figsize =(9,4))
plt.title('Figure 7 : Satisfaction level on Voice Quality')
sns.barplot(x = 'Service Provider', y = 'Voice quality', data = project_Wireline, hue = 'Service Provider')


# In[40]:


project_Wireline.groupby('Service Provider')['Continuous connection without call drops'].mean()


# In[39]:


plt.figure(figsize =(9,4))
plt.title('Figure 8: Satisfaction level on continuous connection without call drops')
sns.barplot(x = 'Service Provider', y = 'Continuous connection without call drops', data = project_Wireline, palette = 'cool', hue = 'Service Provider')


# In[41]:


plt.figure(figsize =(9,4))
plt.title('Figure 9: Customer Satisfaction on Internet Speed')
sns.barplot(x = 'Service Provider', y = 'Speed of Internet', data = project_Wireline, hue = 'Service Provider')


# In[43]:


plt.figure(figsize =(9,4))
plt.title('Figure 10: Dispute resolution related to Billing')
sns.barplot(x = 'Service Provider', y = 'Dispute in Billing', data = project_Wireline, palette = 'hot', hue = 'Service Provider')


# In[44]:


plt.figure(figsize =(9,4))
plt.title('Figure 11: Resolution Update provides by Customer care')
sns.barplot(x = 'Service Provider', y = 'Update provides by Customer care', data = project_Wireline, palette = 'cool', hue = 'Service Provider')


# In[46]:


plt.figure(figsize =(9,4))
plt.title('Figure 12: Timely updates on Complain from customer care')
sns.barplot(x = 'Service Provider', y = 'Timely updates on Complaint', data = project_Wireline, hue = 'Service Provider')


# In[50]:


plt.figure(figsize =(9,4))
plt.title('Figure 13: Customer Satisfaction on Responsiveness of field Engineer')
sns.barplot(x = 'Service Provider', y = 'Responsiveness of Engineer', data = project_Wireline, palette = 'hot', hue = 'Service Provider')


# In[48]:


plt.figure(figsize =(9,4))
plt.title('Figure 14: Customer Satisfaction on Ability of field Engineer')
sns.barplot(x = 'Service Provider', y = 'Ability of engineer', data = project_Wireline, hue = 'Service Provider')


# In[51]:


plt.figure(figsize =(9,4))
plt.title('Figure 15: Satisfaction level on time taken by engineer to resolve the technical issue')
sns.barplot(x = 'Service Provider', y = 'time taken by engineer', data = project_Wireline, palette = 'cool', hue = 'Service Provider')


# In[4]:


sns.countplot(x='awareness of escalation matrix', data = project_Wireline)


# In[3]:


sns.countplot(x='Have you used Self Service Online Portal?', data = project_Wireline)


# In[7]:


plt.figure(figsize =(9,4))
plt.title('Figure 16 : Trust level on Service provider')
sns.barplot(x = 'Service Provider', y = 'Trusted Brand', data = project_Wireline, palette = 'hot')


# In[9]:


plt.figure(figsize =(9,4))
plt.title('Figure 17: Expert in Telecom Sector as per Customer Review')
sns.barplot(x = 'Service Provider', y = 'experts in the field', data = project_Wireline, palette = 'cool')


# In[10]:


plt.figure(figsize =(9,4))
plt.title('Figure 18: Customer satisfction level on cost')
sns.barplot(x = 'Service Provider', y = 'Charges a fair price for the service it provides', data = project_Wireline, palette = 'cool')


# In[12]:


plt.figure(figsize =(9,4))
plt.title('Figure 19: Provides inovative solutions as per companys productivity')
sns.barplot(x = 'Service Provider', y = 'Provides solutions which enhances my companys productivity', data = project_Wireline, palette = 'hot')


# In[163]:


plt.figure(figsize =(9,4))
plt.title('Mode of Payment')
sns.countplot(df['Mode of Payment'], data = df, palette = 'cool', hue = 'Mode of Payment')


# In[169]:


##Which Service provider has Maximum Recomendation?

df[df['Rating of Brands'].max()==df['Rating of Brands']]['Service Provider']


# In[170]:


df['Rating of Brands'].std()


# In[171]:


df.isnull().sum()


# In[174]:


df3 = df.copy()


# In[175]:


df3


# In[176]:


df3['Satisfaction with Online Portal'].fillna(value = '0', inplace = True) 


# In[177]:


df3['Satisfaction with Online Portal']


# In[ ]:




