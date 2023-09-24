#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install selenium')
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import warnings
warnings.filterwarnings('ignore')


# # Q1: Write a python program to scrape data for “Data Analyst” Job position in “Bangalore” location. Youhave to scrape the job-title, job-location, company_name, experience_required. You have to scrape first 10jobs data.
# This task will be done in following steps:
# 1. First get the webpage https://www.shine.com/
# 2. Enter “Data Analyst” in “Job title, Skills” field and enter “Bangalore” in “enter the location” field.
# 3. Then click the searchbutton.
# 4. Then scrape the data for the first 10 jobs results you get.
# 5. Finally create a dataframe of the scraped data.

# In[ ]:


import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import warnings
warnings.filterwarnings('ignore')


# In[2]:


driver = webdriver.Chrome()


# In[3]:


url = 'https://www.shine.com/'
driver.get(url)


# In[5]:


search_job = driver.find_element(By.XPATH,"/html/body/div[1]/div[4]/div/div[2]/div[2]/div/form/div/div[1]/ul/li[1]/div/input")
search_job.send_keys('Data Analyst')


# In[6]:


loc = driver.find_element(By.XPATH,"/html/body/div[1]/div[4]/div/div[2]/div[2]/div/form/div/div[1]/ul/li[2]/div/input")
loc.send_keys('Bangalore')


# In[8]:


search = driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/div/div[2]/div[2]/div/form/div/div[2]/div/button")
search.click()


# In[60]:


job_title=[]
job_location=[]
company_name=[]
experience_required=[]


# In[61]:


title_tags = driver.find_elements(By.XPATH, '//h2[@itemprop="name"]')


# In[62]:


for i in title_tags[0:10]:
        title=i.text
        job_title.append(title)
    


# In[63]:


location_tags = driver.find_elements(By.XPATH,'//div[@class=" jobCard_jobCard_lists_item__YxRkV jobCard_locationIcon__zrWt2"]')


# In[64]:


for i in location_tags[0:10]:
        location=i.text
        job_location.append(location)


# In[65]:


company_tags = driver.find_elements(By.XPATH, '//div[@class="jobCard_jobCard_cName__mYnow"]')


# In[66]:


for i in company_tags[0:10]:
        company=i.text
        company_name.append(company)


# In[69]:



experience_tags = driver.find_elements(By.XPATH,'//div[@class=" jobCard_jobCard_lists_item__YxRkV jobCard_jobIcon__3FB1t"]')
for i in experience_tags[0:10]:
    experience=i.text
    experience_required.append(experience)
    experience


# In[72]:


print(len(job_title), len(job_location), len(company_name), len(experience_required))


# In[75]:


df = pd.DataFrame({
    'Job Title': job_title,
    'Job Location': job_location,
    'Company Name': company_name,
    'Experience Required': experience_required})


# In[76]:


df


# In[ ]:





# # Q2:Write a python program to scrape data for “Data Scientist” Job position in“Bangalore” location. Youhave to scrape the job-title, job-location, company_name. You have to scrape first 10 jobs data.
# This task will be done in following steps:
# 1. First get the webpage https://www.shine.com/
# 2. Enter “Data Scientist” in “Job title, Skills” field and enter “Bangalore” in “enter thelocation” field.
# 3. Then click the search button.
# 4. Then scrape the data for the first 10 jobs results you get.
# 5. Finally create a dataframe of the scraped data.
# 

# In[ ]:


import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import warnings
warnings.filterwarnings('ignore')


# In[79]:


driver = webdriver.Chrome()


# In[80]:


url = 'https://www.shine.com/'
driver.get(url)


# In[82]:


search_job = driver.find_element(By.XPATH,"/html/body/div[1]/div[4]/div/div[2]/div[2]/div/form/div/div[1]/ul/li[1]/div/input")
search_job.send_keys('Data Scientist')


# In[83]:


loc = driver.find_element(By.XPATH,"/html/body/div[1]/div[4]/div/div[2]/div[2]/div/form/div/div[1]/ul/li[2]/div/input")
loc.send_keys('Bangalore')


# In[84]:


search = driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/div/div[2]/div[2]/div/form/div/div[2]/div/button")
search.click()


# In[85]:


