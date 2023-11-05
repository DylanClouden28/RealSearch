import requests
import os
from dotenv import load_dotenv


# query = user input, page = page number (default is 0)
# Input: A string
# Output: A list of 10 dictionaries
def get_webtags(query, page = 0): 
    load_dotenv()

    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

    RSE_KEY = os.getenv("RSE_KEY")

    start = page

    query = query.replace(" ", "%20")

    url = f"https://www.googleapis.com/customsearch/v1?key={GOOGLE_API_KEY}&cx={RSE_KEY}&q={query}&start={start}"

    data = requests.get(url).json()

    # get the result items
    search_items = data.get("items")

    webtags = []

    # iterate over 10 results found
    for i, search_item in enumerate(search_items, start=1):
        
        # get the page title
        title = search_item.get("title")

        # extract the page url
        link = search_item.get("link")

        mapper = {"title":title, "link":link}

        webtags.append(mapper)

        
    return webtags # returns the results (list of dictionaries)