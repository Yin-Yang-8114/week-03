class Employee:
    def __init__(self, name,salary):
        self.name = name
        self.salary = salary
    
    def title(self):
        return "employee"
    def monthly_cost(self):
        return self.salary
    def describe(self):
        return f"{self.title()} {self.name} monthly cost: {self.monthly_cost()}"