"""  die_class.py : excerise to code  a class """
from random import randint 

class die:
    def __init__(self, value=6, maxvalue=6):
        self.value = value
        self.maxvalue = maxvalue

    def roll(self):
        self.value = randint(1, self.maxvalue)

    def seriesroll(self, tries):
        print(f"ROLL D{self.maxvalue}   {tries} TIMES")
        for i in range(1, tries+1):
            self.roll()
            print (f"D{self.maxvalue} roll {i} is {self.value}")                    

dice = die(2)
print (f"dice value is {dice.value}")        
dice.roll()
print (f"roll dice value is {dice.value}")        

d20 = die(1, 20)
print (f"d20 value is {d20.value}")        
d20.roll()
print (f"d20 value is {d20.value}")        

d20.seriesroll(10)