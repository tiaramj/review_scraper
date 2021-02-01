from bs4 import BeautifulSoup
from collections import Counter
import requests
from time import sleep
from glob import glob
import re
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def get_reviews():
    '''This function requests from `https://transcripts.fandom.com/wiki/` and
    saves the file in the local folder `strangerthings/`. The function doesn't
    return a value (so by default, it will automatically return `None`).'''

    h = {'user-agent': 'Tiara Johnson (tiara.johnson@podium.com)'}

    for i in range(1, 6):
        # Add link to the base url
        url = "https://www.dealerrater.com/dealer/McKaig-Chevrolet-Buick-A-Dealer-For-The-People-dealer-reviews-23685/page" + str(i) + "/?filter=#link"
        response = requests.get(url, headers=h)

        content = response.text
        soup = BeautifulSoup(content, 'html.parser')
        authors.extend([spans.text for spans in soup.find_all('span', {'class': 'italic font-18 black notranslate'})])
        review_body.extend([p.text for p in soup.find_all('p', {'class': "font-16 review-content margin-bottom-none line-height-25"})])
        regex = r'<div class=\"rating-static visible-xs pad-none margin-none rating-(.)'  # Dialogue regex
        overall_ratings.extend(re.findall(regex, content, flags=re.IGNORECASE))
        regex = r'>Customer.*\n.*<div.*rating-(.)'
        service.extend(re.findall(regex, content, flags=re.IGNORECASE))
        regex = r'>Quality of.*\n.*<div.*rating-(.)'
        quality.extend(re.findall(regex, content, flags=re.IGNORECASE))
        regex = r'>Friendli.*\n.*<div.*rating-(.)'
        friendliness.extend(re.findall(regex, content, flags=re.IGNORECASE))
        regex = r'>Pricing.*\n.*<div.*rating-(.)'
        pricing.extend(re.findall(regex, content, flags=re.IGNORECASE))
        regex = r'>Overall Experi.*\n.*<div.*rating-(.)'
        experience.extend(re.findall(regex, content, flags=re.IGNORECASE))
        dealer.extend([divs.text.strip() for divs in soup.find_all('div', {'class': "td small-text boldest"})])
    

        # tells the scraper to sleep for 1 sec per loop/request
        sleep(1)
        

def calculate_score():
    htmlfilename = "pagefinal.txt"
    with open(htmlfilename, 'w') as textfile:
        for i in range(len(authors)):
                
            print(authors[i], file=textfile)
            print(overall_ratings[i], file=textfile)
            print(review_body[i], file=textfile)
            ps = hal.polarity_scores(review_body[i])
            # use compound score
            #print(round(ps.get('compound') * 10, 2))
            score = (ps.get('compound') * 10) + int(overall_ratings[i]) + int(service[i]) + int(quality[i]) + int(friendliness[i]) + int(pricing[i]) + int(experience[i])
                    
            print(service[i], file=textfile)
            print(quality[i], file=textfile)
            print(friendliness[i], file=textfile)
            print('Pricing ' + pricing[i], file=textfile)
            print(experience[i], file=textfile)

            if dealer[i] == "Yes":
                score = score + 10
            print(round(score, 2), file=textfile)
            final_scores.append(score)


def find_highest_scores(n):
    
    #store list in tmp to retrieve index
    tmp=list(final_scores)
    #sort list so that largest elements are on the far right
    final_scores.sort()
    #To get the n largest elements
    #print(final_scores[-n:])
    
    #get index of the n largest elements
    for i in range(1, n+1):
        index = (tmp.index(final_scores[-i]))
        print(authors[index])
        print(review_body[index])
        print()
                

hal = SentimentIntensityAnalyzer()
authors = []
review_body = []
overall_ratings = []
quality = []
service = []
friendliness = []
pricing = []
experience = []
dealer = []
final_scores = []

get_reviews()
calculate_score()
N=3
find_highest_scores(N)