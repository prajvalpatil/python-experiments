class person:
    __name=""
    __age=0
    __gender=""
    def get(self):
        self.name=input("Enter the name: ")
        self.age=int(input("Enter your age"))
        self.gender=input("ENter your gender")
    def display(self):
        print("Name:",self.name)
        print("\nAge:",self.age)
        print("\nGender:",self.gender)
class faculty(person):
    __designation=""
    __dept=""
    def set(self):
        super().get()
        self.designation=input("Enter your post:")
        self.dept=input("Enter your department:")
    def show(self):
        super().display()
        print("Disignation:",self.designation)
        print("Department:",self.dept)
class publication(faculty):
    __noresearch=0
    __nobooks=0
    __noarticles=0
    def read(self):
        super().set()
        self.noresearch=int(input("Enter no of research publications:"))
        self.nobooks=int(input("Enter no of books:"))
        self.noarticles=int(input("Enter no of articles:"))
    def print(self):
        super().show()
        print("NOrp:",self.noresearch)
        print("NObooks:",self.nobooks)
        print("NOart:",self.noarticles)
f1=publication()
f1.read()
f1.print()
