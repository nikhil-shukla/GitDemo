#SingleLevel Heritance

class Base:
    name="nikhil"
    def baseMethod(self):
        print("I'm in base class")

class Child(Base):
    company="nik"
    def childMethod(self):
        print("I'm in child class")

c= Child()
c.childMethod()

#b= Base()
c.baseMethod()
print(c.name,c.company)