#keyword arbitory arguments
#kwargs will recieve value as adictionary

def print_names(**kwargs):
    print(kwargs)
    print(kwargs["phone"])

    for x,y in kwargs.items():
        print(x,y)

print_names(name="nikhil",address="indore",phone=1522)

#both *args and **kwargs in one function

def hello_world(fname,*args,**kwargs):
    print(fname)
    print(args)
    print(kwargs)

hello_world(10,20,"nikhil",name="python",country="india")