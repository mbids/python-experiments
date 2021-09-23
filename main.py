class Employee:
    
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.email = first + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee('Ghe','Boi')
emp_2 = Employee('Yeet','Machine')




