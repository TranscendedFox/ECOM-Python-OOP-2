class Employee:
    def __init__(self, name, employee_id, job_title, role, monthly_salary):
        self.__name = name
        self.__employee_id = employee_id
        self.__job_title = job_title
        self.__role = role
        self.__monthly_salary = monthly_salary

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def employee_id(self):
        return self.__employee_id

    @employee_id.setter
    def employee_id(self, employee_id):
        self.__employee_id = employee_id

    @property
    def job_title(self):
        return self.__job_title

    @job_title.setter
    def job_title(self, job_title):
        self.__job_title = job_title

    @property
    def role(self):
        return self.__role

    @role.setter
    def department(self, role):
        self.__role = role

    @property
    def monthly_salary(self):
        return self.__monthly_salary

    @monthly_salary.setter
    def monthly_salary(self, monthly_salary):
        self.__monthly_salary = monthly_salary

    def __calculate_bonus(self, factor):
        return factor * self.__monthly_salary

    def get_bonus(self):
        print(f"{self.name} you got {self.__calculate_bonus(self.__role.monthly_salary_factor)} as the annual bonus.")

    def get_bonus_amount(self):
        return self.__calculate_bonus(self.__role.monthly_salary_factor)

    def print_employee(self):
        print(f"Name: {self.name}, ID: {self.__employee_id}, Title: {self.job_title}, Role: {self.__role.name}, Role description: {self.__role.description} Monthly Salary: {self.__monthly_salary}")

    def promote(self, role):
        self.__role = role