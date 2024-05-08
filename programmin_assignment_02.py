print("hello world")


class course:
    def __init__(self,name , marks):
        self.name=name
        self.marks=marks

    def display(self):
        print(self.name, self.marks)
    
c1=course("sail",2.3)

c1.display()