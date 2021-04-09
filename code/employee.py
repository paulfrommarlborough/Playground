class Employee:
    def __init__(self, first,last,salary):
        self.first = first
        self.last = last
        self.salary=salary

    def give_standard(self):
        self.salary += 5000
   
    def give_custom(self, bonus):
        self.salary += bonus
        

bob = Employee('bob', 'evans', 10000)
bob.give_standard()
print(f" bob = {bob.first}, {bob.last}, {bob.salary}")      