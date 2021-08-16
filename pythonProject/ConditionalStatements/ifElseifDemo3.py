#if condition shorthands
print("Welcome")
if 5>10:print("Yes")
print("Bye")

#if else condition shorthands
marks=80
print("A+") if marks>90 else print("A")

#Nested if condition for shorthands
salary = input("Please enter your salary: ")
print(type(salary))
sal=int(salary)
print(type(sal))
#sal=10000
if sal>40000:
    print("Eligible for car loan")
    if sal>80000:
        print("Eligible for home loan")
        if sal>100000:
            print("Premium customer - eligible for all kinda loans")
else:
    print("Sorry we could not serve you")
