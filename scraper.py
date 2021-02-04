from bs4 import BeautifulSoup
import re
import requests
from time import sleep
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


def get_reviews(no_of_pages):
    '''This function requests from dealer rater and extracts reviews from
    the first n pages mentioned by the user. The function returns a list of
    Reviews with different ratings.'''

    h = {'user-agent': 'Tiara Johnson (tiara.johnson@podium.com)'}

    Reviews = []
    authors = []
    review_body = []
    overall_ratings = []
    quality = []
    service = []
    friendliness = []
    pricing = []
    experience = []
    dealer = []

    for i in range(no_of_pages):
        # Add page no to the base url
        url = "https://www.dealerrater.com/dealer/McKaig-Chevrolet-Buick-A-Dealer-For-The-People-dealer-reviews-23685/page" + str(i+1) + "/?filter=#link"
        response = requests.get(url, headers=h)

        content = response.text
        soup = BeautifulSoup(content, 'html.parser')

        # Using beautiful soup and regex to parse out information from reviews
        authors.extend([spans.text for spans in soup.find_all('span', {'class': 'italic font-18 black notranslate'})])
        review_body.extend([p.text for p in soup.find_all('p', {'class': "font-16 review-content margin-bottom-none line-height-25"})])
        overall_ratings.extend(re.findall(r'margin-none rating-(.)', content, flags=re.IGNORECASE))
        service.extend(re.findall(r'>Customer.*\n.*<div.*rating-(.)', content, flags=re.IGNORECASE))
        quality.extend(re.findall(r'>Quality of.*\n.*<div.*rating-(.)', content, flags=re.IGNORECASE))
        friendliness.extend(re.findall(r'>Friendli.*\n.*<div.*rating-(.)', content, flags=re.IGNORECASE))
        pricing.extend(re.findall(r'>Pricing.*\n.*<div.*rating-(.)', content, flags=re.IGNORECASE))
        experience.extend(re.findall(r'>Overall Experi.*\n.*<div.*rating-(.)', content, flags=re.IGNORECASE))
        dealer.extend([divs.text.strip() for divs in soup.find_all('div', {'class': "td small-text boldest"})])

        # Tell the scraper to sleep for 1 sec per loop/request
        sleep(1)

    # Create list of reviews
    for i in range(len(authors)):
        Reviews.append({'author': authors[i], 'review_body': review_body[i], 'overall_rating': overall_ratings[i], 'service': service[i], 'quality': quality[i], 'friendliness': friendliness[i], 'pricing': pricing[i], 'experience': experience[i], 'recommend_dealer': dealer[i]})
        
    return Reviews


def calculate_score(Reviews):
    '''This function calculates the final score for each review using the 
    sentiment score of the review body, overall rating, sub-category ratings,
    and whether the dealer is recommend or not. The final score is added to the
    Review list and all the review details are printed to reviews.txt'''

    hal = SentimentIntensityAnalyzer()
    filename = "reviews.txt"
    with open(filename, 'w') as textfile:
        for review in Reviews:
                
            print(review['author'], file=textfile)
            print(review['overall_rating'], file=textfile)
            print(review['review_body'], file=textfile)
            print('Customer Service: ' + review['service'], file=textfile)
            print('Quality of work:' + review['quality'], file=textfile)
            print('Friendliness: ' + review['friendliness'], file=textfile)
            print('Pricing: ' + review['pricing'], file=textfile)
            print('Experience: ' + review['experience'], file=textfile)
            print('Recommend Dealer: ' + review['recommend_dealer'], file=textfile)

            # Perform sentiment analysis on review body
            ps = hal.polarity_scores(review['review_body'])
            # Use compound score
            #print(round(ps.get('compound') * 10, 2))
            score = (ps.get('compound') * 10) + int(review['overall_rating']) + int(review['service']) + int(review['quality']) + int(review['friendliness']) + int(review['pricing']) + int(review['experience'])
            if review['recommend_dealer'] == "Yes":
                score = score + 10
            print('Final Score: ' + str(round(score, 2)) + '\n', file=textfile)
            review['final_score'] = score

    return Reviews


def find_highest_scores(Reviews, n):
    ''' This function takes list of reviews as the first arg and the num of
    reviews to be returned (n) as the second arg. The function will find the 
    n highest scored reviews and print it to the console.'''
    
    result = []
    # Create a list of final scores
    tmp = [rev['final_score'] for rev in Reviews]
    # Create a copy of the list to find the index
    final_scores = list(tmp)
    # Sort list so that highest scores are on the far right
    final_scores.sort()
    
    # Get index(s) of the n highest final scores
    for i in range(1, n+1):
        index = (tmp.index(final_scores[-i]))
        print(Reviews[index]['author'])
        print(Reviews[index]['final_score'])
        print(Reviews[index]['review_body'])
        print()

        # For unit testing
        result.append({'author': Reviews[index]['author'], 'review_body': Reviews[index]['review_body'], 'final_score': Reviews[index]['final_score']})

    return result


Reviews = get_reviews(5)
Reviews = calculate_score(Reviews)
result = find_highest_scores(Reviews, 3)