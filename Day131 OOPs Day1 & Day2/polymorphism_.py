# Polymorphism

#1. Method overriding
#2. MEthod overloading
#3. Operator overloading


class Geometry:
    def area(self,r):
        return 3.14*r*r
    
    def area(self,l,b):
        return l*b
    


ob = Geometry()
print(ob.area(4))