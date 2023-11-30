#!/usr/bin/env python
# coding: utf-8

# # Question 1: Scrape details of most viewed videos on YouTube

# In[25]:


import requests
from bs4 import BeautifulSoup

def scrape_youtube():
    try:
        url = "https://en.wikipedia.org/wiki/List_of_most-viewed_YouTube_videos"
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the table containing YouTube video details
        table = soup.find('table', {'class': 'wikitable'})

        # Initialize lists to store data
        ranks = []
        names = []
        artists = []
        upload_dates = []
        views = []

        # Extract data from the table
        for row in table.find_all('tr')[1:]:
            columns = row.find_all('td')

            # Add print statement to debug
            print(f"Columns: {columns}")

            if len(columns) >= 5:
                ranks.append(columns[0].text.strip())
                names.append(columns[1].text.strip())
                artists.append(columns[2].text.strip())
                upload_dates.append(columns[4].text.strip())
                views.append(columns[3].text.strip())
            else:
                print("Unexpected number of columns in a row.")

        # Print or return the data as needed
        for i in range(len(ranks)):
            print(f"Rank: {ranks[i]}, Name: {names[i]}, Artist: {artists[i]}, Upload Date: {upload_dates[i]}, Views: {views[i]}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function
scrape_youtube()



# # Question 2: Scrape details of team India’s international fixtures from bcci.tv

# In[31]:


import requests
from bs4 import BeautifulSoup

def scrape_bcci():
    try:
        url = "https://www.bcci.tv/fixtures?platform=international&type=women"
        response = requests.get(url)
        response.raise_for_status()

        # Check if the response is successful (status code 200)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            # Extract data from the webpage (adjust the selectors based on the webpage structure)
            series = [item.text.strip() for item in soup.select('.fixture__format')]
            places = [item.text.strip() for item in soup.select('.fixture__description')]
            dates = [item.text.strip() for item in soup.select('.fixture__date')]
            times = [item.text.strip() for item in soup.select('.fixture__time')]

            # Print or return the data as needed
            for i in range(len(series)):
                print(f"Series: {series[i]}, Place: {places[i]}, Date: {dates[i]}, Time: {times[i]}")
        else:
            print(f"Error: {response.status_code} - {response.text}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function
scrape_bcci()


# # Question 3: Scrape details of State-wise GDP of India from statisticstimes.com 

# In[18]:


https://www.bcci.tv/fixtures?platform=international&type=women

    
    import requests
from bs4 import BeautifulSoup

def scrape_gdp():
    try:
        url = "http://statisticstimes.com/economy/india-statistics.php"
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the first table on the page
        table = soup.find('table')
        
        if table:
            # Initialize lists to store data
            ranks = []
            states = []
            gsdp_1819 = []
            gsdp_1920 = []
            share_1819 = []
            gdp_billion = []

            # Extract data from the table
            for row in table.find_all('tr')[1:]:
                columns = row.find_all('td')
                ranks.append(columns[0].text.strip())
                states.append(columns[1].text.strip())
                gsdp_1819.append(columns[2].text.strip())
                gsdp_1920.append(columns[3].text.strip())
                share_1819.append(columns[4].text.strip())
                gdp_billion.append(columns[5].text.strip())

            # Print or return the data as needed
            for i in range(len(ranks)):
                print(f"Rank: {ranks[i]}, State: {states[i]}, GSDP(18-19): {gsdp_1819[i]}, GSDP(19-20): {gsdp_1920[i]}, Share(18-19): {share_1819[i]}, GDP($ billion): {gdp_billion[i]}")
        else:
            print("Table not found on the webpage.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function
scrape_gdp()



# # Question 4: Scrape details of trending repositories on Github.com

# In[33]:


import requests
from bs4 import BeautifulSoup

def scrape_github():
    try:
        url = "https://github.com/trending"
        response = requests.get(url)
        response.raise_for_status()

        # Check if the response is successful (status code 200)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            # Extract data from the webpage (adjust the selectors based on the webpage structure)
            repo_titles = [item.text.strip() for item in soup.select('.h3.lh-condensed')]
            repo_descriptions = [item.text.strip() for item in soup.select('.col-9.color-text-secondary.my-1.pr-4')]
            contributors_counts = [item.text.strip() for item in soup.select('.f6.color-text-secondary.mt-2 .d-inline-block.mr-3')]
            languages_used = [item.text.strip() for item in soup.select('.f6.color-text-secondary.mt-2 span[itemprop="programmingLanguage"]')]

            # Add print statements to debug
            print(f"Repo Titles: {repo_titles}")
            print(f"Repo Descriptions: {repo_descriptions}")
            print(f"Contributors Counts: {contributors_counts}")
            print(f"Languages Used: {languages_used}")

            # Print or return the data as needed
            for i in range(len(repo_titles)):
                print(f"Repository Title: {repo_titles[i]}, Description: {repo_descriptions[i]}, Contributors Count: {contributors_counts[i]}, Language Used: {languages_used[i]}")
        else:
            print(f"Error: {response.status_code} - {response.text}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function
scrape_github()




# # Question 5: Scrape details of top 100 songs on billboard.com

# In[40]:


import requests
from bs4 import BeautifulSoup

def scrape_billboard():
    try:
        url = "https://www.billboard.com/charts/hot-100/"
        response = requests.get(url)
        response.raise_for_status()

        # Check if the response is successful (status code 200)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            # Extract data from the webpage (adjust the selectors based on the webpage structure)
            song_names = [item.text.strip() for item in soup.select('.chart-element__information__song')]
            artist_names = [item.text.strip() for item in soup.select('.chart-element__information__artist')]
            last_week_ranks = [item.text.strip() for item in soup.select('.chart-element__meta.text--last')]
            peak_ranks = [item.text.strip() for item in soup.select('.chart-element__meta.text--peak')]
            weeks_on_board = [item.text.strip() for item in soup.select('.chart-element__meta.text--week')]

            # Print or return the data as needed
            for i in range(len(song_names)):
                print(f"Song Name: {song_names[i]}, Artist Name: {artist_names[i]}, Last Week Rank: {last_week_ranks[i]}, Peak Rank: {peak_ranks[i]}, Weeks on Board: {weeks_on_board[i]}")
        else:
            print(f"Error: {response.status_code} - {response.text}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function
scrape_billboard()


# # Question 6: Scrape details of Highest selling novels

# In[41]:


import requests
from bs4 import BeautifulSoup

def scrape_novels():
    try:
        url = "https://www.theguardian.com/news/datablog/2012/aug/09/best-selling-books-all-time-fifty-shades-grey-compare"
        response = requests.get(url)
        response.raise_for_status()

        # Check if the response is successful (status code 200)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            # Extract data from the webpage (adjust the selectors based on the webpage structure)
            book_names = [item.text.strip() for item in soup.select('.embed blockquote p strong')]
            author_names = [item.text.strip() for item in soup.select('.embed blockquote p em')]
            volumes_sold = [item.text.strip() for item in soup.select('.embed blockquote p')[1::4]]
            publishers = [item.text.strip() for item in soup.select('.embed blockquote p')[2::4]]
            genres = [item.text.strip() for item in soup.select('.embed blockquote p')[3::4]]

            # Print or return the data as needed
            for i in range(len(book_names)):
                print(f"Book Name: {book_names[i]}, Author Name: {author_names[i]}, Volumes Sold: {volumes_sold[i]}, Publisher: {publishers[i]}, Genre: {genres[i]}")
        else:
            print(f"Error: {response.status_code} - {response.text}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function
scrape_novels()



# # Question 7: Scrape details most watched tv series of all time from imdb.com

# In[42]:


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.keys import Keys

def scrape_tv_series():
    driver = None  # Initialize driver outside the try block

    try:
        url = "https://www.imdb.com/list/ls095964455/"
        
        # Set up the ChromeDriver
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--headless")  # Run Chrome in headless mode (no GUI)
        chrome_service = ChromeService(executable_path="/path/to/chromedriver")
        driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
        
        # Navigate to the IMDb page
        driver.get(url)
        
        # Scroll to the bottom of the page to load all content (adjust sleep time as needed)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        driver.implicitly_wait(10)  # Implicitly wait for content to load
        
        # Extract data using Selenium
        series_names = driver.find_elements(By.XPATH, "//h3[@class='lister-item-header']/a")
        year_spans = driver.find_elements(By.XPATH, "//span[@class='lister-item-year text-muted unbold']")
        genres = driver.find_elements(By.XPATH, "//span[@class='genre']")
        run_times = driver.find_elements(By.XPATH, "//span[@class='runtime']")
        ratings = driver.find_elements(By.XPATH, "//strong")
        votes = driver.find_elements(By.XPATH, "//span[@name='nv']")
        
        # Print or return the data as needed
        for i in range(len(series_names)):
            print(f"Series Name: {series_names[i].text}, Year Span: {year_spans[i].text}, Genre: {genres[i].text}, Run Time: {run_times[i].text}, Ratings: {ratings[i].text}, Votes: {votes[i].text}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if driver:
            driver.quit()  # Ensure the driver is closed even if an exception occurs

# Call the function
scrape_tv_series()



# # Question 8: Details of Datasets from UCI machine learning repositories.

# In[43]:


import requests
from bs4 import BeautifulSoup

def scrape_datasets():
    try:
        url = "https://archive.ics.uci.edu/"
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        # Navigate to Show All Dataset page
        all_datasets_url = "https://archive.ics.uci.edu/ml/datasets.php"
        response_all_datasets = requests.get(all_datasets_url)
        response_all_datasets.raise_for_status()
        soup_all_datasets = BeautifulSoup(response_all_datasets.text, 'html.parser')

        # Extract dataset details
        dataset_names = [item.text.strip() for item in soup_all_datasets.select('p a b')]
        data_types = [item.text.strip() for item in soup_all_datasets.select('p:nth-child(5)')]
        tasks = [item.text.strip() for item in soup_all_datasets.select('p:nth-child(6)')]
        attribute_types = [item.text.strip() for item in soup_all_datasets.select('p:nth-child(7)')]
        num_instances = [item.text.strip() for item in soup_all_datasets.select('p:nth-child(8)')]
        num_attributes = [item.text.strip() for item in soup_all_datasets.select('p:nth-child(9)')]
        years = [item.text.strip() for item in soup_all_datasets.select('p:nth-child(10)')]

        # Print or return the data as needed
        for i in range(len(dataset_names)):
            print(f"Dataset Name: {dataset_names[i]}, Data Type: {data_types[i]}, Task: {tasks[i]}, Attribute Type: {attribute_types[i]}, No of Instances: {num_instances[i]}, No of Attributes: {num_attributes[i]}, Year: {years[i]}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function
scrape_datasets()


# In[ ]:




