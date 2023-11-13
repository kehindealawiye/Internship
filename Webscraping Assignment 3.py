#!/usr/bin/env python
# coding: utf-8

# Q1: Write a python program which searches all the product under a particular product from www.amazon.in. The 
# product to be searched will be taken as input from user. For e.g. If user input is ‘guitar’. Then search for 
# guitars

# In[ ]:


import requests
from bs4 import BeautifulSoup

def search_amazon_product(product_name):
    base_url = "https://www.amazon.in/s?k="

    # Replace spaces in the product name with '+'
    formatted_product_name = '+'.join(product_name.split())

    # Construct the search URL
    search_url = f"{base_url}{formatted_product_name}"

    # Send an HTTP request to the Amazon website
    response = requests.get(search_url)

    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract product details, you may need to inspect the HTML structure of the Amazon page to get accurate details
        # For demonstration purposes, let's just print the product titles
        product_titles = soup.select('.s-title-instructions h2 a span')
        
        for index, title in enumerate(product_titles, start=1):
            print(f"{index}. {title.text}")

    else:
        print(f"Error: Unable to fetch data. Status code: {response.status_code}")

if __name__ == "__main__":
    # Take user input for the product to be searched
    user_input = input("Enter the product to search on Amazon: ")
    
    # Call the function to search Amazon for the specified product
    search_amazon_product(user_input)


# Q2: In the above question, now scrape the following details of each product listed in first 3 pages of your search 
# results and save it in a data frame and csv. In case if any product has less than 3 pages in search results then 
# scrape all the products available under that product name. Details to be scraped are: "Brand 
# Name", "Name of the Product", "Price", "Return/Exchange", "Expected Delivery", "Availability" and 
# “Product URL”. In case, if any of the details are missing for any of the product then replace it by “-“. 

# In[ ]:


import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_product_details(product_url):
    # Send an HTTP request to the product page
    response = requests.get(product_url)

    if response.status_code == 200:
        # Parse the HTML content of the product page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract the required details, modify as needed based on the Amazon page structure
        brand_name = soup.select_one('.a-spacing-none #bylineInfo').get_text(strip=True) if soup.select_one('.a-spacing-none #bylineInfo') else '-'
        product_name = soup.select_one('.a-size-large span').get_text(strip=True) if soup.select_one('.a-size-large span') else '-'
        price = soup.select_one('.a-offscreen').get_text(strip=True) if soup.select_one('.a-offscreen') else '-'
        return_exchange = soup.select_one('#icon-plus span.a-declarative span.a-size-base').get_text(strip=True) if soup.select_one('#icon-plus span.a-declarative span.a-size-base') else '-'
        expected_delivery = soup.select_one('.a-section #ddmDeliveryMessage span.a-declarative span.a-size-medium').get_text(strip=True) if soup.select_one('.a-section #ddmDeliveryMessage span.a-declarative span.a-size-medium') else '-'
        availability = soup.select_one('#availability span.a-declarative span.a-size-medium').get_text(strip=True) if soup.select_one('#availability span.a-declarative span.a-size-medium') else '-'

        # Return the scraped details
        return brand_name, product_name, price, return_exchange, expected_delivery, availability

    else:
        print(f"Error: Unable to fetch data for product URL: {product_url}. Status code: {response.status_code}")
        return '-', '-', '-', '-', '-', '-'

