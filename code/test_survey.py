import unittest 
from survey import AnonymousSurvey

""" unit test samples - uses setup   """

class TestAnonymousSurvey(unittest.TestCase):
   
    def setUp(self):
        """setup create survey set of response"""
        question = "What language did you first learn to speak?"  
        self.my_survey = AnonymousSurvey(question)
        self.responses = [ 'English', 'Italian', 'Spanish']


    """ unit test for anonymous survey """
    def test_store_single_response(self):
        """ test for single resonse inpt """
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses[0])

    def test_store_tree_response(self):
        """ store 3 """
       
        for r in self.responses:
            self.my_survey.store_response(r)

        for r in self.responses:        
            self.assertIn(r, self.my_survey.responses)

if __name__ == "__main__":
    unittest.main()        
