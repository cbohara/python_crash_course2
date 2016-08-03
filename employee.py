class Employee():
    def __init__(self, first_name, last_name, annual_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def print_info(self):
        print(self.first_name.title() + " " + self.last_name.title() +
            " makes $" + str(self.annual_salary) + " per year.")

    def give_raise(self, raise_amount=5000):
        self.annual_salary += raise_amount
        return self.annual_salary
