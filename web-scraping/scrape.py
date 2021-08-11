import requests
# pip3 install beautifulSoup4
# BeautifulSoup will convert the response string into an object
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/')
soup = BeautifulSoup(res.text, 'html.parser')
links = soup.select(('.storylink'))
subtext = soup.select('.subtext')

#print(soup.body.contents) #will return only the body html
# print(soup.find_all('div')) # will return all the divs
# print(soup.find_all('a'))
''' 
print(soup.find('a')) # will return the first a tag
print(soup.find(id="score-123"))
print(soup.select('.score')) #class of score
print(soup.select('#score345')) # select id score345
print(soup.select('.storylink')[0]) # get the first class with that name
'''
def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key= lambda k:k['votes'])

def create_custon_hn(links,votes):
    hn = []
    for inx, item in enumerate(links):
        title = links[inx].getText()
        href = links[inx].get('href', None) # second parameter in case the link doesn't have href
        vote = subtext[inx].select('.score')
        if len(vote):
            points= int(vote[0].getText().replace('points', ''))

            hn.append({'title': title,'link':href, 'votes': points})

    return sort_stories_by_votes(hn)

pprint.pprint(create_custon_hn(links, subtext))