def search_amazon_product(product_name, num_pages=3):
    base_url = "https://www.amazon.in/s?k="

    # Replace spaces in the product name with '+'
    formatted_product_name = '+'.join(product_name.split())

    product_details_list = []

    # Iterate through specified number of pages or until there are no more pages
    for page_num in range(1, num_pages + 1):
        # Construct the search URL with page number
        search_url = f"{base_url}{formatted_product_name}&page={page_num}"

        # Send an HTTP request to the Amazon website
        response = requests.get(search_url)

        if response.status_code == 200:
            # Parse the HTML content of the page
            soup = BeautifulSoup(response.text, 'html.parser')

            # Extract product URLs
            product_links = [a['href'] for a in soup.select('.s-title-instructions h2 a')]

            # Scrape details for each product URL
            for product_url in product_links:
                details = scrape_product_details("https://www.amazon.in" + product_url)
                product_details_list.append(details)

        else:
            print(f"Error: Unable to fetch data. Status code: {response.status_code}")

    # Create a DataFrame with the scraped details
    columns = ["Brand Name", "Name of the Product", "Price", "Return/Exchange", "Expected Delivery", "Availability"]
    df = pd.DataFrame(product_details_list, columns=columns)

    # Add "Product URL" column to the DataFrame
    df["Product URL"] = ["https://www.amazon.in" + link for link in product_links]

    # Save the DataFrame to a CSV file
    df.to_csv(f"{formatted_product_name}_search_results.csv", index=False)

if __name__ == "__main__":
    # Take user input for the product to be searched
    user_input = input("Enter the product to search on Amazon: ")
    
    # Call the function to search Amazon for the specified product and scrape details
    search_amazon_product(user_input)


# Q3: Write a python program to access the search bar and search button on images.google.com and scrape 10 
# images each for keywords ‘fruits’, ‘cars’ and ‘Machine Learning’, ‘Guitar’, ‘Cakes’.

# In[ ]:


from selenium import webdriver
import time

# Create a new Chrome browser instance
driver = webdriver.Chrome()

# Define the keywords to search for
keywords = ['fruits', 'cars', 'Machine Learning', 'Guitar', 'Cakes']

# Loop through each keyword and scrape 10 images
for keyword in keywords:
    # Navigate to the Google Images website
    driver.get('https://images.google.com/')
    time.sleep(2)

    # Find the search bar and enter the keyword
    search_bar = driver.find_element_by_name('q')
    search_bar.send_keys(keyword)

    # Click the search button
    search_button = driver.find_element_by_css_selector('button[type="submit"]')
    search_button.click()
    time.sleep(2)

    # Scroll down to load more images
    for i in range(5):
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        time.sleep(2)

    # Scrape the first 10 images
    images = driver.find_elements_by_css_selector('img.rg_i')
    for i in range(10):
        image_url = images[i].get_attribute('src')
        print(f'{keyword} image {i+1}: {image_url}')

# Close the browser
driver.quit()


# Q4: Write a python program to search for a smartphone(e.g.: Oneplus Nord, pixel 4A, etc.) on www.flipkart.com
# and scrape following details for all the search results displayed on 1st page. Details to be scraped: “Brand 
# Name”, “Smartphone name”, “Colour”, “RAM”, “Storage(ROM)”, “Primary Camera”, 
# “Secondary Camera”, “Display Size”, “Battery Capacity”, “Price”, “Product URL”. Incase if any of the 
# details is missing then replace it by “- “. Save your results in a dataframe and CSV.

# In[ ]:


import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

# Create a new Chrome browser instance
driver = webdriver.Chrome()

# Define the URL to scrape
url = 'https://www.flipkart.com/'

# Define the search query
search_query = 'Oneplus Nord'

# Navigate to the Flipkart website
driver.get(url)

# Find the search bar and enter the search query
search_bar = driver.find_element(By.XPATH, '//input[@title="Search for products, brands and more"]')
search_bar.send_keys(search_query)

# Click the search button
search_button = driver.find_element(By.XPATH, '//button[@type="submit"]')
search_button.click()

# Wait for the search results to load
driver.implicitly_wait(10)

# Scrape the details for each search result
results = driver.find_elements(By.XPATH, '//div[@class="_2kHMtA"]')
data = []
for result in results:
    try:
        brand_name = result.find_element(By.XPATH, './/div[@class="_4rR01T"]').text
    except:
        brand_name = '-'
    try:
        smartphone_name = result.find_element(By.XPATH, './/a[contains(@class,"_1fQZEK")]/div').text
    except:
        smartphone_name = '-'
    try:
        color = result.find_element(By.XPATH, './/a[contains(@class,"_1fQZEK")]/div[2]').text
    except:
        color = '-'
    try:
        ram = result.find_element(By.XPATH, './/ul/li[1]').text
    except:
        ram = '-'
    try:
        storage = result.find_element(By.XPATH, './/ul/li[2]').text
    except:
        storage = '-'
    try:
        primary_camera = result.find_element(By.XPATH, './/ul/li[3]').text
    except:
        primary_camera = '-'
    try:
        secondary_camera = result.find_element(By.XPATH, './/ul/li[4]').text
    except:
        secondary_camera = '-'
    try:
        display_size = result.find_element(By.XPATH, './/ul/li[5]').text
    except:
        display_size = '-'
    try:
        battery_capacity = result.find_element(By.XPATH, './/ul/li[6]').text
    except:
        battery_capacity = '-'
    try:
        price = result.find_element(By.XPATH, './/div[@class="_30jeq3 _1_WHN1"]').text
    except:
        price = '-'
    try:
        product_url = result.find_element(By.XPATH, './/a[contains(@class,"_1fQZEK")]').get_attribute('href')
    except:
        product_url = '-'
    data.append([brand_name, smartphone_name, color, ram, storage, primary_camera, secondary_camera, display_size, battery_capacity, price, product_url])

# Create a dataframe from the scraped data
df = pd.DataFrame(data, columns=['Brand Name', 'Smartphone Name', 'Color', 'RAM', 'Storage(ROM)', 'Primary Camera', 'Secondary Camera', 'Display Size', 'Battery Capacity', 'Price', 'Product URL'])

# Save the dataframe to a CSV file
df.to_csv('smartphone_details.csv', index=False)

# Close the browser
driver.quit()


# Q5: Write a program to scrap geospatial coordinates (latitude, longitude) of a city searched on google maps.

# In[ ]:


from selenium import webdriver

# Create a new Chrome browser instance
driver = webdriver.Chrome()

# Define the city to search for
city = 'Lagos'

# Navigate to the Google Maps website
driver.get('https://www.google.com/maps')

# Find the search bar and enter the city
search_bar = driver.find_element_by_id('searchboxinput')
search_bar.send_keys(city)

# Click the search button
search_button = driver.find_element_by_id('searchbox-searchbutton')
search_button.click()

# Wait for the map to load
driver.implicitly_wait(10)

# Extract the latitude and longitude
url = driver.current_url
latitude = url.split('@')[1].split(',')[0]
longitude = url.split('@')[1].split(',')[1]

print(f'The geospatial coordinates of {city} are: {latitude}, {longitude}')

# Close the browser
driver.quit()


# Q6: Write a program to scrap all the available details of best gaming laptops from digit.in.

# In[ ]:


import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

# Create a new Chrome browser instance
driver = webdriver.Chrome()

# Define the URL to scrape
url = 'https://www.digit.in/top-products/best-gaming-laptops-40.html'

# Navigate to the Digit website
driver.get(url)

