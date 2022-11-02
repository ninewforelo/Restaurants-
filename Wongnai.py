#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install selenium')
get_ipython().system('pip install bs4')
get_ipython().system('pip install pandas')


# In[2]:


import bs4
import pandas as pd
import requests
import selenium
from bs4 import BeautifulSoup
from selenium import webdriver 
from selenium.webdriver.firefox.options import Options
import time


# In[3]:


options = Options()
options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
driver = webdriver.Firefox(executable_path=r'C:\Users\COM01\Documents\Pliwlom\DSI 314\geckodriver.exe', options=options)
driver.get('https://www.wongnai.com/businesses?q=%E0%B8%97%E0%B8%B1%E0%B9%89%E0%B8%87%E0%B8%AB%E0%B8%A1%E0%B8%94%E0%B9%83%E0%B8%99%E0%B8%A0%E0%B8%B2%E0%B8%84%E0%B9%83%E0%B8%95%E0%B9%89&originalQ=%E0%B8%A3%E0%B9%89%E0%B8%B2%E0%B8%99%E0%B8%AD%E0%B8%B2%E0%B8%AB%E0%B8%B2%E0%B8%A3%E0%B8%97%E0%B8%B1%E0%B9%89%E0%B8%87%E0%B8%AB%E0%B8%A1%E0%B8%94%E0%B9%83%E0%B8%99%E0%B8%A0%E0%B8%B2%E0%B8%84%E0%B9%83%E0%B8%95%E0%B9%89&page.number=1&page.size=150&rerank=false')


# In[4]:


driver.execute_script("document.body.style.MozTransform='scale(0.1)';")
driver.execute_script('document.body.style.MozTransformOrigin = "0 0";')


# In[5]:


data = driver.page_source
soup = bs4.BeautifulSoup(data)
time.sleep(6)


# In[6]:


all_Name = soup.find_all('div',{'class':"sc-1bs98dy-2 Dtkmv"})


# In[7]:


all_Name_list = []
for Name in all_Name:
    all_Name_list.append(Name.text)
all_Name_list


# In[8]:


all_Rating = soup.find_all('div',{'class':"Gap-sc-ilei7b Container-sc-1lk8ybd ikRntG bZDAts badge-content"})


# In[9]:


all_Rating_list = []
for Rating in all_Rating:
    all_Rating_list.append(Rating.text)
all_Rating_list


# In[10]:


all_Review = soup.find_all('span',{'class':"sc-1uyabda-0 iQqWsz rg12 text-gray-500"})


# In[11]:


all_Review_list = []
for Review in all_Review:
    all_Review_list.append(Review.text)
all_Review_list


# In[12]:


all_Location = soup.find_all('span',{'class':"text-gray-500 font-highlight rg16 rg14-mWeb"})


# In[13]:


all_Location_list = []
for Location in all_Location:
    all_Location_list.append(Location.text)
all_Location_list


# In[14]:


Wongnai_data = pd.DataFrame([all_Name_list,all_Rating_list,all_Review_list, all_Location_list])


# In[15]:


Wongnai_data = Wongnai_data.transpose()
Wongnai_data.columns = ['Name','Rating','Review','Location']


# In[16]:


Wongnai_data


# In[17]:


Wongnai_data.to_excel('Wongnai.xlsx', encoding='utf-8')


# In[ ]:




