#!/usr/bin/env python
# coding: utf-8

# Q1: Write a python program to scrape data for “Data Analyst” Job position in “Bangalore” location. You
# have to scrape the job-title, job-location, company_name, experience_required. You have to scrape first 10
# jobs data.
# This task will be done in following steps:
# 1. First get the webpage https://www.shine.com/
# 2. Enter “Data Analyst” in “Job title, Skills” field and enter “Bangalore” in “enter the location” field.
# 3. Then click the searchbutton.
# 4. Then scrape the data for the first 10 jobs results you get.
# 5. Finally create a dataframe of the scraped data.
# Note: All of the above steps have to be done in code. No step is to be done manually

# In[4]:


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Navigate to the Shine.com website
driver.get("https://www.shine.com/")

# Find the job title and location search fields and enter the values
job_title_input = driver.find_element(By.CSS_SELECTOR, 'input[name="q"]')
location_input = driver.find_element(By.CSS_SELECTOR, 'input[name="l"]')
search_button = driver.find_element(By.ID, 'jb_form_btn')

job_title_input.send_keys("Data Analyst")
location_input.send_keys("Bangalore")
search_button.click()

# Wait for the search results to load (you may need to adjust the wait time)
driver.implicitly_wait(10)

# Find job listings on the page
job_listings = driver.find_elements(By.CLASS_NAME, "search_listing")

# Create lists to store the scraped data
job_titles = []
job_locations = []
company_names = []
experience_required = []

# Loop through the job listings and extract the data
for job in job_listings[:10]:  # Get the first 10 jobs
    job_title = job.find_element(By.CLASS_NAME, "w-90").text.strip()
    job_location = job.find_elements(By.TAG_NAME, "span")[0].text.strip()
    company_name = job.find_elements(By.TAG_NAME, "span")[2].text.strip()
    exp_required = job.find_elements(By.TAG_NAME, "span")[4].text.strip()

    job_titles.append(job_title)
    job_locations.append(job_location)
    company_names.append(company_name)
    experience_required.append(exp_required)

# Create a DataFrame from the scraped data
job_data = pd.DataFrame({
    'Job Title': job_titles,
    'Job Location': job_locations,
    'Company Name': company_names,
    'Experience Required': experience_required
})

# Display the DataFrame
print(job_data)

# Close the browser
driver.quit()


# Write a python program to scrape data for “Data Scientist” Job position in“Bangalore” location. You
# have to scrape the job-title, job-location, company_name. You have to scrape first 10 jobs data.
# This task will be done in following steps:
# 1. First get the webpage https://www.shine.com/
# 2. Enter “Data Scientist” in “Job title, Skills” field and enter “Bangalore” in “enter thelocation” field.
# 3. Then click the search button.
# 4. Then scrape the data for the first 10 jobs results you get.
# 5. Finally create a dataframe of the scraped data.

# In[21]:


import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import pandas as pd

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Navigate to the Shine.com website
driver.get("https://www.shine.com/")

# Find the job title and location search fields and enter the values
job_title_input = driver.find_element_by_id("search")
location_input = driver.find_element_by_id("l")
search_button = driver.find_element_by_id("jb_form_btn")

job_title_input.send_keys("Data Scientist")
location_input.send_keys("Bangalore")
search_button.click()

# Wait for the search results to load
time.sleep(5)

# Get the page source after the search
page_source = driver.page_source

# Parse the page source with BeautifulSoup
soup = BeautifulSoup(page_source, "html.parser")

# Find job listings on the page
job_listings = soup.find_all("div", class_="w-90 d-inline-block")

# Create lists to store the scraped data
job_titles = []
job_locations = []
company_names = []

# Loop through the job listings and extract the data for the first 10 jobs
for job in job_listings[:10]:
    job_title = job.find("a", class_="w-90").text.strip()
    job_location = job.find("div", class_="search_listing").find("span").text.strip()
    company_name = job.find_all("span")[1].text.strip()

    job_titles.append(job_title)
    job_locations.append(job_location)
    company_names.append(company_name)

# Create a DataFrame from the scraped data
job_data = pd.DataFrame({
    'Job Title': job_titles,
    'Job Location': job_locations,
    'Company Name': company_names
})

# Display the DataFrame
print(job_data)

# Close the browser
driver.quit()


# Q3: Write a python program to scrape data for “Data Scientist” Job position in “Delhi/NCR” location. You have to use the location and salary filter.
# You have to scrape data for “Data Scientist” designation for first 10 job results.
# You have to scrape the job-title, job-location, company name, experience required.
# The location filter to be used is “Delhi/NCR”. The salary filter to be used is “3-6” lakhs
# The task will be done as shown in the below steps:
# 1. first get the web page https://www.shine.com/
# 2. Enter “Data Scientist” in “Skill, Designations, and Companies” field.
# 3. Then click the search button.
# 4. Then apply the location filter and salary filter by checking the respective boxes
# 5. Then scrape the data for the first 10 jobs results you get.
# 6. Finally create a dataframe of the scraped data.

# In[26]:


# Importing the required libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

# Setting the base url and the search parameters
base_url = "https://www.shine.com/"
search_params = {"q": "Data Scientist", "loc": "Delhi/NCR", "minsalary": "3", "maxsalary": "6"}

# Creating a webdriver object and opening the base url
driver = webdriver.Chrome()
driver.get(base_url)

# Finding the search box and entering the query
search_box = driver.find_element_by_id("id_q")
search_box.send_keys(search_params["q"])

# Finding the search button and clicking it
search_button = driver.find_element_by_id("id_search")
search_button.click()

# Waiting for the page to load and finding the location filter
wait = WebDriverWait(driver, 10)
location_filter = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Location']")))

# Clicking the location filter and finding the checkbox for Delhi/NCR
location_filter.click()
delhi_ncr_checkbox = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[text()='Delhi/NCR']")))

# Checking the checkbox for Delhi/NCR and finding the apply button
delhi_ncr_checkbox.click()
apply_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Apply']")))

# Clicking the apply button and finding the salary filter
apply_button.click()
salary_filter = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Salary']")))

# Clicking the salary filter and finding the checkbox for 3-6 lakhs
salary_filter.click()
three_six_lakhs_checkbox = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[text()='3-6 Lakhs']")))

# Checking the checkbox for 3-6 lakhs and clicking the apply button
three_six_lakhs_checkbox.click()
apply_button.click()

# Waiting for the page to load and finding the div elements that contain the job details
job_divs = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "result-display__profile")))

# Creating empty lists to store the scraped data
job_titles = []
job_locations = []
company_names = []
experience_required = []

# Looping through the first 10 job divs
for job_div in job_divs[:10]:
    # Finding the job title and appending it to the list
    job_title = job_div.find_element_by_class_name("job_title_anchor").text.strip()
    job_titles.append(job_title)

    # Finding the job location and appending it to the list
    job_location = job_div.find_element_by_class_name("result-display__profile__years").text.strip()
    job_locations.append(job_location)

    # Finding the company name and appending it to the list
    company_name = job_div.find_element_by_class_name("result-display__profile__name").text.strip()
    company_names.append(company_name)

    # Finding the experience required and appending it to the list
    experience = job_div.find_element_by_class_name("result-display__profile__experience").text.strip()
    experience_required.append(experience)

# Creating a dataframe of the scraped data
df = pd.DataFrame({"Job Title": job_titles, "Job Location": job_locations, "Company Name": company_names, "Experience Required": experience_required})

# Printing the dataframe
print(df)

# Closing the driver
driver.close()


# Q4: Scrape data of first 100 sunglasses listings on flipkart.com. You have to scrape four attributes:
# Brand
# ProductDescription
# Price
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
# 6. Repeat this until you get data for 100sunglasses

# Question 5: Scrape 100 reviews data from flipkart.com for iphone11 phone. You have to go the link:
# https://www.flipkart.com/apple-iphone-11-black-64-gb/p/itm4e5041ba101fd?pid=MOBFWQ6BXGJCEYNY&lid=LSTMOBFWQ6BXGJCEYNYZE3ENS&marketplace=FLIPKART&q=iphone+11&store=tyy/4io&srno=s_1_1&otracker=AS_Query_HistoryAutoSuggest_6_0_na_na_na&otracker1=AS_Query_HistoryAutoSuggest_6_0_na_na_na&fm=organic&iid=e30aaa70-fe6e-466c-81d4-993e630ea913.MOBFWQ6BXGJCEYNY.SEARCH&ppt=hp&ppn=homepage&ssid=nseg9l47e80000001699187524593&qH=f6cdfdaa9f3c23f3
# place=FLIPKART
# 
# You have to scrape the tick marked attributes. These are:
# 1. Rating
# 2. Review summary
# 3. Full review
# 4. You have to scrape this data for first 100reviews.

# In[27]:


# Importing the required libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

# Setting the base url and the search query
base_url = "https://www.flipkart.com/"
search_query = "sunglasses"

# Creating a webdriver object and opening the base url
driver = webdriver.Chrome()
driver.get(base_url)

# Finding the search box and entering the query
search_box = driver.find_element_by_class_name("_3704LK")
search_box.send_keys(search_query)

# Finding the search button and clicking it
search_button = driver.find_element_by_class_name("L0Z3Pu")
search_button.click()

# Waiting for the page to load and finding the sunglasses elements
wait = WebDriverWait(driver, 10)
sunglasses = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "_2B099V")))

# Creating empty lists to store the scraped data
brands = []
descriptions = []
prices = []

# Setting a counter to keep track of the number of sunglasses scraped
count = 0

# Looping until 100 sunglasses are scraped
while count < 100:
    # Looping through each sunglasses element on the current page
    for sunglasses_element in sunglasses:
        # Finding the brand name and appending it to the list
        brand = sunglasses_element.find_element_by_class_name("_2WkVRV").text
        brands.append(brand)

        # Finding the product description and appending it to the list
        description = sunglasses_element.find_element_by_class_name("IRpwTa").text
        descriptions.append(description)

        # Finding the price and appending it to the list
        price = sunglasses_element.find_element_by_class_name("_30jeq3").text
        prices.append(price)

        # Incrementing the counter by 1
        count += 1

        # Breaking the loop if 100 sunglasses are scraped
        if count == 100:
            break

    # Finding the next button and clicking it if it exists
    try:
        next_button = driver.find_element_by_class_name("_1LKTO3")
        next_button.click()

        # Waiting for the next page to load and finding the sunglasses elements
        wait = WebDriverWait(driver, 10)
        sunglasses = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "_2B099V")))
    except:
        # Printing an error message if the next button is not found
        print("No more pages to scrape. Stopping the program.")
        break

# Creating a dataframe of the scraped data
df = pd.DataFrame({"Brand": brands, "Product Description": descriptions, "Price": prices})

# Printing the dataframe
print(df)

# Closing the driver
driver.close()


# Q6: Scrape data forfirst 100 sneakers you find whenyou visit flipkart.com and search for “sneakers” inthe
# search field.
# You have to scrape 3 attributes of each sneaker:
# 1. Brand
# 2. ProductDescription
# 3. Price

# In[28]:


# Importing the required libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

# Setting the base url and the search query
base_url = "https://www.flipkart.com/"
search_query = "sneakers"

# Creating a webdriver object and opening the base url
driver = webdriver.Chrome()
driver.get(base_url)

# Finding the search box and entering the query
search_box = driver.find_element_by_class_name("_3704LK")
search_box.send_keys(search_query)

# Finding the search button and clicking it
search_button = driver.find_element_by_class_name("L0Z3Pu")
search_button.click()

# Waiting for the page to load and finding the sneakers elements
wait = WebDriverWait(driver, 10)
sneakers = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "_2B099V")))

# Creating empty lists to store the scraped data
brands = []
descriptions = []
prices = []

# Setting a counter to keep track of the number of sneakers scraped
count = 0

# Looping until 100 sneakers are scraped
while count < 100:
    # Looping through each sneakers element on the current page
    for sneakers_element in sneakers:
        # Finding the brand name and appending it to the list
        brand = sneakers_element.find_element_by_class_name("_2WkVRV").text
        brands.append(brand)

        # Finding the product description and appending it to the list
        description = sneakers_element.find_element_by_class_name("IRpwTa").text
        descriptions.append(description)

        # Finding the price and appending it to the list
        price = sneakers_element.find_element_by_class_name("_30jeq3").text
        prices.append(price)

        # Incrementing the counter by 1
        count += 1

        # Breaking the loop if 100 sneakers are scraped
        if count == 100:
            break

    # Finding the next button and clicking it if it exists
    try:
        next_button = driver.find_element_by_class_name("_1LKTO3")
        next_button.click()

        # Waiting for the next page to load and finding the sneakers elements
        wait = WebDriverWait(driver, 10)
        sneakers = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "_2B099V")))
    except:
        # Printing an error message if the next button is not found
        print("No more pages to scrape. Stopping the program.")
        break

# Creating a dataframe of the scraped data
df = pd.DataFrame({"Brand": brands, "Product Description": descriptions, "Price": prices})

# Printing the dataframe
print(df)

# Closing the driver
driver.close()


# Q7: Go to webpage https://www.amazon.in/ Enter “Laptop” in the search field and then click the search icon. Then
# set CPU Type filter to “Intel Core i7” as shown in the below image:
#     After setting the filters scrape first 10 laptops data. You have to scrape 3 attributes for each laptop:
# 1. Title
# 2. Ratings
# 3. Price

# In[29]:


# Importing the required libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

# Setting the base url and the search query
base_url = "https://www.amazon.in/"
search_query = "Laptop"

# Creating a webdriver object and opening the base url
driver = webdriver.Chrome()
driver.get(base_url)

# Finding the search box and entering the query
search_box = driver.find_element_by_id("twotabsearchtextbox")
search_box.send_keys(search_query)

# Finding the search button and clicking it
search_button = driver.find_element_by_id("nav-search-submit-button")
search_button.click()

# Waiting for the page to load and finding the CPU type filter
wait = WebDriverWait(driver, 10)
cpu_type_filter = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Intel Core i7']")))

# Clicking the CPU type filter
cpu_type_filter.click()

# Waiting for the page to load and finding the laptop elements
laptops = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "s-result-item")))

# Creating empty lists to store the scraped data
titles = []
ratings = []
prices = []

# Looping through the first 10 laptop elements
for laptop in laptops[:10]:
    # Finding the title and appending it to the list
    title = laptop.find_element_by_class_name("a-size-medium").text
    titles.append(title)

    # Finding the rating and appending it to the list
    try:
        rating = laptop.find_element_by_class_name("a-icon-alt").get_attribute("aria-label")
        ratings.append(rating)
    except:
        # If no rating is found, appending "No rating" to the list
        ratings.append("No rating")

    # Finding the price and appending it to the list
    try:
        price = laptop.find_element_by_class_name("a-price-whole").text
        prices.append(price)
    except:
        # If no price is found, appending "No price" to the list
        prices.append("No price")

# Creating a dataframe of the scraped data
df = pd.DataFrame({"Title": titles, "Rating": ratings, "Price": prices})

# Printing the dataframe
print(df)

# Closing the driver
driver.close()


# Q8: Write a python program to scrape data for Top 1000 Quotes of All Time.
# The above task will be done in following steps:
# 1. First get the webpagehttps://www.azquotes.com/
# 2. Click on TopQuotes
# 3. Than scrap a) Quote b) Author c) Type Of Quotes

# In[30]:


# Importing the required libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

# Setting the base url and the number of quotes to scrape
base_url = "https://www.azquotes.com/"
num_quotes = 1000

# Creating a webdriver object and opening the base url
driver = webdriver.Chrome()
driver.get(base_url)

# Finding the top quotes button and clicking it
top_quotes_button = driver.find_element_by_link_text("Top Quotes")
top_quotes_button.click()

# Waiting for the page to load and finding the quote elements
wait = WebDriverWait(driver, 10)
quotes = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "wrap-block")))

# Creating empty lists to store the scraped data
quote_texts = []
quote_authors = []
quote_types = []

# Setting a counter to keep track of the number of quotes scraped
count = 0

# Looping until 1000 quotes are scraped
while count < num_quotes:
    # Looping through each quote element on the current page
    for quote in quotes:
        # Finding the quote text and appending it to the list
        quote_text = quote.find_element_by_class_name("title").text
        quote_texts.append(quote_text)

        # Finding the quote author and appending it to the list
        quote_author = quote.find_element_by_class_name("author").text
        quote_authors.append(quote_author)

        # Finding the quote type and appending it to the list
        quote_type = quote.find_element_by_class_name("cat").text
        quote_types.append(quote_type)

        # Incrementing the counter by 1
        count += 1

        # Breaking the loop if 1000 quotes are scraped
        if count == num_quotes:
            break

    # Finding the next button and clicking it if it exists
    try:
        next_button = driver.find_element_by_link_text("Next")
        next_button.click()

        # Waiting for the next page to load and finding the quote elements
        wait = WebDriverWait(driver, 10)
        quotes = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "wrap-block")))
    except:
        # Printing an error message if the next button is not found
        print("No more pages to scrape. Stopping the program.")
        break

