class Company:
    
    def __init__(self, company_name):
        self.company_name = company_name
        self.company_list = {}
    
    def record_company(self, project_title):
        if project_title not in self.company_list:
            self.company_list[project_title] = []
        self.company_list[project_title].append(self.company_name)
    
