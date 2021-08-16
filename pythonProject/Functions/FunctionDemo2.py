#default arguments

def sum(num1,num2=0,num3=0,num4=0): #passing default value to avoid missing argument
    result=num1+num2+num3+num4
  #  print("Result is: ",result)  #comma can be used to avoid string to int type error
    return result

newresult=sum(12,12,34)
print("value is ",newresult)