# Creating a dataframe of the scraped data
df = pd.DataFrame({"Quote": quote_texts, "Author": quote_authors, "Type": quote_types})

# Printing the dataframe
print(df)

# Closing the driver
driver.close()


# Q9: Write a python program to display list of respected former Prime Ministers of India(i.e. Name, Born-Dead,
# Term of office, Remarks) from https://www.jagranjosh.com/.
# This task will be done in following steps:
# 1. First get the webpagehttps://www.jagranjosh.com/
# 2. Then You have to click on the GK option
# 3. Then click on the List of all Prime Ministers of India
# 4. Then scrap the mentioned data and make theDataFrame.

# In[31]:


# Importing the required libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

# Setting the base url and the article url
base_url = "https://www.jagranjosh.com/"
article_url = "https://www.jagranjosh.com/general-knowledge/list-of-all-prime-ministers-of-india-1378370"

# Creating a webdriver object and opening the base url
driver = webdriver.Chrome()
driver.get(base_url)

# Finding the GK option and clicking it
gk_option = driver.find_element_by_link_text("GK")
gk_option.click()

# Waiting for the page to load and finding the article link
wait = WebDriverWait(driver, 10)
article_link = wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "List of all Prime Ministers of India")))

# Clicking the article link
article_link.click()

# Waiting for the page to load and finding the table element
table = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "tableizer-table")))

# Creating empty lists to store the scraped data
names = []
born_dead = []
term_of_office = []
remarks = []

# Finding the table rows and looping through them
table_rows = table.find_elements_by_tag_name("tr")
for table_row in table_rows:
    # Finding the table cells and extracting the text
    table_cells = table_row.find_elements_by_tag_name("td")
    name = table_cells[0].text
    born_dead = table_cells[1].text
    term_of_office = table_cells[2].text
    remark = table_cells[3].text

    # Appending the text to the lists
    names.append(name)
    born_dead.append(born_dead)
    term_of_office.append(term_of_office)
    remarks.append(remark)

# Creating a dataframe of the scraped data
df = pd.DataFrame({"Name": names, "Born-Dead": born_dead, "Term of office": term_of_office, "Remark": remarks})

# Printing the dataframe
print(df)

# Closing the driver
driver.close()


# Q10: Write a python program to display list of 50 Most expensive cars in the world (i.e.
# Car name and Price) from https://www.motor1.com/
# This task will be done in following steps:
# 1. First get the webpage https://www.motor1.com/
# 2. Then You have to type in the search bar ’50 most expensive cars’
# 3. Then click on 50 most expensive carsin the world..
# 4. Then scrap the mentioned data and make the dataframe.

# In[32]:


# Importing the required libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

# Setting the base url and the search query
base_url = "https://www.motor1.com/"
search_query = "50 most expensive cars"

# Creating a webdriver object and opening the base url
driver = webdriver.Chrome()
driver.get(base_url)

# Finding the search bar and entering the query
search_bar = driver.find_element_by_class_name("search-icon")
search_bar.click()
search_box = driver.find_element_by_id("search-input")
search_box.send_keys(search_query)

# Finding the search button and clicking it
search_button = driver.find_element_by_class_name("search-button")
search_button.click()

# Waiting for the page to load and finding the article link
wait = WebDriverWait(driver, 10)
article_link = wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "50 Most Expensive Cars In The World")))

# Clicking the article link
article_link.click()

# Waiting for the page to load and finding the car elements
cars = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "listicle-item")))

# Creating empty lists to store the scraped data
car_names = []
car_prices = []

# Looping through each car element
for car in cars:
    # Finding the car name and appending it to the list
    car_name = car.find_element_by_class_name("listicle-item-title").text
    car_names.append(car_name)

    # Finding the car price and appending it to the list
    car_price = car.find_element_by_class_name("listicle-item-subtitle").text
    car_prices.append(car_price)

# Creating a dataframe of the scraped data
df = pd.DataFrame({"Car Name": car_names, "Price": car_prices})

# Printing the dataframe
print(df)

# Closing the driver
driver.close()


# In[ ]:




