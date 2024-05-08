from system.system import System
from system.organization.organization import Organization
from system.company.project.project import Project
# datetime for the time format
from datetime import datetime
# sys for the quit function
import sys
import os
import json
import matplotlib.pyplot as plt

class Menu:
    def __init__(self):
        self.system = System()
        self.role = Organization()
    # create a function to get user inputs
    # while loop to get correct input
    def run(self):
            while True:
                choice = str(input("Please enter the service you want (load, add, search, role, generate report, chart or X to quit): "))
                if choice.lower() == "load":
                    self.load_data()
                elif choice.lower() == "add":
                    self.add_project()
                elif choice.lower() == "search":
                    self.search_project()
                elif choice.lower() == "x":
                    self.quit()
                elif choice.lower() == "role":
                    self.show_orgs_involved_with_roles()
                elif choice.lower() == "generate report":
                    self.gen_report()
                elif choice.lower() == "chart":
                    self.chart()
                elif choice.lower() != "add" or "search" or "x" or "load" or "role" or "generate report":
                    self.run()
    
    def load_data(self):
        # the directory of this Python script
        script_dir = os.path.dirname(os.path.abspath(__file__))
        # create an absolute path to the txt file
        file_path = os.path.join(script_dir, f"projects_data.json")
        # check if this file exist in the given path
        if os.path.exists(file_path):
            with open(file_path, "r") as file:
                print("Load successfully")
                projects_data = json.load(file)
            
            # for loop to read data of a dict
            for project_json in projects_data["project"]:
                project = Project(project_json["project_title"], 
                                    project_json["location"], 
                                    project_json["star"],
                                    project_json["score"], 
                                    project_json["date"], 
                                    project_json["tool"], 
                                    project_json["company"], 
                                    project_json["status"])
                # load project into system class project list
                self.system.load_project(project)
                self.system.add_organ(project_json["project_title"], project_json["organization"])
        else: return "No existing file found"
        
        
            
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
                if new_stars in range(1, 7):
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
            tool_ver = ["communities", "custom", "design & as built", "green star buildings", "green star homes", "green star performance", "interiors", "legacy", "perfomance", "railway stations"]
            try:
                new_tool = str(input("Please enter project rating tool \n(Communities, Custom, Design & As Built, Green Star Buildings, Green Star Homes, Green Star Performance, Interiors, Legacy, Perfomance, Railway Stations): "))
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
        
        # _SAVE_DATA_TO_A_JSON_FILE_______________________________________________________________________
        # OBJECT serialization and desrialization using JSON
        # the directory of this Python script
        script_dir = os.path.dirname(os.path.abspath(__file__))
        # create an absolute path to the txt file
        file_path = os.path.join(script_dir, f"projects_data.json")
        # check if this file exist in the given path
        if os.path.exists(file_path):
            with open(file_path, "r") as file:
                existing_data = json.load(file)
                # append to "project" key in json file
                existing_data["project"].append({
                                "project_title": new_ptitle,
                                "location": new_state,
                                "status": new_status,
                                "star": new_stars,
                                "score": int(new_score),
                                "date": new_date,
                                "tool": new_tool,
                                "company": new_company,
                                "organization": new_organization
                            })
                # write to file
                with open(file_path, "w") as file:
                    json.dump(existing_data, file, indent=4)
        # if this json file not exist
        else:   
            # create a json file
            with open(file_path, "w") as file:
                # Create a template of JSON file
                initial_data = '''
                    {
                        "project": [
                            
                        ]
                    }
                '''
                
                # Load the initial string of this file
                new_data = json.loads(initial_data)
                # Add new data to project in this json file
                new_data["project"].append({
                                "project_title": f"{new_ptitle}",
                                "location": f"{new_state}",
                                "status": f"{new_status}",
                                "star": new_stars,
                                "score": int(new_score),
                                "date": f"{new_date}",
                                "tool": f"{new_tool}",
                                "company": f"{new_company}",
                                "organization": f"{new_organization}"
                            })
                # add new string to project with indentation
                new_json = json.dumps(new_data, indent=4)
                # write to json file
                file.write(new_json)  
        
        
    
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
            # add file to the current script folder with write only mode
            with open(file_path, "w", encoding="utf-8") as file:
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
                file.close()
        else: 
            print("This project is not in the system.")
        self.run()
    
    # _MAKE_CHARTS_WITH_JSON_DATA___________________________________________________________________________________
    def chart(self):
        # load the JSON file
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, f"projects_data.json")
        if os.path.exists(file_path):
            with open(file_path, "r") as file:
                projects = json.load(file)
                # create variable to "project" value of Json file
                project_list = projects["project"]
        while True:
            try:
                # create 4 choices
                choice = int(input("Select Pie chart (1), Bar chart (2) or Line chart (3) or return to menu (0): "))
                if choice == 1:
                    certified_tool = {}
                    for project in project_list:
                        if project["status"] == "certified":
                            tool = project["tool"]
                            if tool in certified_tool:
                                certified_tool[tool] += 1
                            else: certified_tool[tool] = 1
                    labels = certified_tool.keys()
                    sizes = certified_tool.values()
                    # plot the chart
                    plt.figure(figsize=(8, 6))
                    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
                    plt.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.
                    plt.title("Certified Ratings Issued By Tool")
                    plt.show()
                elif choice == 2:
                    certified_state = {}
                    for project in project_list:
                        if project["status"] == "certified":
                            state = project["location"]
                            if state in certified_state:
                                certified_state[state] += 1
                            else: certified_state[state] = 1
                    # for loop to make the state uppercase
                    certified_state_upper = {key.upper(): value for key, value in certified_state.items()}
                    certified_state_abs_int = {key: int(abs(value)) for key, value in certified_state.items()}
                    # plot the chart 
                    plt.figure(figsize=(10, 6))
                    plt.bar(certified_state_upper.keys(), certified_state_abs_int.values(), color='skyblue')
                    plt.xlabel('State')
                    plt.ylabel('Number of Certified Ratings')
                    plt.title('Certified Ratings Issued by State')
                    plt.show()
                elif choice == 3:
                    registered_tool = {}
                    for project in project_list:
                        if project["status"] == "registered":
                            tool = project["tool"]
                            if tool in registered_tool:
                                registered_tool[tool] +=1
                            else: registered_tool[tool] = 1
                    
                    registered_tool = dict(sorted(registered_tool.items()))
                    # plot the chart
                    plt.figure(figsize=(10, 6))
                    plt.plot(registered_tool.keys(), registered_tool.values(), marker='o', linestyle='-')
                    plt.xlabel('Tool')
                    plt.ylabel('Number of Registered Ratings')
                    plt.title('Registered Ratings by Tool')
                    plt.xticks(rotation=0)
                    plt.grid(True)
                    plt.show()
                elif choice == 0:
                    self.run()
                else: raise ValueError
            except ValueError: 
                print("Please enter number 1, 2, 3 or 0")
        
            
    # quit function to exit the program
    def quit(self):
        print("Successfully quit") 
        sys.exit()

# run the program from this script 
if __name__ == "__main__":
    program = Menu()
    program.run()