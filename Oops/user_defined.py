class partyAnimal:
    x=0
    def party(self):
        self.x=self.x+1
        print("so far",self.x)
an=partyAnimal()
print(type(an))
print(dir(an))
print(type(an.x))
print(type(an.party))