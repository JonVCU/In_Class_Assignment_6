#!/usr/bin/env python
# coding: utf-8

# In[1]:


#The question I want to answer with this data of the most popular dog breeds in the U.S.is which is the most popular and least popular breeds. I want to visualize the data to make it easier for the viewer to see which breeds tend to be on the uptrend and those that are decreasing.  


# In[ ]:


import pandas as pd


# In[2]:


df = pd.read_csv("allDogDescriptions.csv.zip")


# In[3]:


df.head(5)
df.tail(4)


# In[4]:


df.shape


# In[ ]:





# In[ ]:





# In[ ]:





# In[7]:


import plotly.express as px
fig = px.histogram(df, x=["Dog Type" "Breed"], barmode="overlay")
fig.show()


# In[8]:


correlation_matrix = df.corr()
fig = px.imshow(correlation_matrix, text_auto=True)
fig.show()


# In[ ]:


#By looking at the data what we found was that the cattle dos was the most popular out of all of the dogs in the dataset. We chose to use both a histogram and a heat map to visualize the data to make it much more easier for the user to view when wanting to find out which breeds people are chosing to get. What is fascinating is that a lot of the popular dog breeds are bigger then the average size dog. I was thinking that the smaller size dog would be the most popular beace they would be much more easier to take care of. 


# In[ ]:





# In[ ]:




