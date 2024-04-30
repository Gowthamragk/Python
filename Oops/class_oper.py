# CLASS EXAMPLE

class PartyAnimal:
    x = 0
    def party(self):               # Methods
        self.x = self.x+1
        print("so far",self.x)
        
a = PartyAnimal()  # a is the object here
b = PartyAnimal()

a.party()      
a.party()       # if same class is called twice the value of the variables will not be changed
b.party()