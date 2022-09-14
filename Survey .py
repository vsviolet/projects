#!/usr/bin/env python
# coding: utf-8

# In[60]:


# import libraries 

import pandas as pd
import seaborn as sns
import numpy as np

import matplotlib
import matplotlib.pyplot as plt
plt.style.use('ggplot')
from matplotlib.pyplot import figure
import plotly.express as px
import plotly.graph_objects as go

df = pd.read_csv(r'/Users/violet/survey.csv')


# In[4]:


df.head()


# In[6]:


df.columns


# ### Columns description:
# 
# 1. Timestamp
# 2. Age
# 3. Gender
# 4. Country
# 5. state: If you live in the United States, which state or territory do you live in?
# 6. self_employed: Are you self-employed?
# 7. family_history: Do you have a family history of mental illness?
# 8. treatment: Have you sought treatment for a mental health condition?
# 9. work_interfere: If you have a mental health condition, do you feel that it interferes with your work?
# 10. no_employees: How many employees does your company or organization have?
# 11. remote_work: Do you work remotely (outside of an office) at least 50% of the time?
# 12. tech_company: Is your employer primarily a tech company/organization?
# 13. benefits: Does your employer provide mental health benefits?
# 14. care_options: Do you know the options for mental health care your employer provides?
# 15. wellness_program: Has your employer ever discussed mental health as part of an employee wellness program?
# 16. seek_help: Does your employer provide resources to learn more about mental health issues and how to seek help?
# 17. anonymity: Is your anonymity protected if you choose to take advantage of mental health or substance abuse treatment resources?
# 18. leave: How easy is it for you to take medical leave for a mental health condition?
# 19. mental_health_consequence: Do you think that discussing a mental health issue with your employer would have negative consequences?
# 20. phys_health_consequence: Do you think that discussing a physical health issue with your employer would have negative consequences?
# 21. coworkers: Would you be willing to discuss a mental health issue with your coworkers?
# 22. supervisor: Would you be willing to discuss a mental health issue with your direct supervisor(s)?
# 23. mental_health_interview: Would you bring up a mental health issue with a potential employer in an interview?
# 24. phys_health_interview: Would you bring up a physical health issue with a potential employer in an interview?
# 25. mental_vs_physical: Do you feel that your employer takes mental health as seriously as physical health?
# 26. obs_consequence: Have you heard of or observed negative consequences for coworkers with mental health conditions in your workplace?
# 27. comments: Any additional notes or comments

# In[2]:


#drop unnecessary columns

df = df.drop(["Timestamp", "state"], axis = 1)


# In[18]:


df.columns


# In[10]:


#check for missing data 

df.isnull().sum()


# In[19]:


#Percent of missing 

pct_missing = (df.isnull().sum().sort_values(ascending = False)/len(df))*100
pct_missing


# In[3]:


#drop comments column as well 

df = df.drop("comments", axis = 1)


# In[43]:


df.shape


# In[6]:


df.info()


# In[4]:


#check unique values in Gender column 
df['Gender'].unique()


# In[5]:


df['Gender'].value_counts()


# In[6]:


df['Gender'] = df['Gender'].replace(['male', 'M', 'm', 'Make', 'Man', 'Cis Male', 'Male ', 'Cis Man', 'Mail', 'Malr', 'msle', 'cis male', 'Mal', 'Male (CIS)', 'maile'], 'Male')
df['Gender'] = df['Gender'].replace(['female', 'F', 'f', 'Woman', 'femail', 'femake', 'Female ', 'cis-female/femme', 'Female (cis)', 'woman', 'Femake', 'Cis Female'], 'Female')
df['Gender'] = df['Gender'].replace(['Male-ish', 'Trans-female',
       'something kinda male?', 'queer/she/they', 'non-binary', 'Nah',
       'All', 'Enby', 'fluid', 'Genderqueer', 'Androgyne', 'Agender',
       'Guy (-ish) ^_^', 'male leaning androgynous', 'Trans woman',
       'Neuter', 'Female (trans)', 'queer', 'A little about you', 'p',
       'ostensibly male, unsure what that really means'], 'Other')


# In[7]:


df['Gender'].value_counts()


# In[24]:


plt.figure(figsize=(10,5))
plt.bar(df.Gender.value_counts().index, df.Gender.value_counts())


# Majority men answered the survey because more men work in the Tech industry 

# In[26]:


