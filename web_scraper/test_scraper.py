from .scraper import get_citations_needed_count, get_citations_needed_report

# User acceptance tests
# verify that correct count of citations needed is calculated
# verify that preceding passage

def correct_count(url):
    get_citations_needed_count('https://en.wikipedia.org/wiki/Coronavirus_disease_2019')
    length_citations_list = len(citation_list)
    expected = 12
    assert length_citations_list == expected

# def correct_passage(url):
#     assert get_citations_needed_report('https://en.wikipedia.org/wiki/Coronavirus_disease_2019') == 


