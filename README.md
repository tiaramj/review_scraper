
* Review Score Calculation
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


* Dependencies
Python3.7 or higher
To install BeautifulSoup
```bash
pip3 install --user bs4
```
To install vaderSentiment, run 
```bash
pip3 install --user vaderSentiment
```

* How to Run
Run
python3 scraper.py

Test
python3 test_scraper.py to run all tests
