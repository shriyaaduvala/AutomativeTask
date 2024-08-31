import requests
from bs4 import BeautifulSoup

# URL of the website you want to scrape
url = "https://www.codealpha.tech/"

# Send a GET request to the website
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    print("Successfully retrieved the webpage")
    
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    #Find all <a> tags with the class name 'btn'
    Register_link = soup.find_all(name="a")

    # Loop through the register_links and print them
    
    for register in Register_link:
        print(register.get("href"))
    
    # Find all <h2> tags with the class name 'news-title'
    news_titles = soup.select('h2', class_='span')

    # Loop through the titles and print them
    for title in news_titles:
        print(title.get_text())
else:
    print("Failed to retrieve the webpage")
