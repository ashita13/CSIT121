from system.company.project.company1 import Company
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
    