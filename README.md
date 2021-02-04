# Coding Challenge: “A Dealer For the People”
The KGB has noticed a resurgence of overly excited reviews for a McKaig Chevrolet Buick, a dealership they have planted in the United States. In order to avoid attracting unwanted attention, you’ve been enlisted to scrape reviews for this dealership from DealerRater.com and uncover the top three worst offenders of these overly positive endorsements.

Your mission, should you choose to accept it, is to write a tool that:

* scrapes the first five pages of reviews
* identifies the top three most “overly positive” endorsements (using criteria of your choosing, documented in the README)
* outputs these three reviews to the console, in order of severity

## Review Score Calculation
Using the star ratings and sentiment analysis, each review gets a final score out of 50.
Overall Star Rating - 0 to 5
Customer Service - 0 to 5
Quality Of Work - 0 to 5
Friendliness - 0 to 5
Pricing - 0 to 5
Experience - 0 to 5
Recommend Dealer - Yes(+10) or No(+0)
Sentiment analysis on review body - 0 to 10 (+/-)
    - The compound score gives me a score between -1 and +1. I have multiplied this by 10 to get the sentiment score.


## Dependencies
Python3.7 or higher
To install BeautifulSoup
```bash
pip3 install --user bs4
```
To install vaderSentiment, run 
```bash
pip3 install --user vaderSentiment
```

## How to Run
Run
python3 scraper.py

Test
python3 test_scraper.py to run all tests