job_title=[]
job_location=[]
company_name=[]


# In[86]:


title_tags = driver.find_elements(By.XPATH, '//h2[@itemprop="name"]')


# In[87]:


for i in title_tags[0:10]:
        title=i.text
        job_title.append(title)


# In[90]:


location_tags = driver.find_elements(By.XPATH,'//div[@class=" jobCard_jobCard_lists_item__YxRkV jobCard_locationIcon__zrWt2"]')


# In[91]:


for i in location_tags[0:10]:
        location=i.text
        job_location.append(location)


# In[92]:


company_tags = driver.find_elements(By.XPATH, '//div[@class="jobCard_jobCard_cName__mYnow"]')


# In[93]:


for i in company_tags[0:10]:
        company=i.text
        company_name.append(company)


# In[98]:


print(len(job_title), len(job_location), len(company_name))


# In[97]:


df = pd.DataFrame({
    'Job Title': job_title,
    'Job Location': job_location,
    'Company Name': company_name,})


# In[99]:


df


# In[ ]:





# # Q3: In this question you have to scrape data using the filters available on the webpageYou have to use the location and salary filter.
# You have to scrape data for “Data Scientist” designation for first 10 job results.
# You have to scrape the job-title, job-location, company name, experience required.
# The location filter to be used is “Delhi/NCR”. The salary filter to be used is “3-6” lakhs
# The task will be done as shown in the below steps:
# 1. first get the web page https://www.shine.com/
# 2. Enter “Data Scientist” in “Skill, Designations, and Companies” field.
# 3. Then click the search button.
# 4. Then apply the location filter and salary filter by checking the respective boxes
# 5. Then scrape the data for the first 10 jobs results you get.
# 6. Finally create a dataframe of the scrapeddata.

# In[59]:


import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import warnings
warnings.filterwarnings('ignore')


# In[60]:


driver = webdriver.Chrome()


# In[61]:


url = 'https://www.shine.com/'
driver.get(url)


# In[63]:


search_job = driver.find_element(By.XPATH,"/html/body/div[1]/div[4]/div/div[2]/div[2]/div/form/div/div[1]/ul/li[1]/div/input")
search_job.send_keys('Data Scientist')
search_location = driver.find_element(By.XPATH,"/html/body/div[1]/div[4]/div/div[2]/div[2]/div/form/div/div[1]/ul/li[2]/div/input")
search_location.send_keys('Delhi/NCR')


# In[64]:


search_btn = driver.find_element(By.XPATH,"/html/body/div[1]/div[4]/div/div[2]/div[2]/div/form/div/div[2]/div/button")
driver.execute_script("arguments[0].click();", search_btn)


# In[65]:


title_tags = driver.find_elements(By.XPATH,'//h2[@itemprop="name"]')
titles = []
for i in title_tags:
    titles.append(i.text)
del titles[10:]
len(titles)


# In[66]:


company_tags = driver.find_elements(By.XPATH,'//div[@class="jobCard_jobCard_cName__mYnow"]')
company = []
for i in company_tags:
    company.append(i.text)
del company[10:]
len(company)


# In[67]:


exp_tags = driver.find_elements(By.XPATH,'//div[@class=" jobCard_jobCard_lists_item__YxRkV jobCard_jobIcon__3FB1t"]')
exp = []
for i in exp_tags:
    exp.append(i.text)
del exp[10:]
len(exp)


# In[68]:


loc_tags = driver.find_elements(By.XPATH,'//div[@class=" jobCard_jobCard_lists_item__YxRkV jobCard_locationIcon__zrWt2"]')
loc = []
for i in loc_tags:
    loc.append(i.text)
del exp[10:]
len(exp)


# In[70]:


data = pd.DataFrame()
data['Position'] = titles
data['Company'] = company
data['Experience'] = exp
data


# In[ ]:





# # Q4: Scrape data of first 100 sunglasses listings on flipkart.com. You have to scrape four attributes:
# 6. Brand
# 7. ProductDescription
# 8. Price
# The attributes which you have to scrape is ticked marked in the below image.
# To scrape the data you have to go through following steps:
# 1. Go to Flipkart webpage by url :https://www.flipkart.com/
# 2. Enter “sunglasses” in the search fieldwhere “search for products, brands and more” is written and
# click the search icon
# 3. After that you will reach to the page having a lot of sunglasses. From this page you can scrap the
# required data as usual.
# 4. After scraping data from the first page, go to the “Next” Button at the bottom other page , then
# click on it.
# 5. Now scrape data from this page as usual
# 6. Repeat this until you get data for 100sunglasses.