df['treatment'].value_counts()


# In[62]:


plt.figure(figsize=(10,5))
fig = px.histogram(df, x = 'treatment', color='treatment', text_auto=True)
fig.show()


# Almost 50/50 split between those seeking treatment and those not. 

# In[9]:


df = df[df.Age>15]
df = df[df.Age<70]


# In[52]:


fig = px.histogram(df, x = 'Age', color= 'treatment' )
fig.show()


# In[39]:


plt.figure(figsize = (10,5))
sns.countplot(data = df, x = 'Gender', hue = 'treatment')


# In[33]:


plt.figure(figsize=(10,5))
sns.countplot(data=df, x = 'work_interfere')


# In[34]:


df['work_interfere'].value_counts()


# In[53]:


fig = px.histogram(df, x = 'work_interfere', color= 'treatment', text_auto=True, barmode = 'group' )
fig.show()


# Seems there may be some correlation between work interference and whether someone has sought treatment. 

# In[91]:


df.columns


# In[54]:


fig = px.histogram(df, x = 'remote_work', color= 'treatment', text_auto=True, barmode = 'group' )
fig.show()


# In[98]:


countries = df['Country'].value_counts()
countries[:10]


# In[22]:


top_countries = df[df['Country'].isin(['United States','United Kingdom', 'Canada', 'Germany', 'Netherlands', 'Ireland', 'Australia', 'France'])]


# In[55]:


plt.figure(figsize = (10,5))
fig = px.histogram(top_countries, x = 'Country', color= 'treatment', text_auto=True, barmode = 'group' )
fig.show()


# 1. Most of the people who completed the survey are from the US 
# 2. Of the people in the US, more have sought treatment than not 
# 3. It is pretty evenly split in other countries except France/Netherlands where less have sought treatment

# In[103]:


plt.figure(figsize = (10,5))
countries[:10].plot(kind='bar')


# In[40]:


df.head(10)


# In[20]:


# Let's check thoughts about mental vs physical health 

plt.figure(figsize=(10,5))
sns.countplot(data=df, x = 'mental_vs_physical')
plt.title('Do you feel that your employer takes mental health as seriously as physical health')


# Most don't know

# In[56]:


fig = px.histogram(df, x = 'mental_health_interview', 
             text_auto=True,
             title= 'Would you bring up a mental health issue with a potential employer in an interview?')
fig.show()


# In[57]:


fig = px.histogram(df, x = 'phys_health_interview', 
             text_auto=True,
             title='Would you bring up a physical health issue with a potential employer in an interview?')
fig.show()


# People generally feel less comfortable bringing up mental health issues with potential employers.
# Unlike physical health issues, most wouldn't even consider bringing up mental health issues. 

# In[58]:


fig = px.histogram(df, x = 'mental_health_consequence',
             text_auto=True, 
             title= 'Do you think that discussing a mental health issue with your employer would have negative consequences?')
fig.show()


# In[59]:


fig = px.histogram(df, x = 'phys_health_consequence', 
             text_auto=True, 
             title= 'Do you think that discussing a physical health issue with your employer would have negative consequences?')
fig.show()


#     Most people think bringing up mental health issues would be less appropriate than physical health issues

# In[28]:


plt.figure(figsize=(8,4))
plt.title('Is your anonymity protected if you choose to take advantage of treatment resources?')
sns.countplot(data = df , x = 'anonymity')


# Most people probably don't feel comfortable taking advantage of resources because they don't know how it will affect them at work and whether their anonymity will be protected. 

# In[43]:


sns.countplot(data = df , x = 'benefits')
plt.title('Does your employer provide mental health benefits')


# In[46]:


sns.countplot(data = df , x = 'seek_help')
plt.title('Does your employer provide resources to learn more about mental health issues and how to seek help?')


# In[48]:


sns.countplot(data = df , x = 'obs_consequence')
plt.title('Have you heard of or observed negative consequences for coworkers with mental health conditions in your workplace?')


# ### Some thoughts
# 1. This survey was taken in 2014, so it would be interesting to see how the conversation around mental health has changed.
# 2. It would be interesting to see data in the last 2.5 years on remote work vs mental health. 
# 3. It seems like employees either weren't aware of what employers offered or they felt that needs were not met. 
# 4. General consensus seems to be that mental health isn't taken as seriously as physical health
# 5. About 50% of those surveyed have sought treatment so it was not uncommon. 
# 
