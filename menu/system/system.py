from system.company.project.project import Project
from system.organization.organization import Organization
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
    
