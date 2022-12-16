name=input("Enter the name of an item\n")
quantity=int(input("Enter the quantity of an item\n"))
value=int(input("Enter the value of an item\n"))

discount=(quantity*value)*0.1
tax=(quantity*value)*0.05
bill_amt=(quantity*value)+tax-discount
print("Name\tquantity\tprice\tdiscount\ttax\ttotal\n")
print(name+"\t"+str(quantity)+"\t\t"+str(value)+"\t"+str(discount)+"\t\t"+str(tax)+"\t"+str(bill_amt)+"\n"  )

