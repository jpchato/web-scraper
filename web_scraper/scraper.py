import requests

from bs4 import BeautifulSoup

def get_citations_needed_count(url):

    citation_list = []

    URL = url
    response = requests.get(URL)

    content = response.content

    soup = BeautifulSoup(content, 'html.parser')

    results = soup.find_all(class_='noprint Inline-Template Template-Fact')

    for citations in results:

        citation_list.append(results)

    print(len(citation_list))
    
    return len(citation_list)
    
get_citations_needed_count('https://en.wikipedia.org/wiki/Coronavirus_disease_2019')


def get_citations_needed_report(url):

    URL = url

    response = requests.get(URL)
    content = response.content

    soup = BeautifulSoup(content, 'html.parser')

    results = soup.find_all(class_='noprint Inline-Template Template-Fact')

    for citations in results:

        print("********" * 5)

        print(citations.parent.text.strip())

        print("********" * 5)

get_citations_needed_report('https://en.wikipedia.org/wiki/Coronavirus_disease_2019') 
