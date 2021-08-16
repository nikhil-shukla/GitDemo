f=open("Demo.txt")
data=f.read()
print(f.name)
print(f.mode)
print(f.closed)
print(data)
f.close()
print(f.closed)

