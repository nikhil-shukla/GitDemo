# Multiple Heritance
#MRO - MEthod Resolution order - is the order in which python looks for a method in hierarchy of classes

class A:
    def methodA(self):
        print("I'm from class A")

    def hello_world(self):
        print("hello from class A")


class B:
    def methodB(self):
        print("I'm from class B")

    def hello_world(self):                  #method overriding
        print("hello from class B")


class C(A,B): #in case of A being first A's same name method will b called an d vice-versa
    def methodC(self):
        print("I'm from class C")


objC = C()
objC.methodC()
objC.methodB()
objC.methodA()
#objC.hello_world1()
#objC.hello_world2()
objC.hello_world()

print(C.mro())