# Scrape the details for each laptop
results = driver.find_elements(By.XPATH, '//div[@class="TopNumbeHeading sticky-footer"]/following-sibling::ul/li')
data = []
for result in results:
    try:
        brand_name = result.find_element(By.XPATH, './/div[@class="TopNumbeHeading sticky-footer"]/following-sibling::h3').text
    except:
        brand_name = '-'
    try:
        laptop_name = result.find_element(By.XPATH, './/div[contains(text(),"Model Name")]/following-sibling::div').text
    except:
        laptop_name = '-'
    try:
        price = result.find_element(By.XPATH, './/div[contains(text(),"Price")]/following-sibling::div').text
    except:
        price = '-'
    try:
        os = result.find_element(By.XPATH, './/div[contains(text(),"OS")]/following-sibling::div').text
    except:
        os = '-'
    try:
        display_size = result.find_element(By.XPATH, './/div[contains(text(),"Display Size")]/following-sibling::div').text
    except:
        display_size = '-'
    try:
        processor = result.find_element(By.XPATH, './/div[contains(text(),"Processor")]/following-sibling::div').text
    except:
        processor = '-'
    try:
        ram = result.find_element(By.XPATH, './/div[contains(text(),"Memory")]/following-sibling::div').text
    except:
        ram = '-'
    try:
        storage = result.find_element(By.XPATH, './/div[contains(text(),"Storage")]/following-sibling::div').text
    except:
        storage = '-'
    try:
        graphics_card = result.find_element(By.XPATH, './/div[contains(text(),"Graphics Processor")]/following-sibling::div').text
    except:
        graphics_card = '-'
    try:
        weight = result.find_element(By.XPATH, './/div[contains(text(),"Weight")]/following-sibling::div').text
    except:
        weight = '-'
    try:
        dimensions = result.find_element(By.XPATH, './/div[contains(text(),"Dimension")]/following-sibling::div').text
    except:
        dimensions = '-'
    try:
        product_url = result.find_element(By.XPATH, './/a').get_attribute('href')
    except:
        product_url = '-'
    data.append([brand_name, laptop_name, price, os, display_size, processor, ram, storage, graphics_card, weight, dimensions, product_url])

# Create a dataframe from the scraped data
df = pd.DataFrame(data, columns=['Brand Name', 'Laptop Name', 'Price', 'OS', 'Display Size', 'Processor', 'RAM', 'Storage', 'Graphics Card', 'Weight', 'Dimensions', 'Product URL'])

# Save the dataframe to a CSV file
df.to_csv('gaming_laptops.csv', index=False)

# Close the browser
driver.quit()


# Q7: Write a python program to scrape the details for all billionaires from www.forbes.com. Details to be scrapped: 
# “Rank”, “Name”, “Net worth”, “Age”, “Citizenship”, “Source”, “Industry”. 

# In[ ]:


import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

# Create a new Chrome browser instance
driver = webdriver.Chrome()

# Define the URL to scrape
url = 'https://www.forbes.com/billionaires/'

# Navigate to the Forbes website
driver.get(url)

# Scrape the details for each billionaire
results = driver.find_elements(By.XPATH, '//div[@class="rank"]')
data = []
for result in results:
    try:
        rank = result.text
    except:
        rank = '-'
    try:
        name = result.find_element(By.XPATH, './following-sibling::div[1]').text
    except:
        name = '-'
    try:
        net_worth = result.find_element(By.XPATH, './following-sibling::div[2]').text
    except:
        net_worth = '-'
    try:
        age = result.find_element(By.XPATH, './following-sibling::div[3]').text
    except:
        age = '-'
    try:
        citizenship = result.find_element(By.XPATH, './following-sibling::div[4]').text
    except:
        citizenship = '-'
    try:
        source = result.find_element(By.XPATH, './following-sibling::div[5]').text
    except:
        source = '-'
    try:
        industry = result.find_element(By.XPATH, './following-sibling::div[6]').text
    except:
        industry = '-'
    data.append([rank, name, net_worth, age, citizenship, source, industry])

# Create a dataframe from the scraped data
df = pd.DataFrame(data, columns=['Rank', 'Name', 'Net Worth', 'Age', 'Citizenship', 'Source', 'Industry'])

# Save the dataframe to a CSV file
df.to_csv('billionaires_details.csv', index=False)

# Close the browser
driver.quit()


# Q8: Write a program to extract at least 500 Comments, Comment upvote and time when comment was posted 
# from any YouTube Video. 

# In[ ]:


from selenium import webdriver
import time

# Create a new Chrome browser instance
driver = webdriver.Chrome()

