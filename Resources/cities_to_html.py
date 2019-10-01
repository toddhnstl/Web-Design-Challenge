#!/usr/bin/env python
# coding: utf-8

# In[20]:



import pandas as pd
import numpy as np
import os

cities_data_file = "cities.csv"

cities_data_html_file = os.path.join('..', 'cities_data_table.html')



# In[21]:


cityWeatherDF = pd.read_csv(cities_data_file)
cityWeatherDF.head()


# In[22]:


cityWeatherDF.to_html(cities_data_html_file, index=False, justify="center")


# In[ ]:




