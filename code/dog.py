class dog:
    def __init__(self, name, age):
        self.name = name 
        self.age = age
        self.sitflag = False

    def sit(self):
        self.sitflag = True

    def stand(self):
        self.sitflag = False

    def doing(self):
        if (self.sitflag == True):
            print(f"{self.name} is sitting")
        else:
            print(f"{self.name} is standing")


willie = dog('willie', 5)
willie.sit()
lucy = dog('lucy', 2)

sidney = dog('sidney', 3)


willie.doing()
lucy.doing()
sidney.doing()