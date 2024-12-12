#Write a program to create a class with the named employee and
#  create a constructor and destructor. 
# Then, write a function to create an object for that class and delete the object.
#  Make sure you call the function to get everything implemented!

class Employee:
    def __init__(self):
        print("Employee Created")
        
    #destructor
    def __del__(self):
        print("Employee deleted")

def Create_obj():
    print("Creating Object of Employee. . .")
    obj=Employee()
    print("function end. . ")
    return obj

print("Calling function Create_Obj()")
obj=Create_obj()
print("program end. . .")