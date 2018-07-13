class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullName(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee('Corey', 'Schafer', '50000')
emp_2 = Employee('Brian', 'Yego', '60000')


print(emp_1.pay)
print(emp_2.email)


Employee.fullName(emp_1)
# print(emp_1.fullName())
