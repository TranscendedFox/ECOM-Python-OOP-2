class Company:

    def __init__(self):
        self.__employees = []

    def add_employee(self, employee):
        self.__employees.append(employee)

    def annual_expense(self):

        result = 0

        for employee in self.__employees:
            result += employee.get_bonus_amount() + (employee.monthly_salary * 12)

        return result