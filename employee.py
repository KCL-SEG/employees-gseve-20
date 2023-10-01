"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, unit_pay, type, period=1, comission_pay=0,number_of_comissions=0):
        self.name = name
        self.unit_pay = unit_pay
        self.type = type
        self.period = period
        self.comission_pay = comission_pay
        self.number_of_comissions = number_of_comissions
        


    def get_pay(self):
        return self.unit_pay*self.period + self.comission_pay*self.number_of_comissions

    def __str__(self):
        if self.type == 'monthly':
            string_one =  f"{self.name} works on a monthly salary of {self.unit_pay}"
        else:
            string_one =  f"{self.name} works on a contract of {self.period} hours at {self.unit_pay}/hour"
        if self.number_of_comissions == 1:
            string_two = f" and receives a bonus commission of {self.comission_pay}."
        elif self.comission_pay:
            string_two = f" and receives a commission for {self.number_of_comissions} contract(s) at {self.comission_pay}/contract."
        else:
            string_two = "."
        return string_one + string_two + f" Their total pay is {self.get_pay()}."


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', 4000, type='monthly')


# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', 25, period=100, type='hourly')

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee',3000,comission_pay=200, number_of_comissions=4, type='monthly' )

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan',25,period=150,type='hourly',comission_pay=220,number_of_comissions=3)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie',2000,comission_pay=1500,number_of_comissions=1,type='monthly')

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel',30,period=120,comission_pay=600,number_of_comissions=1,type='hourly')

