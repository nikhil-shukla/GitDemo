num = int(input("Please enter number: "))

if num==0:
    raise FileNotFoundError #raise a exception of ur choice
print("Number is ",num)