# In[15]:


import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import warnings
warnings.filterwarnings('ignore')


# In[16]:


driver = webdriver.Chrome()


# In[17]:


url = 'https://www.flipkart.com/'
driver.get(url)


# In[18]:



search_sunglasses = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div/div/div/div[1]/div/div[1]/div/div[1]/header/div[1]/div[2]/form/div/div/input")
search_sunglasses.send_keys('sunglasses')


# In[22]:


search_btn = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div/div/div/div[1]/div/div[1]/div/div[1]/header/div[1]/div[2]/form/div/button")
driver.execute_script("arguments[0].click();", search_btn)


# In[23]:


brand_tags = driver.find_elements(By.XPATH,'//div[@class="_2WkVRV"]')
brands = []
for i in brand_tags:
    brands.append(i.text)
len(brands)


# In[26]:


descrip = driver.find_elements(By.XPATH,'//a[@class="IRpwTa"]')
dis = []
for i in descrip:
    dis.append(i.text)
len(dis)


# In[27]:


prices = driver.find_elements(By.XPATH,'//div[@class="_30jeq3"]')
price = []
for i in prices:
    price.append(i.text)
len(price)


# In[28]:


discounts = driver.find_elements(By.XPATH,'//div[@class="_3Ay6Sb"]')
discount = []
for i in discounts:
    discount.append(i.text)
len(discount)


# In[29]:


next_page = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/div[1]/div[2]/div[12]/div/div/nav/a[11]")


# In[30]:


driver.execute_script("arguments[0].click();", next_page)


# In[31]:


brand_tags = driver.find_elements(By.XPATH,'//div[@class="_2WkVRV"]')
for i in brand_tags:
    brands.append(i.text)
len(brands)


# In[32]:


descrip = driver.find_elements(By.XPATH,'//a[@class="IRpwTa"]')
for i in descrip:
    dis.append(i.text)
len(dis)


# In[33]:


prices = driver.find_elements(By.XPATH,'//div[@class="_30jeq3"]')
for i in prices:
    price.append(i.text)
len(price)


# In[34]:


discounts = driver.find_elements(By.XPATH,'//div[@class="_3Ay6Sb"]')
for i in discounts:
    discount.append(i.text)
len(discount)


# In[35]:


next_page1 = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/div[1]/div[2]/div[12]/div/div/nav/a[12]")


# In[36]:


driver.execute_script("arguments[0].click();", next_page1)


# In[37]:


brand_tags = driver.find_elements(By.XPATH,'//div[@class="_2WkVRV"]')
for i in brand_tags:
    brands.append(i.text)
del brands[100:]
len(brands)


# In[39]:


descrip = driver.find_elements(By.XPATH,'//a[@class="IRpwTa"]')
for i in descrip:
    dis.append(i.text)
del dis[100:]
len(dis)


# In[38]:


prices = driver.find_elements(By.XPATH,'//div[@class="_30jeq3"]')
for i in prices:
    price.append(i.text)
del price[100:]
len(price)


# In[40]:


discounts = driver.find_elements(By.XPATH,'//div[@class="_3Ay6Sb"]')
for i in discounts:
    discount.append(i.text)
del discount[100:]
len(discount)


# In[41]:


data = pd.DataFrame()
data['Brand'] = brands
data['Description'] = dis
data['Price'] = price
data['Discount'] = discount


# In[42]:


data


# In[ ]:





# # Q5: Scrape 100 reviews data from flipkart.com for iphone11 phone. You have to go the link:
# https://www.flipkart.com/apple-iphone-11-black-64-gb/productreviews/itm4e5041ba101fd?pid=MOBFWQ6BXGJCEYNY&lid=LSTMOBFWQ6BXGJCEYNYZXSHRJ&market
# place=FLIPKART
# As shown in the above page you have to scrape the tick marked attributes. These are:
# 1. Rating
# 2. Review summary
# 3. Full review
# 4. You have to scrape this data for first 100reviews.
# 

