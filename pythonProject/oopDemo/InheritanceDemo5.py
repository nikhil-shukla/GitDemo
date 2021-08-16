class A:
    def sum(self):
        print("calling from A- sum is 15")

class B(A):
    def sum(self):
        print("calling from B- sum is 30")

b=B()
b.sum()