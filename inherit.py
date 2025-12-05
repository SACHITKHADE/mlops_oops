'''class Animal:
    def __init__(self,name):
        self.name=name
    def speak(self):
        print(f"{self.name} is making sound")

class Dog(Animal):
    def speak(self):
        print(f"{self.name} is barking")

animal=Animal("generic animal")
animal.speak()
dog=Dog("tomy")
dog.speak()'''
class Animal:
    def __init__(self):
        self.name='tomy'
    def speak(self):
        print(f"{self.name} is making sound")

class Dog(Animal):
    def __init__(self, breed):
        super().__init__() # used to take the atrribute initiated by parent class
        self.breed=breed
    def speak(self):
        super().speak()# call the method form parent class
        print(f"{self.name} is barking, it is a {self.breed}")

dog=Dog("german shefferd")
dog.speak()