# In[1]:


import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import warnings
warnings.filterwarnings('ignore')


# In[2]:


driver = webdriver.Chrome()


# In[3]:


url = 'https://www.flipkart.com/'
driver.get(url)


# In[4]:


search_iphone = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div/div/div/div[1]/div/div[1]/div/div[1]/header/div[1]/div[2]/form/div/div/input")
search_iphone.send_keys('iphone 11')


# In[5]:


search_btn = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div/div/div/div[1]/div/div[1]/div/div[1]/header/div[1]/div[2]/form/div/button")
driver.execute_script("arguments[0].click();", search_btn)


# In[6]:


click_iphone = driver.find_element(By.XPATH,"/html/body/div/div/div[3]/div[1]/div[2]/div[2]/div/div/div/a/div[2]/div[1]/div[1]")
click_iphone.click()


# In[97]:


from selenium.webdriver.common.by import By
review = []
for i in range(0, 17):
    reviews = driver.find_elements(By.XPATH, '//div[@class="_3LWZlK _1BLPMq"]')
    for j in reviews:
        review.append(j.text)


# In[98]:


review


# In[99]:


from selenium.webdriver.common.by import By
review_sum = []
for i in range(0, 17):
    reviews_sum = driver.find_elements(By.XPATH, '//p[@class="_2-N8zT"]')
    for review in reviews_sum:
        review_sum.append(review.text)


# In[100]:


review_sum


# In[101]:


from selenium.webdriver.common.by import By
full_review = []
for i in range(0, 17):
    reviews_ful = driver.find_elements(By.XPATH, '//div[@class="t-ZTKy"]')
    for review in reviews_ful:
        full_review.append(review.text)


# In[102]:


full_review


# In[103]:


ReviewData = pd.DataFrame({})
ReviewData['Review'] = review
ReviewData['Review_Summary'] = review_sum
ReviewData['full_Review'] = full_review
ReviewData


# In[ ]:





# # Q6: Scrape data forfirst 100 sneakers you find whenyou visit flipkart.com and search for “sneakers” inthe
# search field.
# You have to scrape 3 attributes of each sneaker:
# 1. Brand
# 2. ProductDescription
# 3. Price
# As shown in the below image, you have to scrape the above attributes.
# 

# In[ ]:


import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import warnings
warnings.filterwarnings('ignore')


# In[32]:


driver = webdriver.Chrome()


# In[33]:


url = 'https://www.flipkart.com/'
driver.get(url)


# In[ ]:


signup = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/button")


# In[ ]:


driver.execute_script("arguments[0].click();", signup)


# In[40]:


search = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div/div/div/div[1]/div/div[1]/div/div[1]/header/div[1]/div[2]/form/div/button")


# In[41]:


search_snea = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div/div/div/div[1]/div/div[1]/div/div[1]/header/div[1]/div[2]/form/div/button")
search_snea.click()


# In[42]:


brand_tags = driver.find_elements(By.XPATH,'//div[@class="_2WkVRV"]')
brands = []
for i in brand_tags:
    brands.append(i.text)
len(brands)


# In[43]:


descrip = driver.find_elements(By.XPATH,'//div[@class="_2B099V"]')
dis = []
for i in descrip:
    dis.append(i.text.split('₹')[0].split('\n')[1])
len(dis)


# In[44]:


prices = driver.find_elements(By.XPATH,'//div[@class="_30jeq3"]')
price = []
for i in prices:
    price.append(i.text)
len(price)


# In[45]:


discounts = driver.find_elements(By.XPATH,'//div[@class="_3Ay6Sb"]')
discount = []
for i in discounts:
    discount.append(i.text)
len(discount)


# In[46]:


next_page = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/div[1]/div[2]/div[12]/div/div/nav/a[11]")


# In[47]:


driver.execute_script("arguments[0].click();", next_page)


# In[48]:


brand_tags = driver.find_elements(By.XPATH,'//div[@class="_2WkVRV"]')
for i in brand_tags:
    brands.append(i.text)
len(brands)


# In[49]:


descrip = driver.find_elements(By.XPATH,'//div[@class="_2B099V"]')
for i in descrip:
    dis.append(i.text.split('₹')[0].split('\n')[1])
