import unittest
# from A1 import Project, Company, System, Organization

class Project:
    def __init__(self, project_title, location, star, score, date_certified, rating_tool, company, status=""):
        self.project_title = project_title
        self.location = location
        self.star = star
        self.score = score
        self.date_certified = date_certified
        self.rating_tool = rating_tool
        self.status = status
        self.company = company
        
    def get_project_title(self):
        return self.project_title
    def get_location(self):
        return self.location
    def get_status(self):
        return self.status
    def get_star(self):
        return self.star
    def get_score(self):
        return self.score
    def get_date_certified(self):
        return self.date_certified
    def get_rating_tool(self):
        return self.rating_tool
    def get_company(self):
        return self.company
    
class Company:
    
    def __init__(self, company_name):
        self.company_name = company_name
        self.company_list = {}
    
    def record_company(self, project_title):
        if project_title not in self.company_list:
            self.company_list[project_title] = []
        self.company_list[project_title].append(self.company_name)

class System:
    # create a projects list
    def __init__(self):
        self.projects = []
        self.organs = {}
        
    # add project to system projects list
    def add_project(self, project_title, location, star, score, date_certified, rating_tool, company, status=""):
        project = Project(project_title, location, star, score, date_certified, rating_tool, company, status)
        self.projects.append(project)
        
    # define search function to get the specific project title
    def get_project(self, p_title):
        for project in self.projects:
            if project.get_project_title() == p_title:
                return project
        return None
    
    # p_title need to establish first when its not in the dictionary
    def add_organ(self, p_title, organ_name):
        if p_title not in self.organs:
            self.organs[p_title] = []
        self.organs[p_title].append(organ_name)
    
    # get the value of the p_title key so the output is not 
    # showing all the available organizations
    def display_organ(self, p_title):
        output_organ = self.organs.get(p_title)
        if output_organ:
            return ", ".join(output_organ)
        else: return "None"
    
    # get value according to key project title
    def get_org(self, p_title):
        output_organ = self.organs.get(p_title)
        return output_organ
    
class Organization:
    def __init__(self):
        self.role = {}
    
    # add role value by organization name
    def add_role(self, organ_name, role):
        role_name = self.role.get(role)
        if role_name not in self.role:
            self.role[organ_name] = []
        # append to value of key so this key's value is a list
        self.role[organ_name].append(role)

    # get the according role with organization name
    def get_role(self, organ_name):
        output_role = self.role.get(organ_name)
        if output_role:
            return "".join(output_role)
        else: return "None"
    


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
