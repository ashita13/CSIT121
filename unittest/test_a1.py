import unittest

# define a test project class with outputs
class TestProject:
    def get_project_title(self):
        return "Project Test"
    
    def get_location(self):
        return "LOCATION"
    
    def get_status(self):
        return "STATUS"
    
    def get_star(self):
        return "STAR"
    
    def get_score(self):
        return "SCORE"
    
    def get_date_certified(self):
        return "DATE"
    
    def get_rating_tool(self):
        return "TOOL"
    
    def get_company(self):
        return "COMPANY"

# Define test case for search function
class TestMenu(unittest.TestCase):
    
    def setUp(self):
        self.testproject = TestProject()

    # test with assertEqual to see if functions in TestProject class output is the same
    def test_search_project_exist(self):
        self.assertEqual(self.testproject.get_project_title(), "Project Test")
        self.assertEqual(self.testproject.get_location(), "LOCATION")
        self.assertEqual(self.testproject.get_status(), "STATUS")
        self.assertEqual(self.testproject.get_star(), "STAR")
        self.assertEqual(self.testproject.get_score(), "SCORE")
        self.assertEqual(self.testproject.get_date_certified(), "DATE")
        self.assertEqual(self.testproject.get_rating_tool(), "TOOL")
        self.assertEqual(self.testproject.get_company(), "COMPANY")

    # test with assertNotEqual to see if get project title output is "Project Test"
    def test_search_project_not_exist(self):
        self.assertNotEqual(self.testproject.get_project_title(), "Other Project")

if __name__ == "__main__":
    unittest.main()
