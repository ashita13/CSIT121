from system.system import System
from system.organization.organization import Organization
# datetime for the time format
from datetime import datetime
# sys for the quit function
import sys
import os

class Menu:
    def __init__(self):
        self.system = System()
        self.role = Organization()
    # create a function to get user inputs
    # while loop to get correct input
    def run(self):
            while True:
                choice = str(input("Please enter the service you want (add, search, role, generate report or X to quit): "))
                if choice.lower() == "add":
                    self.add_project()
                elif choice.lower() == "search":
                    self.search_project()
                elif choice.lower() == "x":
                    self.quit()
                elif choice.lower() == "role":
                    self.show_orgs_involved_with_roles()
                elif choice.lower() == "generate report":
                    self.gen_report()
                elif choice.lower() != "add" or "search" or "x":
                    self.run()
            
    def add_project(self):
        print("Now you can add new project")
        new_ptitle = str(input("Please enter new project name: "))
        new_location = str(input("Please enter location of the project: "))
        state_au = ["ACT", "INTERNATIONAL", "NATIONAL", "NSW", "NT", "QLD", "SA", "TAS", "VIC", "WE"]
        while True:
            try:    
                new_state = str(input("Please enter state (ACT, International, National, NSW, NT, QLD, SA, TAS, VIC, WE): "))
                if new_state.upper() in state_au:
                    new_location += f", {new_state}"
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Enter the right state")
        while True:
            try:
                new_status = str(input("Please enter status of the project (REGISTERED/ CERTIFIED): "))
                if new_status.lower() == "registered" or new_status.lower() == "certified":
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Please enter REGISTERED or CERTIFIED")
        # while loop to get the right input datatype
        # try except to handle error
        while True:
            try:
                new_stars = int(input("Please enter project Green Star rating (1 to 6): "))
                if new_stars in range(1, 6):
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Please enter a number in range")
                
        while True:
            try:        
                new_score = str(input("Please enter project final score (0 - 100) or NA: "))
                if new_score == "NA":
                    break
                elif int(new_score) in range(0, 100):
                    break
                else: raise ValueError
            except ValueError:
                print("Please enter a number in range or NA")
        
        while True:
            new_date = input("Please enter certified date (DD/MM/YYYY): ")
            try:
                date = datetime.strptime(new_date, "%d/%m/%Y")
                break
            except ValueError:
                print("Please enter the right date format")
        
        while True:
            tool_ver = ["v3", "v2", "v0.1", "v0.2", "v1", "v1.1", "v1.2", "v1.2.0", "v1.3", "PILOT v0.0", "PILOT v0.1", "PILOT v0.2"]
            try:
                new_tool = str(input("Please enter project rating tool \n(v0.1, v0.2, v1, v2, v3, v1.1, v1.2, v1.3, v1.2.0, PILOT v0.0, PILOT v0.1, PILOT v0.2): "))
                if new_tool.lower() in tool_ver:
                    break
                else: raise ValueError
            except ValueError:
                print("Please enter existing version number")
        new_company = str(input("What is the main company of this project?: "))
        
        # add to organizations list in system class
        # with the project title and the corresponding organizations
        while True:
            choice = str(input("Do you want to add new organizations to this project? (Y/N): "))
            if choice.lower() == "y":
                new_organization = str(input("Please enter organization: "))
                organ_role = str(input("Please provide role of this organization: "))
                self.system.add_organ(new_ptitle, new_organization)
                self.role.add_role(new_organization, organ_role)
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
            print(f"{'Status: ':>20}{(project.get_status()).upper()}")
            print(f"{'Green Star rating: ':>20}{project.get_star()}")
            print(f"{'Final score: ':>20}{project.get_score()}")
            print(f"{'Certified date: ':>20}{project.get_date_certified()}")
            print(f"{'Rating tool: ':>20}{project.get_rating_tool()}")
            print(f"{'Main company: ':>20}{project.get_company()}")
            # display organizations according to p_title
            print(f"Organizations involved: {self.system.display_organ(p_title)}")
            print("")
        else: 
            print("This project is not in the system.")
        self.run()
    
    # show the role and organization with project title
    def show_orgs_involved_with_roles(self):
        p_title = str(input("Please enter the project name: "))
        orgs = (self.system.get_org(p_title))
        if p_title:
            print("Role of each organizations: ")
            for org in orgs:
                print(f"{org}: {self.role.get_role(org)}")
            else: return "Project not found"

    def gen_report(self):
        # same code as in search fucntion
        p_title = str(input("Please enter the project name: "))
        project = self.system.get_project(p_title)
        orgs = (self.system.get_org(p_title))
        
        # the directory of this Python script
        script_dir = os.path.dirname(os.path.abspath(__file__))
        # create an absolute path to the txt file
        file_path = os.path.join(script_dir, f"PROJECT_{p_title}_REPORT.txt")
        
        if project:
            with open(file_path, "w") as file:
                file.write(f"Project title: {project.get_project_title()}\n")
                file.write(f"Location: {project.get_location()}\n")
                file.write(f"Status: {(project.get_status()).upper()}\n")
                file.write(f"Green Star rating: {project.get_star()}\n")
                file.write(f"Final score: {project.get_score()}\n")
                file.write(f"Certified date: {project.get_date_certified()}\n")
                file.write(f"Rating tool: {project.get_rating_tool()}\n")
                file.write(f"Main company: {project.get_company()}\n")
                file.write(f"Organizations involved: {self.system.display_organ(p_title)}\n")
                file.write("Role of each organizations \n")
                for org in orgs:
                    file.write(f"{org}: {self.role.get_role(org)}\n")
        else: 
            print("This project is not in the system.")
        self.run()
    
    # quit function to exit the program
    def quit(self):
        print("Successfully quit") 
        sys.exit()

# run the program from this script 
if __name__ == "__main__":
    program = Menu()
    program.run()