class store:
    price=0
    code=0
    quantity=0
    def __init__(self,code,price,quantity):
       self.code=code
       self.price=price
       self.quantity=quantity
    def calculate(self):
       amount=self.price*self.quantity
       print(amount)
a=store("abc",100,5)
b=store("xyz",200,5)
#
a.calculate()
total=a.price*a.quantity + b.price*b.quantity
print(total)
