class QueryBase:
    def query(self):
        raise NotImplementedError

class Employee(QueryBase):
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def query(self):
        return f"Employee: {self.name}, ID: {self.emp_id}"

class Team(QueryBase):
    def __init__(self, team_name, members):
        self.team_name = team_name
        self.members = members  # List of Employee objects

    def query(self):
        return f"Team: {self.team_name}, Members: {[m.name for m in self.members]}"
