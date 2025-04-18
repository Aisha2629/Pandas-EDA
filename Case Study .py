#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


data=pd.read_csv('4. covid_19_data.csv')


# In[3]:


data.head()


# In[4]:


data.isnull().sum()


# In[5]:


sns.heatmap(data.isnull())


# In[6]:


#Q. 1) Show the number of Confirmed, Deaths and Recovered cases in each Region.
data.groupby('Region').sum()


# In[7]:


#Confirmed Case in each region
data.groupby('Region')['Confirmed'].sum()


# In[8]:


data.groupby('Region')['Recovered'].sum()


# In[13]:


data.groupby('Region')['Deaths'].sum()


# In[18]:


#Q. 2) Remove all the records where the Confirmed Cases is Less Than 10.
data[~(data['Confirmed'] < 10)]


# In[24]:


#Q. 3) In which Region, maximum number of Confirmed cases were recorded ?
data.groupby('Region').Confirmed.max().sort_values(ascending=False)


# In[26]:


data.groupby('Region').Deaths.min().sort_values(ascending=True)


# In[29]:


#Q. 5) How many Confirmed, Deaths & Recovered cases were reported from India till 29 April 2020 ?

data[data['Region']=='India']


# In[31]:


#Sort the Values by confirmed cases in ascending value

data.sort_values(by=['Confirmed'],ascending=True)


# In[32]:


#Q. 6-B ) Sort the entire data wrt No. of Recovered cases in descending order.

data.sort_values(by=['Recovered'],ascending=False)


# In[ ]:





# In[ ]:





# In[ ]:





# # 6. India Census Analysis

# In[12]:


cen=pd.read_csv('6. India Census 2011.csv')


# In[13]:


#Basic Data Exploration
cen.head(5)


# In[14]:


cen.info()


# In[15]:


cen.isnull().sum()


# In[16]:


cen.dtypes


# In[17]:


cen.index


# In[18]:


cen.columns


# In[19]:


#Q. 1) How will you hide the indexes of the dataframe.

cen.style.hide_index ()


# In[20]:


#Q. 2) How can we set the caption / heading on the data frame

cen.style.set_caption('India Census Analysis')


# In[21]:


#Q. 3) Show the records related with the districts - New Delhi , Lucknow , Jaipur
cen[cen['District_name'].isin(['New Delhi','Lucknow','Jaipur'])]


# In[22]:


#Q. 4) Calculate state-wise :
#A. Total number of population.


cen.groupby('State_name')['Population'].sum()


# In[23]:


#B. Total no. of the population with different religions.
cen.groupby('State_name')['Christians','Sikhs','Buddhists','Jains'].sum()


# In[24]:


#Q. 5) How many Male Workers were there in Maharashtra state ?

cen[cen['State_name']=='MAHARASHTRA']['Male_Workers'].sum()


# In[25]:


#Q. 6) How many Female Workers were there in NAGALAND state ?


# In[34]:


(cen[cen['State_name']=='NAGALAND']['Female_Workers'].sum()/1978502)*100


# In[38]:


(cen[cen['State_name']=='NAGALAND']['Male_Workers'].sum()/1978502)*100


# In[ ]:





# In[32]:


cen[cen['State_name']=='NAGALAND']['Population'].sum()


# # Data Science Warmup Exercise

# In[109]:


dict={
    'Name':['Aishwarya','Prajkta','Rashi','Ashish','Vaishnavi','Suraj'],
    'Score':[98,90,68,70,65,88],
    'Gender':['Female','Female','Female','Male','Female','Male']
}
df=pd.DataFrame(dict)
df


# In[112]:


#Top 3 Rows 

df.head(3)


# In[111]:


#Last 3 Rows
df.tail(3)


# In[113]:


#Shape

df.shape


# In[114]:


df.info()


# In[115]:


#Checking Null

df.isnull().sum()


# In[116]:


df.describe()


# In[118]:


#Find All unique Value

df['Gender'].unique()


# In[119]:


#No. of Unique Value in Gender
df['Gender'].nunique()


# In[120]:


#COUNT OF UNIQUE VALUES
df['Gender'].value_counts()


# In[124]:


#Total Num of students who has marks bet 90 and 100
len(df[(df['Score'] >=90)  & (df['Score'] <=100)])


# In[123]:


df['Score'].between(90,100).sum()


# In[126]:


#Mean
df['Score'].mean()


# In[127]:


#max marks
df['Score'].max()


# In[ ]:




