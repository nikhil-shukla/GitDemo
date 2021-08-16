#arbitory arguments

#normal way
def print_name(name1,name2):
    print(name1,name2)

print_name("Python","Java")


#"*args" - it will recieve values in tuples
#instead of args we can use anything like *nik
def print_name(*args):
    print(args)
    print(args[2])
    for x in args:
        print(x)

print_name("Python","Java","C","JS","Ruby")

def get_sum_of_all_numbers(*args):
    print(sum(args))

def get_min_number(*args):
    print(min(args))

def get_max_number(*args):
    print(max(args))

get_sum_of_all_numbers(10,30,60)
get_min_number(90,25,62,35,15)
get_max_number(101,485,45,86)
