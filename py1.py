class Greet:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello {self.name}!"
    

greet1 = Greet("Dre")
print(greet1.greet())