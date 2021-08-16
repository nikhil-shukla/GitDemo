#Syntax 1
dict1={1:"nikhil",2:"python",3:"selenium"}
print(dict1)

emp={"QA":"nikhil","dev":"ruba","devops":"chhaya","security":90,50:"python"}
print(emp)
print(type(emp))
print(emp["devops"])
print(emp.get("QA"))
print(emp.get(50))

#storing values in the list in the dictionary
emp2={"QA":["nikhil","rahul","john"],"dev":"ruba","devops":"chhaya"}
print(emp2["QA"])
print(emp2["QA"][2]) #fecthing values from list of dictionary using list concepts of indexing

#Dictionary inside another dictionary
emp3={"QA":"Nikhil","Dev":{"frontend":"rajeev","backend":"neha"}}
print(emp3["Dev"])
print(emp3["Dev"]["backend"]) #one way of accessing values via brackets
print(emp3.get("Dev").get("frontend")) #another way of accessing values via get methods

#add
emp3["Manager"]="ravan"
print(emp3)

emp3["Manager"]="Satya"
print(emp3)

#deletion
emp3.pop("QA") #exact key value pair will be removed
print(emp3)

emp3.popitem() #it will remove in LIFO order
print(emp3)