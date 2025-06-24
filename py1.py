class Name:
    def __init__(self):
        self.name = False

    def setName(self, name):
        self.name = name
    
    def getName(self):
        return f'Name: {self.name} :)'
    

person1 = Name()

person1.setName("Andre")
print(person1.getName())