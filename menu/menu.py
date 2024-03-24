from system.system import System
from system.company.project.project import Project
# datetime for the time format
from datetime import datetime
# sys for the quit function
import sys

class Menu:
    def __init__(self):
        self.system = System()
    # create a function to get user inputs
    # while loop to get correct input
    def run(self):
            while True:
                choice = str(input("Please enter the service you want (add, search, or X to quit): "))
                if choice.lower() == "add":
                    self.add_project()
                elif choice.lower() == "search":
                    self.search_project()
                elif choice.lower() == "x":
                    self.quit()
                elif choice.lower() != "add" or "search" or "x":
                    self.run()
            
    def add_project(self):
        print("Now you can add new project")
        new_ptitle = str(input("Please enter new project name: "))
        new_location = str(input("Please enter location of the project: "))
        new_status = str(input("Please enter status of the project: "))
        
        # while loop to get the right input datatype
        # try except to handle error
        while True:
            try:
                new_stars = int(input("Please enter project Green Star rating: "))
                break
            except ValueError:
                print("Please enter a number")
                
        while True:
            try:        
                new_score = int(input("Please enter project final score: "))
                break
            except ValueError:
                print("Please enter a number")
        
        while True:
            new_date = input("Please enter certified date (DD/MM/YYYY): ")
            try:
                date = datetime.strptime(new_date, "%d/%m/%Y")
                break
            except ValueError:
                print("Please enter the right date format")
        
        new_tool = str(input("Please enter project rating tool: "))
        new_company = str(input("What is the main company of this project?: "))
        
        # add to organizations list in system class
        # with the project title and the corresponding organizations
        while True:
            choice = str(input("Do you want to add new organizations to this project? (Y/N): "))
            if choice.lower() == "y":
                new_organization = str(input("Please enter organization: "))
                self.system.add_organ(new_ptitle, new_organization)
            elif choice.lower() == "n":
                break
            else: print("Invalid choice! Please try again")
            
        # add project to the System class list
        self.system.add_project(new_ptitle, new_location, new_stars, new_score, new_date, new_tool, new_company, new_status)
        
        
    # search function that collect project datas from project module
    def search_project(self):
        p_title = str(input("Please enter the project name: "))
        # get_project function from System class
        project = self.system.get_project(p_title)
        if project:
            print("This project is in the system.")
            print("")
            print(f"{'Project title: ':>20}{project.get_project_title()}")
            print(f"{'Location: ':>20}{project.get_location()}")
            print(f"{'Status: ':>20}{project.get_status()}")
            print(f"{'Green Star rating: ':>20}{project.get_star()}")
            print(f"{'Final score: ':>20}{project.get_score()}")
            print(f"{'Certified date: ':>20}{project.get_date_certified()}")
            print(f"{'Rating tool: ':>20}{project.get_rating_tool()}")
            print(f"{'Main company: ':>20}{project.get_company()}")
            # display organizations according to p_title
            print(f"{'Organizations involved: '}{self.system.display_organ(p_title)}")
            print("")
        else: 
            print("This project is not in the system.")
        self.run()
    
    def quit(self):
        print("Successfully quit") 
        sys.exit()
            
menu = Menu()
menu.run()