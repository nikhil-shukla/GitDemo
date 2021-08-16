#Errors detected during runtime is called exceptions

#example1:
try:
    content=open("F:\Study\pythonProject\Demo1.txt","r")
    print(content.read())

except FileNotFoundError as err:
    print("Something went wrong", err)

print("Last statement")

#example2
try:
    val = input("enter number: ")
    v=int(val)
    print(5/v)

except TypeError as e:
    print("provide numbers", e)

except ZeroDivisionError as e:
    print("Dnt give zero", e)

except ValueError as e:
    print("provide valid entries",e)

except Exception as e:
    print("All errors handled - something went wrong")

else: #when no exception else will execute
    print("All went right")

finally: #it will execute alwz
    print("Bye")




