#constructor with inheritance

class A:
    def __init__(self): #__init_- is used for creation of constructor
        print("I'm from class A")

class B(A):
    def __init__(self):
        super(B, self).__init__()
        A.__init__(self)
        print("I'm from class B")

obj1= B()