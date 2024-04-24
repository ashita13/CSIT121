import unittest
from A1 import Project, Company, System, Organization

# define a test project class with default outputs
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
class TestSearch(unittest.TestCase):
    
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

# unittest for class System
class TestSystem(unittest.TestCase):
    def setUp(self):
        # Initialize a System instance for testing
        self.system = System()

    def test_add_project(self):
        # Test adding a project
        self.system.add_project("Project A", "Location A", 5, 90, "20/04/2022", "Tool X", "Company Y")
        self.assertEqual(len(self.system.projects), 1)

    def test_get_project(self):
        # Test getting a project
        self.system.add_project("Project B", "Location B", 4, 80, "21/04/2024", "Tool Y", "Company Z")
        project = self.system.get_project("Project B")
        self.assertIsNotNone(project)
        self.assertEqual(project.get_project_title(), "Project B")

    def test_add_organ(self):
        # Test adding an organ to a project
        self.system.add_organ("Project A", "Organ X")
        self.assertEqual(self.system.display_organ("Project A"), "Organ X")

    def test_get_org(self):
        # Test getting organs for a project
        self.system.add_organ("Project B", "Organ Y")
        self.system.add_organ("Project B", "Organ Z")
        organs = self.system.get_org("Project B")
        self.assertEqual(len(organs), 2)
        self.assertIn("Organ Y", organs)
        self.assertIn("Organ Z", organs)

# unittest for Company class
class TestCompany(unittest.TestCase):
    def setUp(self):
        # Initialize a Company instance for testing
        self.company = Company("ABC")

    def test_record_company(self):
        # Test recording a company for a project
        self.company.record_company("Project A")
        self.assertIn("ABC", self.company.company_list["Project A"])

        # Test adding another company for the same project
        self.company.record_company("Project A")
        self.assertEqual(len(self.company.company_list["Project A"]), 2)
        self.assertIn("ABC", self.company.company_list["Project A"])

        # Test recording a company for a different project
        self.company.record_company("Project B")
        self.assertIn("ABC", self.company.company_list["Project B"])

# unittest for Organization class
class TestOrganization(unittest.TestCase):
    def setUp(self):
        self.org = Organization()

    def test_add_and_get_role(self):
        self.org.add_role('Company A', 'Manager')
        self.assertEqual(self.org.get_role('Company A'), 'Manager')

        self.org.add_role('Company A', 'Developer')
        self.assertEqual(self.org.get_role('Company A'), 'Developer')

        self.assertEqual(self.org.get_role('Company B'), 'None')

if __name__ == "__main__":
    unittest.main()