len(dis)


# In[50]:


prices = driver.find_elements(By.XPATH,'//div[@class="_30jeq3"]')
for i in prices:
    price.append(i.text)
len(price)


# In[51]:


discounts = driver.find_elements(By.XPATH,'//div[@class="_3Ay6Sb"]')
for i in discounts:
    discount.append(i.text)
len(discount)


# In[52]:


next_page1 = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/div[1]/div[2]/div[12]/div/div/nav/a[12]")


# In[53]:


driver.execute_script("arguments[0].click();", next_page1)


# In[54]:


brand_tags = driver.find_elements(By.XPATH,'//div[@class="_2WkVRV"]')
for i in brand_tags:
    brands.append(i.text)
del brands[100:]
len(brands)


# In[55]:


descrip = driver.find_elements(By.XPATH,'//a[@class="IRpwTa"]')
for i in descrip:
    dis.append(i.text)
del dis[100:]
len(dis)


# In[56]:


prices = driver.find_elements(By.XPATH,'//div[@class="_30jeq3"]')
for i in prices:
    price.append(i.text)
del price[100:]
len(price)


# In[57]:


discounts = driver.find_elements(By.XPATH,'//div[@class="_3Ay6Sb"]')
for i in discounts:
    discount.append(i.text)
del discount[100:]
len(discount)


# In[59]:


data = pd.DataFrame()
data['Brand'] = brands
data['Description'] = dis
data['Price'] = price
data['Discount'] = discount
data


# In[ ]:





# # Q7: Go to webpage https://www.amazon.in/ Enter “Laptop” in the search field and then click the search icon. Then
# set CPU Type filter to “Intel Core i7” as shown in the below image:
# After setting the filters scrape first 10 laptops data. You have to scrape 3 attributes for each laptop:
# 1. Title
# 2. Ratings
# 3. Price

# In[60]:


import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import warnings
warnings.filterwarnings('ignore')


# In[61]:


driver = webdriver.Chrome()


# In[62]:


url = 'https://www.amazon.in/'
driver.get(url)


# In[63]:


search = driver.find_element(By.XPATH,"/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[2]/div[1]/input")
search.send_keys('Laptop')


# In[64]:


search_btn = driver.find_element(By.XPATH,"/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[3]/div/span/input")


# In[65]:


driver.execute_script("arguments[0].click();", search_btn)


# In[68]:


search_i7 = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[1]/div[2]/div/div[3]/span/div[1]/div/div/div[6]/ul[6]/span[12]/li/span/a/div/label/i")
driver.execute_script("arguments[0].click();", search_i7)


# In[69]:


laptop = driver.find_elements(By.XPATH,'//span[@class="a-size-medium a-color-base a-text-normal"]')
laptops = []
for i in laptop:
    laptops.append(i.text)
del laptops[10:]
len(laptops)


# In[70]:


price = driver.find_elements(By.XPATH,'//span[@class="a-price-whole"]')
prices = []
for i in price:
    prices.append(i.text)
del prices[10:]
len(prices)


# In[73]:


data = pd.DataFrame()
data['Laptop Name'] = laptops
data['Price'] = prices
data


# # Q8: Write a python program to scrape data for Top 1000 Quotes of All Time.
# The above task will be done in following steps:
# 1. First get the webpagehttps://www.azquotes.com/
# 2. Click on TopQuotes
# 3. Than scrap a) Quote b) Author c) Type Of Quotes

# In[1]:


import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import warnings
warnings.filterwarnings('ignore')


# In[2]:


driver = webdriver.Chrome()


# In[3]:


#site link
url = 'https://www.azquotes.com/'
driver.get(url)


# In[4]:



search_top_quotes = driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[1]/div/div[3]/ul/li[5]/a")
search_top_quotes.click()


# In[66]:


from selenium.webdriver.common.by import By
Quote = []
for i in range(0, 10):
    Quote_tags = driver.find_elements(By.XPATH, '//a[@class="title"]')
    for qt in Quote_tags:
        Quote.append(qt.text)


# In[67]:


Quote


# In[68]:


len(Quote)


# In[69]:


