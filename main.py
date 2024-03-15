from Model.Employee import Employee
from Model.Role import Role
from Model.Company import Company

if __name__ == '__main__':

    #1 , #2
    role = Role("Software Engineer", "Develops software applications", 1.5)
    employee = Employee("John Doe", "E1234", "Software Engineer", role, 5000)
    employee.get_bonus()
    employee.print_employee()

    #3
    promotion = Role("Customer", "You are fired", 0)
    employee.promote(promotion)
    employee.get_bonus()
    employee.print_employee()

    #4
    company = Company()

    role = Role("Software Engineer", "Develops software applications", 1.5)
    employee_2 = Employee("number 2", "E1235", "Software Engineer", role, 6000)

    company.add_employee(employee)
    company.add_employee(employee_2)

    print(company.annual_expense())

    #5
    def sum_of_array(array):
        sum = 0

        if len(array) > 0:
            first = array[0]
            array.pop(0)
            sum += first + sum_of_array(array)

        return sum

    print(sum_of_array([1,1,2,3,5,8]))

    #6
    def length_of_string(string):

        length = 0

        if string == "":
            return 0

        split = string[1:]
        if split != "":
            length += length_of_string(split)

        return length + 1


    print(length_of_string(""))
    print(length_of_string("abc"))
    print(length_of_string("abcdef"))
    print(length_of_string("abcdefghi"))
