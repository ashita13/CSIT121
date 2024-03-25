# create a dict to store organizations name as key
# and role as value
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
    

