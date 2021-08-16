status=False

lang= input("Please enter language: ")

names=["python","java","c#"]

for name in names:
    if name==lang:
        status=True
    else:
        print("Please wait we are still searching")

if status==True:
    print("We found it")
else:
    print("Sorry")