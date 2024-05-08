print("hello world")


class course:
    def __init__(self,name , marks):
        self.name=name
        self.marks=marks

    def display(self):
        print(self.name, self.marks)
    
c1=course("sail",2.3)

c1.display()

print("hello world")




class Customer:
    def __init__(self,ID,name,rewards):
        self.ID=ID
        self.name=name
        self.rewards=rewards

    def display(self):
        print(self.ID,self.name,self.rewards)

c1=Customer(100,"sahil",66)
c1.display()