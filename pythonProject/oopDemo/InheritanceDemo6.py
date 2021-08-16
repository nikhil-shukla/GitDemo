class A:
    def sum(self):
        print("calling from A- sum is 15")

    def bye(self):
        print("calling from A- sum is 45")

class B(A):
    def sum(self):
        super().sum()
        super().bye()
     #   A.sum(self) #one way to call parent method
        print("calling from B- sum is 30")

b=B()
b.sum()