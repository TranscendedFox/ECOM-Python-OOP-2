class Role:
    def __init__(self, name, description, monthly_salary_factor):
        self.__name = name
        self.__description = description
        self.__monthly_salary_factor = monthly_salary_factor

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description):
        self.__description = description

    @property
    def monthly_salary_factor(self):
        return self.__monthly_salary_factor

    @monthly_salary_factor.setter
    def monthly_salary_factor(self, monthly_salary_factor):
        self.__monthly_salary_factor = monthly_salary_factor