"""
class Customer:
    def __init__(self,name):
        self.name = name

def greet(customer):
    print(id(customer))
    customer.name="Nitish"
    print(customer.name)
    print(id(customer))
cust = Customer("Prakritee")
#print(id(cust))
greet(cust)

print(cust.name)
"""


"""
def change(L):
    print(id(L))
    L.append(5)
    print(id(L))

L1=[1,2,3,4]
print(id(L1))
print(L1)

change(L1[:])

print(L1)
"""

"""
def change(L):
    print(id(L))
    L.append(5)
    print(id(L))

L1=[1,2,3,4]
print(id(L1))
print(L1)

change(L1)

print(L1)"""


def change(L):
    print(id(L))
    L=L+(5)
    print(id(L))

L1=(1,2,3,4)
print(id(L1))
print(L1)

change(L1)

print(L1)