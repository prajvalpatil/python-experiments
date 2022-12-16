'''class complex:
    def __init__(self,r,i):
       self.real = r
       self.img = i
    def __add__(self,other):
        real = self.real+other.real
        img = self.img+other.img
        return real,img
    
c1=complex(10,20)
c2=complex(4,5)
c3=c1+c2
print(c1.real+c2.real,"+",c1.img+c2.img,"i")'''

class complex:
   def __init__(self,r,i):
       self.real = r
       self.img = i

   def __add__(self, other): #overloading addition operator
       temp=complex(0,0)
       temp.real = self.real + other.real
       temp.img = self.img + other.img
       return temp

print("Enter two complex numbers")
r1 = int(input("Enter real part of 1st complex number: "))
c1 = int(input("Enter imaginary part of 1st complex number: "))
r2 = int(input("Enter real part of 2nd complex number: "))
c2 = int(input("Enter imaginary part of 2nd complex number: "))
print("First complex number is {} + {}i".format(r1,c1))
print("Second complex number is {} + {}i".format(r2,c2))
obj1 = complex(r1,c1) 
obj2 = complex(r2,c2) 
obj3= obj1+obj2
print(obj3.real,"+",obj3.img,"i")
print(obj3)
