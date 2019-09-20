#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[1]:


import pandas as pd
from bs4 import BeautifulSoup as bs
import requests
from splinter import Browser


# In[ ]:

def scrape_info():
    
    # PART 1 NASA Mars News


    # In[2]:


    mars_url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"


    # In[3]:


    response = requests.get(mars_url)


    # In[4]:


    soup = bs(response.text, 'html.parser')


    # In[5]:


    print(soup.prettify())


    # In[6]:


    title_results = soup.find_all('div', class_="content_title")
    first_title = title_results[0].text
    first_title


    # In[7]:


    paragraph_results = soup.find_all('div', class_="rollover_description_inner")
    first_para = paragraph_results[0].text
    first_para


    # In[ ]:


    # Part 2 JPL Mars Space Images - Featured Image


    # In[62]:


    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)

    image_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(image_url)


    # In[63]:


    # image_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    # browser.visit(image_url)


    # In[ ]:





    # In[ ]:


    # Part 3 Mars Weather


    # In[11]:


    weather_url = "https://twitter.com/marswxreport?lang=en"


    # In[12]:


    response2 = requests.get(weather_url)
    soup2 = bs(response2.text, 'html.parser')


    # In[13]:


    print(soup2.prettify())


    # In[17]:


    #weather_results = soup.find_all('div', class_="js-tweet-text-container")
    #recent_weather = weather_results[0].text
    #recent_weather


    # In[28]:


    # weather_results = soup.find_all('div', class_="js-tweet-text-container")
    # weather = []

    # for x in weather_results:
    #     if "sol" in x.text:
    #         weather.append(x)
        
    # mars_weather = weather[0]
    # mars_weather


    # In[ ]:





    # In[ ]:


    # Part 4 Mars Facts

    
    # In[29]:


    facts_url = "https://space-facts.com/mars/"


    # In[32]:


    response3 = requests.get(facts_url)
    soup3 = bs(response3.text, 'lxml')
    print(soup3.prettify())


    # In[67]:


    mars = soup3.find('table', attrs={'class':'tablepress-id-comp-mars'})
    data = mars.find_all('tr')
    points = []     

    for x in data:
        table_head = x.find_all('th')
        if len(table_head) != 0:
        header = [x.text for x in table_head]
    else:
        td = x.find_all('td')
        row = [x.text for x in td]
        points.append(row)
        
        fact_df = pd.DataFrame(l, columns=header)
        fact_df 


        # In[70]:


        just_mars = fact_df.drop('Earth', axis=1)
        just_mars.rename(columns={'Mars - Earth Comparison': 'Measurements'})


        # In[72]:


        just_mars.to_html()


        # In[ ]:





        # In[ ]:


        # Part 5 Mars Hemispheres


        # In[79]:


        img_urls = ["https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced",
           "https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced",
           "https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced",
           "https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced"]

        pictures = []

        for x in img_urls:
            urls = requests.get(x)
            bs4 = bs(urls.text, 'html.parser')    
            row = {'title': bs4.title.text.split(' Enhanced')[0],
          'img_url': bs4.find('div', class_='downloads').a['href']}
            hemisphere_image_urls.append(row)


            # In[80]:


            hemisphere_image_urls   


            # In[81]:


            get_ipython().system('jupyter nbconvert --to script ')


            # In[ ]:




