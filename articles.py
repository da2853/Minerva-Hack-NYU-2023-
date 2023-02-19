import requests
from bs4 import BeautifulSoup
import re

# List of keywords to search for
keywords = ["Python", "AI", "machine learning"]

def getArticles(keywords):
    a_string = ""
    for keyword in keywords:
        a_string = a_string + " " + keyword
    # Search for articles and retrieve the responses
    response = requests.get("http://www.google.com/search?q=" + a_string)

    if response.status_code == 200:
        # If response is successful, parse the response using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract article URLs from results page
        urls = [a['href'] for a in soup.find_all('a', href=True)]
        return_lst = []
        counter = 0
        for url in urls:
            if re.match('/url\?q=',url):
                return_lst.append(re.split('&sa=U&ved=', url)[0][7:])
                counter += 1
                if counter >= 1:
                    return return_lst
        return return_lst

#x = getArticles(keywords)
#for i in x:
    #print(i)