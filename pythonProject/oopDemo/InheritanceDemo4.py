# Hybrid Heritance

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

class D(C):
    def methodD(self):
        print("I'm from class D")

objD = D()
objD.methodD()
objD.methodC()
objD.methodB()
objD.methodA()
#objC.hello_world1()
#objC.hello_world2()
objD.hello_world()

print(D.mro())