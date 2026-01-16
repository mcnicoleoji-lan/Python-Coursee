# Class creation
class myClass:
    # private variable
    __privateVar = 11;

    # private method
    def __privMeth(self):
        print("I'm inside class myClass Yaaaaayyy!!!")

    # Function to print value of private variable
    def hello(self):
        print("Private Variable value: ", self.__privateVar)
# Function to print value of private variable
def hello(self):
    print("Private Variable value: ", self.__privateVar)
#Object creation and method call
foo = myClass()
foo.hello()
foo.__privMeth()