# Define the URL of the YouTube video to scrape
url = 'https://www.youtube.com/watch?v=5qap5aO4i9A'

# Navigate to the YouTube video page
driver.get(url)

# Scroll down to load more comments
for i in range(10):
    driver.execute_script('window.scrollTo(0, document.documentElement.scrollHeight);')
    time.sleep(2)

# Extract the comments, comment upvotes and time when comment was posted
comments = driver.find_elements_by_xpath('//*[@id="content-text"]')
comment_upvotes = driver.find_elements_by_xpath('//*[@id="vote-count-middle"]')
comment_times = driver.find_elements_by_xpath('//*[@id="header-author"]/yt-formatted-string/a')

# Print the comments, comment upvotes and time when comment was posted
for i in range(len(comments)):
    print(f'Comment {i+1}: {comments[i].text}')
    print(f'Comment Upvotes: {comment_upvotes[i].text}')
    print(f'Time When Comment Was Posted: {comment_times[i].text}')
    print('\n')

# Close the browser
driver.quit()


# Q9: Write a python program to scrape a data for all available Hostels from https://www.hostelworld.com/ in 
# “London” location. You have to scrape hostel name, distance from city centre, ratings, total reviews, overall 
# reviews, privates from price, dorms from price, facilities and property description.

# In[ ]:


import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

# Create a new Chrome browser instance
driver = webdriver.Chrome()

# Define the URL to scrape
url = 'https://www.hostelworld.com/'

# Navigate to the Hostelworld website
driver.get(url)

# Find the search bar and enter the location
search_bar = driver.find_element(By.XPATH, '//input[@id="search-input-field"]')
search_bar.send_keys('London')

# Click the search button
search_button = driver.find_element(By.XPATH, '//button[@id="search-button"]')
search_button.click()

# Wait for the search results to load
driver.implicitly_wait(10)

# Scrape the details for each hostel
results = driver.find_elements(By.XPATH, '//div[@class="property-card"]')
data = []
for result in results:
    try:
        hostel_name = result.find_element(By.XPATH, './/h2/a').text
    except:
        hostel_name = '-'
    try:
        distance_from_city_centre = result.find_element(By.XPATH, './/a/span').text
    except:
        distance_from_city_centre = '-'
    try:
        ratings = result.find_element(By.XPATH, './/div[contains(@class,"score")]/span').text
    except:
        ratings = '-'
    try:
        total_reviews = result.find_element(By.XPATH, './/div[contains(text(),"Total Reviews")]/span').text
    except:
        total_reviews = '-'
    try:
        overall_reviews = result.find_element(By.XPATH, './/div[contains(text(),"Overall Reviews")]/span').text
    except:
        overall_reviews = '-'
    try:
        privates_from_price = result.find_element(By.XPATH, './/div[contains(text(),"Privates From")]/span').text
    except:
        privates_from_price = '-'
    try:
        dorms_from_price = result.find_element(By.XPATH, './/div[contains(text(),"Dorms From")]/span').text
    except:
        dorms_from_price = '-'
    try:
        facilities = result.find_element(By.XPATH, './/div[contains(@class,"facilities-label")]/following-sibling::div').text
    except:
        facilities = '-'
    try:
        property_description = result.find_element(By.XPATH, './/div[contains(@class,"description")]').text
    except:
        property_description = '-'
    data.append([hostel_name, distance_from_city_centre, ratings, total_reviews, overall_reviews, privates_from_price, dorms_from_price, facilities, property_description])

# Create a dataframe from the scraped data
df = pd.DataFrame(data, columns=['Hostel Name', 'Distance from City Centre', 'Ratings', 'Total Reviews', 'Overall Reviews', 'Privates from Price', 'Dorms from Price', 'Facilities', 'Property Description'])

# Save the dataframe to a CSV file
df.to_csv('hostel_details.csv', index=False)

# Close the browser
driver.quit()

