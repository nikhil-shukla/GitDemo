# MultiLevel Heritance

class A:
    def methodA(self):
        print("I'm from class A")

    def hello_world(self):
        print("hello from class A")


class B(A):
    def methodB(self):
        print("I'm from class B")

    def hello_world(self):                  #method overriding
        print("hello from class B")


class C(B):
    def methodC(self):
        print("I'm from class C")

    def hello_world(self):
        print("hello from class C")

objC = C()
objC.methodC()
objC.methodB()
objC.methodA()
objC.hello_world()
