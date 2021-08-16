name="Python"
for n in name:
    print(n)

marks=[70,80,90,100]
finalmarks=0

for m in marks:
    print(m)

print("Bye")

for m in [70,45,78,98]:
    finalmarks=finalmarks+m
    if m%2==0:
        print("even no")
    else:
        print("odd no")
print(finalmarks)
print("Final value is: "+str(finalmarks))