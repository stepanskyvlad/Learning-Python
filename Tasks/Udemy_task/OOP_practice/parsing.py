class Employee:
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    @classmethod
    def from_string(cls, str_to_parse):
        # data = str_to_parse.split('-')
        # return cls(data[0], data[1], int(data[2]))

        first_name, last_name, salary = str_to_parse.split('-')
        return cls(first_name, last_name, int(salary))


emp1 = Employee('Mary', "Sue", 60000)
emp2 = Employee.from_string("John-Smith-55000")

print(emp1.first_name)
print(emp1.salary)
print(emp2.first_name)
print(emp2.last_name)
print(emp2.salary)
