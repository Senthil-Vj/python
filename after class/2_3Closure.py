# Nested Function
# Store inner function to the outer function

def greet(name):
    def display_name():
        print("Hi", name)
    display_name()

greet("Raja")



def greet():
    name = "Raja"
    return lambda: "Hi " + name
message = greet()
print(message())

