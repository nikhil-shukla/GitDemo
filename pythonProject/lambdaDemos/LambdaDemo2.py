#Lambda- small anonymous functions

#functionObject=lambda arguments:expression

data= lambda num:num*num
result=data(10)
print(result)


newdata = lambda num1,num2,num3:num1*2+num2*3+num3*4
print(newdata(1,2,3))


#lambda to be used in

map()
filter()

from functools import reduce
reduce()