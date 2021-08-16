name="Java"
#print("I know "+name)

myLang="I know {}".format(name)
print(myLang)

myLang="I know {2} {1} {0}".format("Python","Java","JS")
print(myLang)

myLang="I know {p} {j} {js}{}".format(p='Python',j='Java',js='JS')
print(myLang)