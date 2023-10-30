#!/usr/bin/env python
# coding: utf-8

# # Question 1: Write a python program to display all the header tags from wikipedia.org and make data frame.

# In[7]:


import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://en.wikipedia.org/wiki/Main_Page"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all header tags (h1, h2, h3, h4, h5, h6)
    header_tags = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])

    header_text = [tag.get_text() for tag in header_tags]

    df = pd.DataFrame(header_text, columns=['Header'])
    


# In[8]:


df


# # Question 2: Write a python program to display list of respected former presidents of India(i.e. Name , Term of office)
# from https://presidentofindia.nic.in/former-presidents.htm and make data frame

# In[57]:


import requests
import pandas as pd
from bs4 import BeautifulSoup

Presidentsurl = "https://presidentofindia.nic.in/former-presidents"

response = requests.get(Presidentsurl)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "lxml")

    entries = soup.find_all("div", class_="desc-sec")

    for entry in entries:
        name = entry.find("h3").text.strip()
        term = entry.find("h5").text.strip()
        names.append(name)
        terms.append(term)

    # Create a DataFrame
    df = pd.DataFrame({"Name": names, "Term of Office": terms})


# In[58]:


df


# # Question 3: Write a python program to scrape cricket rankings from icc-cricket.com. You have to scrape and make data frame. .
# a) Top 10 ODI teams in men’s cricket along with the records for matches, points and rating
# b) Top 10 ODI Batsmen along with the records of their team and rating.
# c) Top 10 ODI bowlers along with the records of their team and rating

# In[79]:


import requests
import pandas as pd
from bs4 import BeautifulSoup

# Function to scrape and create a DataFrame for the provided URL
def scrape_and_create_dataframe(url, columns):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")

        # Find the table containing the rankings
        table = soup.find("table")

        # Initialize lists to store data
        data = []

        # Iterate through the rows to extract data
        for row in table.find_all("tr")[1:11]:  # Extract top 10 rows
            columns_data = row.find_all("td")
            row_data = [col.get_text(strip=True) for col in columns_data]
            data.append(row_data)

        # Create a DataFrame
        df = pd.DataFrame(data, columns=columns)

        return df

    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
        return None

# Function to scrape top 10 ODI teams
def scrape_odi_teams():
    odi_teams_url = "https://www.icc-cricket.com/rankings/mens/team-rankings/odi"
    odi_teams_columns = ["Position", "Team", "Matches", "Points", "Rating"]
    return scrape_and_create_dataframe(odi_teams_url, odi_teams_columns)

# Function to scrape top 10 ODI Batsmen
def scrape_odi_batsmen():
    odi_batsmen_url = "https://www.icc-cricket.com/rankings/mens/player-rankings/odi/batting"
    odi_batsmen_columns = ["Position", "Player", "Team", "Rating", "Career Best Rating"]
    return scrape_and_create_dataframe(odi_batsmen_url, odi_batsmen_columns)

# Function to scrape top 10 ODI Bowlers
def scrape_odi_bowlers():
    odi_bowlers_url = "https://www.icc-cricket.com/rankings/mens/player-rankings/odi/bowling"
    odi_bowlers_columns = ["Position", "Player", "Team", "Rating", "Career Best Rating"]
    return scrape_and_create_dataframe(odi_bowlers_url, odi_bowlers_columns)

# Scrape and print the DataFrames
odi_teams_df = scrape_odi_teams()
if odi_teams_df is not None:
    print("Top 10 ODI Teams:")
    print(odi_teams_df)

odi_batsmen_df = scrape_odi_batsmen()
if odi_batsmen_df is not None:
    print("Top 10 ODI Batsmen:")
    print(odi_batsmen_df)

odi_bowlers_df = scrape_odi_bowlers()
if odi_bowlers_df is not None:
    print("Top 10 ODI Bowlers:")
    print(odi_bowlers_df)


# In[83]:


odi_teams_df


# In[84]:


odi_batsmen_df


# In[85]:


odi_bowlers_df


# # Question 4: Write a python program to scrape cricket rankings from icc-cricket.com. You have to scrape and make data frame
# a) Top 10 ODI teams in women’s cricket along with the records for matches, points and rating.
# b) Top 10 women’s ODI Batting players along with the records of their team and rating.
# c) Top 10 women’s ODI all-rounder along with the records of their team and rating.
# 

# In[88]:


import requests
import pandas as pd
from bs4 import BeautifulSoup

# Function to scrape and create a DataFrame for the provided URL
def scrape_and_create_dataframe(url, columns):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")

        # Find the table containing the rankings
        table = soup.find("table")

        # Initialize lists to store data
        data = []

        # Iterate through the rows to extract data
        for row in table.find_all("tr")[1:11]:  # Extract top 10 rows
            columns_data = row.find_all("td")
            row_data = [col.get_text(strip=True) for col in columns_data]
            data.append(row_data)

        # Create a DataFrame
        df = pd.DataFrame(data, columns=columns)

        return df

    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
        return None

# Function to scrape top 10 ODI teams
def scrape_women_odi_teams():
    women_odi_teams_url = "https://www.icc-cricket.com/rankings/womens/team-rankings/odi"
    women_odi_teams_columns = ["Position", "Team", "Matches", "Points", "Rating"]
    return scrape_and_create_dataframe(women_odi_teams_url, women_odi_teams_columns)

# Function to scrape top 10 Women's ODI Batling Players
def scrape_women_odi_batting():
    women_odi_batting_url = "https://www.icc-cricket.com/rankings/womens/player-rankings/odi/batting"
    women_odi_batting_columns = ["Position", "Player", "Team", "Rating", "Career Best Rating"]
    return scrape_and_create_dataframe(women_odi_batting_url, women_odi_batting_columns)

# Function to scrape top 10 Women's ODI All-Rounders
def scrape_women_odi_allrounders():
    women_odi_allrounders_url = "https://www.icc-cricket.com/rankings/womens/player-rankings/odi/all-rounder"
    women_odi_allrounders_columns = ["Position", "Player", "Team", "Rating", "Career Best Rating"]
    return scrape_and_create_dataframe(women_odi_allrounders_url, women_odi_allrounders_columns)

# Scrape and print the DataFrames
women_odi_teams_df = scrape_women_odi_teams()
if women_odi_teams_df is not None:
    print("Top 10 Women ODI Teams:")
    print(women_odi_teams_df)

women_odi_batting_df = scrape_women_odi_batting()
if women_odi_batting_df is not None:
    print("Top 10 Women ODI Batting:")
    print(women_odi_batting_df)

women_odi_allrounders_df = scrape_women_odi_allrounders()
if women_odi_allrounders_df is not None:
    print("Top 10 Women ODI allrounders:")
    print(women_odi_allrounders_df)


# In[89]:


women_odi_teams_df


# In[90]:


women_odi_batting_df


# In[91]:


women_odi_allrounders_df


# # Question 5: Write a python program to scrape mentioned news details from https://www.cnbc.com/world/?region=world and make data frame
# 
# i) Headline
# ii) Time
# iii) News Link

# In[115]:


import requests
from bs4 import BeautifulSoup
import pandas as pd

# Send an HTTP GET request to the website
url = "https://www.cnbc.com/world/?region=world"
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find the elements containing the news details
    news_elements = soup.find_all('div', class_='RiverPlusCard-container')
    
    # Initialize lists to store data
    headlines = []
    times = []
    news_links = []
    
    # Extract data from the elements
    for news in news_elements:
        headline = news.text.strip()
        time = news.find_next('time').text.strip()
        link = news.find('a')['href']
        
        headlines.append(headline)
        times.append(time)
        news_links.append(link)
    
    # Create a DataFrame
    data = {
        'Headline': headlines,
        'Time': times,
        'News Link': news_links
    }
    df = pd.DataFrame(data)
    
    # Print the DataFrame
    print(df)
    
else:
    print("Failed to retrieve the webpage. Status code:", response.status_code)


# # Question 6: Write a python program to scrape the details of most downloaded articles from AI in last 90 days.
# https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles
# 
# Scrape below mentioned details and make data frame
# i) Paper Title
# ii) Authors
# iii) Published Date
# iv) Paper URL
# 

# In[148]:


import requests
from bs4 import BeautifulSoup
import pandas as pd

# Function to scrape and create a DataFrame for the provided URL
def scrape_and_create_dataframe(url):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")

        # Find the container containing the articles
        articles_container = soup.find("div", class_="sc-1g5fvti-2.clFnAZ")  # Update this class name

        # Initialize lists to store data
        paper_titles = []
        authors_list = []
        published_dates = []
        paper_urls = []

        # Find all articles within the container
        articles = articles_container.find_all("div", class_="sc-orwwe2-3.jOMrrY")  # Update this class name

        for article in articles:
            # Extract paper title
            paper_title = article.find("a", class_="sc-5smygv-0.fIXTHm").text.strip()  # Update this class name

            # Extract authors
            authors = article.find("div", class_="sc-1w3fpd7-0.dnCAO").text.strip()  # Update this class name
            authors_list.append(authors)

            # Extract published date
            published_date = article.find("div", class_="sc-1thf9iy-2.dvggWt").text.strip()  # Update this class name

            # Extract paper URL
            paper_url = article.find("a", class_="sc-1qrq3sd-1 gRGSUS sc-1nmom32-0 sc-1nmom32-1 btcbYu goSKRg")["href"]  # Update this class name

            paper_titles.append(paper_title)
            published_dates.append(published_date)
            paper_urls.append(paper_url)

        # Create a DataFrame
        df = pd.DataFrame({
            "Paper Title": paper_titles,
            "Authors": authors_list,
            "Published Date": published_dates,
            "Paper URL": paper_urls
        })

        return df

    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
        return None

# URL for the most downloaded articles in AI in the last 90 days
ai_most_downloaded_url = "https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles"
ai_most_downloaded_df = scrape_and_create_dataframe(ai_most_downloaded_url)

if ai_most_downloaded_df is not None:
    print("Most Downloaded AI Articles in the Last 90 Days:")
    print(ai_most_downloaded_df)


# In[ ]:


ai_most_downloaded_df


# # Question 7: Write a python program to scrape mentioned details from dineout.co.in and make data frame
# i) Restaurant name
# ii) Cuisine
# iii) Location
# iv) Ratings
# v) Image URL

# In[144]:


import requests
from bs4 import BeautifulSoup
import pandas as pd

# Function to scrape and create a DataFrame for the provided URL
def scrape_and_create_dataframe(url):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")

        # Find the container containing the restaurant details
        restaurant_container = soup.find("div", class_="listing-page-wrapper listing-page")

        if restaurant_container:
            # Initialize lists to store data
            restaurant_names = []
            cuisines = []
            locations = []
            ratings = []
            image_urls = []

            # Find all restaurants within the container
            restaurants = restaurant_container.find_all("div", class_="restnt-card restaurant")

            for restaurant in restaurants:
                # Extract restaurant name
                restaurant_name = restaurant.find("h3", class_="restnt-name ellipsis").text.strip()

                # Extract cuisine
                cuisine = restaurant.find("span", class_="restnt-cuisine ellipsis").text.strip()

                # Extract location
                location = restaurant.find("span", class_="restnt-loc ellipsis").text.strip()

                # Extract ratings
                rating = restaurant.find("span", class_="restnt-rating rating-4").text.strip()

                # Extract image URL
                image_url = restaurant.find("img")["data-src"].strip()

                restaurant_names.append(restaurant_name)
                cuisines.append(cuisine)
                locations.append(location)
                ratings.append(rating)
                image_urls.append(image_url)

            # Create a DataFrame
            restdf = pd.DataFrame({
                "Restaurant Name": restaurant_names,
                "Cuisine": cuisines,
                "Location": locations,
                "Ratings": ratings,
                "Image URL": image_urls
            })

            return restdf  # Return the DataFrame

        else:
            print("Could not find the restaurant container.")
            return None
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
        return None


# In[145]:


print(restdf)


# In[ ]:




