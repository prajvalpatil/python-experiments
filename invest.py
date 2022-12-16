pa=int(input("Enter the prinipal amount\n"))
print("principal amount=",pa)
roi=0.05
for i in range(1,6):
    pa=(pa*roi)+pa
ma=pa
print("\nMaturity amount after 5 years of span =",ma)
