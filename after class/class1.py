#class creation
class myclass():
    x = 5
print(myclass)

#object creation
class myclass():
    x=5
ob = myclass()
print(ob.x)

class add():
    a = 5
    b = 10
    c = a+b
ob = add()
print(ob.c)

class sub():
    x = int(input("Enter a number:"))
    y = int(input("Enter b number"))
    z = x - y
ob = sub()
print(ob.z)

class mult:
    x = 10
    y = 2
    z = x*y
print(mult.z)

class function():
    x = int(input("Enter a number:"))
    y = int(input("Enter b number:"))
    z = x//y
ob = function()
print(ob.z)



