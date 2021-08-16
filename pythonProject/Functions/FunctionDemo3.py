#keywards arguments

def greeting(fname,lname,marks=0):
    print("Welcome "+fname+" "+lname+" "+str(marks))

greeting("nikhil","shukla")

greeting("shukla","nikhil")

#keywards arguments
greeting(fname="nikhil",lname="shukla",marks=95)

greeting(marks=95,lname="shukla",fname="nikhil")