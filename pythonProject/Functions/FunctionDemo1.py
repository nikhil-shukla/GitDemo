def helloworld():
    print("Hello Python")
    c=10+90
    print(c)
    print("Bye")


#mandatory arguments
def sum(num1,num2):
    result=num1+num2
    print("Result is: ",result)  #comma can be used to avoid string to int type error


#calling defined functions
helloworld()
print(sum(10,25)) #sum doesnt have any return type