from selenium.webdriver.common.by import By
Author = []
for i in range(0, 10):
    author_tags = driver.find_elements(By.XPATH, '//div[@class="author"]')
    for r in author_tags:
        Author.append(r.text)


# In[70]:


Author


# In[71]:


len(Author)


# In[72]:


from selenium.webdriver.common.by import By
Type_of_Quote = []
for i in range(0, 10):
    type_tags = driver.find_elements(By.XPATH, '//div[@class="tags"]')
    for j in type_tags:
        Type_of_Quote.append(j.text)


# In[73]:


Type_of_Quote


# In[74]:


len(Type_of_Quote)


# In[77]:


#make data frame
import pandas as pd

data = {'Quote': Quote,'Author': Author,'Type_of_Quote': Type_of_Quote}
df = pd.DataFrame(data)


# In[78]:


df


# In[ ]:





# # Q9: Write a python program to display list of respected former Prime Ministers of India(i.e. Name, Born-Dead,
# Term of office, Remarks) from https://www.jagranjosh.com/.
# This task will be done in following steps:
# 1. First get the webpagehttps://www.jagranjosh.com/
# 2. Then You have to click on the GK option
# 3. Then click on the List of all Prime Ministers of India
# 4. Then scrap the mentioned data and make theDataFrame.

# In[12]:


import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import warnings
warnings.filterwarnings('ignore')


# In[13]:


driver = webdriver.Chrome()


# In[15]:


url = 'https://www.jagranjosh.com/'
driver.get(url)


# In[18]:


Name =[]
born_dead=[]
term_of_office=[]
remarks=[]


# In[19]:


name_tags = driver.find_elements(By.XPATH,'//a[@href="https://www.jagranjosh.com/general-knowledge/jawaharlal-nehru-biography-1573652876-1"]')
for i in name_tags:
    name_t =i.text
    name.append(name_t)


# In[20]:


born_tags = driver.find_elements(By.XPATH,'//td[@style="width: 105px; height: 121px;"]')
for i in born_tags:
    born_t =i.text
    name.append(born_t)


# In[22]:


office_tags = driver.find_elements(By.XPATH,'//td[@style="width: 256px; height: 121px;"]')
for i in office_tags:
    office_t =i.text
    name.append(office_t)


# In[23]:


remarks_tags = driver.find_elements(By.XPATH,'//td[@style="width: 145px; height: 121px;"]')
for i in remarks_tags:
    remarks_t =i.text
    name.append(remarks_t)


# In[24]:


df = pd.DataFrame({})
df['pm name'] =Name[:19]
df['Born dead'] =born_dead[:19]
df['Term of office'] =term_of_office[:19]
df['Remarks']= remarks[:19]
df


# # Q10: Write a python program to display list of 50 Most expensive cars in the world (i.e.
# Car name and Price) from https://www.motor1.com/
# This task will be done in following steps:
# 1. First get the webpage https://www.motor1.com/
# 2. Then You have to type in the search bar ’50 most expensive cars’
# 3. Then click on 50 most expensive carsin the world..
# 4. Then scrap the mentioned data and make the dataframe

# In[28]:


import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import warnings
warnings.filterwarnings('ignore')


# In[29]:


driver = webdriver.Chrome()


# In[30]:


url = 'https://www.motor1.com'
driver.get(url)


# In[31]:


search_car = driver.find_element(By.XPATH,"/html/body/div[10]/div[2]/div/div/div[3]/div/div/button")
search_car.send_keys('50 most expensive car')


# In[35]:


click_search_car = driver.find_element(By.XPATH,"/html/body/div[10]/div[2]/div/div/div[3]/div/div/div/form/button[1]")
click_search_car.click()


# In[36]:


Car_name = []
Price = []


# In[37]:


car_tags = driver.find_elements(By.XPATH,'//h3[@class="subheader"]')
for i in car_tags:
    car_m = i.text
    Car_name.append(car_m)


# In[38]:


price_tags = driver.find_elements(By.XPATH,'/html/body/div[10]/div[7]/div[2]/div[1]/div[2]/div[2]/p[4]/strong')
for i in price_tags:
    price_r = i.text
    Price.append(price_r)


# In[39]:


Price


# In[40]:


df =pd.DataFrame({'Car name':Car_name})
df


# In[ ]:




