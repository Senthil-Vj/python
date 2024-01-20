class c1:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print("this is function")
    def func1(self):
        print(self.name,self.age)

c=c1("ramesh",45)
c.func1()