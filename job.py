import requests
from bs4 import BeautifulSoup
import collections
import re

#A function that returns a list of keywords that match the job offer
def get_keywords(job_description):
    #download the job offer page
    response = requests.get(job_description)
    soup = BeautifulSoup(response.text, 'html.parser')

    #analyze the page's HTML to find the requirements section
    requirements = soup.find('section', {'class': 'job-requirements'})
    requirements_text = requirements.text.lower()

    #We create a list of keywords that match the requirements
    keywords = []
    for word in re.findall(r'\b\w+\b', requirements_text):
        if len(word) > 3 and word not in stop_words:
            keywords.append(word)
    
    #return a list of keywords
    return keywords

#list of words that will be ignored
stop_words = ['and', 'or', 'the', 'in', 'for', 'to', 'a', 'an', 'with', 'of', 'on', 'at', 'as']

#example job
job_description = 'https://www.example.com/jobs/1234'

#download keywords that match the job offer
keywords = get_keywords(job_description)

#create a dictionary that counts the number of occurrences of each keyword
keyword_count = collections.Counter(keywords)

#list keywords and their number of occurrences
for keyword, count in keyword_count.most_common(10):
    print(keyword, count)
