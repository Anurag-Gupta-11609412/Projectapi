#!/usr/bin/env python
# coding: utf-8

# In[38]:


import requests

base_url = 'https://restcountries.com/v3.1/all'
resp = requests.get(base_url)
data = resp.json()

#print(type(data))
for country in data:
    print("Country name: ",(country['name']['common']))
    print("Capital:",(country['capital']))
    print("Population:",(country['population']))
    print("Area:",(country['area']))
    print("Region:",(country['region']))
    print("Capital:",(country['currencies']))
    print("Country_code:",(country['cioc']))


# In[ ]:




