#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import os

cities_data_input = "cities.csv"

cities_data_html_file = os.path.join('../', 'WebVisualizations',  'cities_data_table.html')


# In[2]:


cityWeatherDF = pd.read_csv(cities_data_input)
cityWeatherDF.head()


# In[3]:



ll_city = []
for index, row in cityWeatherDF.iterrows():
    this_city = row['City']    
    lat = row['Lat']
    lng = row['Lng']
    str = f'<a href="https://www.google.com/maps/@{lat},{lng},11z" target="_blank">{this_city}</a>'
    ll_city.append(str)

cityWeatherDF["City"] = ll_city   



# In[ ]:





# In[4]:


cityWeatherDF.to_html(cities_data_html_file, index=False, escape=False)


# In[ ]:




