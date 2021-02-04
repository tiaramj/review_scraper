import unittest
from scraper import get_reviews, calculate_score, find_highest_scores

class ScraperTest(unittest.TestCase):
    
    def test_reviews_returned(self):
        result = get_reviews(2)
        # Each page returns 10 reviews so there should be 20 total
        self.assertEqual(len(result), 2*10)

    
    def test_calculate_scores(self):
        Reviews = [{'author': '- eric', 'review_body': 'Awesome cars and super service!', 'overall_rating': '5', 'service': '5', 'quality': '5', 'friendliness': '5', 'pricing': '5', 'experience': '5', 'recommend_dealer': 'Yes'}]
        result = calculate_score(Reviews)
        # 8.516 is the review body sentiment. It should add up to 48.516
        self.assertEqual(result, [{'author': '- eric', 'review_body': 'Awesome cars and super service!', 'overall_rating': '5', 'service': '5', 'quality': '5', 'friendliness': '5', 'pricing': '5', 'experience': '5', 'recommend_dealer': 'Yes', 'final_score': 48.516}])
        
    
    def test_no_of_scores_returned(self):
        Reviews = [{'author': '- testuser1', 'review_body': 'Awesome help!', 'final_score': 49.891}, {'author': '- testuser2 ', 'review_body': "I'm always pleased with Mc Kaig. Thanks again you guys. ", 'final_score': 49.559}, {'author': '- Milk942', 'review_body': 'I like the resent changes they have made by walking around vehicle marking off damage before service. Then after service is provided walking around with u to make sure ur satisfied great improvement.', 'final_score': 44.689}, {'author': '- testuser3', 'review_body': 'I love it.. I came in at the headed I left out with a new vehicle', 'final_score': 40.98}]
        result = find_highest_scores(Reviews, 2)
        # Should return only two reviews - testuser1 & testuser2
        self.assertEqual(len(result), 2)


    def test_highest_score_returned(self):
        Reviews = [{'author': '- testuser1', 'review_body': 'Awesome help!', 'final_score': 49.891}, {'author': '- testuser2 ', 'review_body': "I'm always pleased with Mc Kaig. Thanks again you guys. ", 'final_score': 49.559}, {'author': '- Milk942', 'review_body': 'I like the resent changes they have made by walking around vehicle marking off damage before service. Then after service is provided walking around with u to make sure ur satisfied great improvement.', 'final_score': 44.689}, {'author': '- testuser3', 'review_body': 'I love it.. I came in at the headed I left out with a new vehicle', 'final_score': 40.98}]
        result = find_highest_scores(Reviews, 1)
        # Should return testuser1 review
        self.assertEqual(result[0]['final_score'], 49.891)



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()

