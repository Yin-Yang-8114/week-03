from employee import Employee


class Intern(Employee):
    def __init__(self, name, salary, mounth):
        super().__init__(name, salary)
        if mounth <= 0 or mounth > 12:
            raise ValueError("mounth must be between 0 and 12")
        self.mounth = mounth
    def title(self):
        return "intern"