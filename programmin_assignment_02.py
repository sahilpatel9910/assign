
class Customer:
    def __init__(self,ID,name,rewards):
        self.ID=ID
        self.name=name
        self.rewards=rewards
        
    def get_reward(self):
        pass
    
    def get_discount(self):
        pass
    
    def update_reward(self):
        pass
    
    def display_info(self):
        pass
    


class BasicCustomer(Customer):
     reward_rate=1.0

     def __init__(self,ID,name):
         super().__init__(ID, name ,0)

     def get_reward(self, total_cost):
         return round(total_cost * self.reward_rate)
     
     def update_reward(self,value):
        self.rewards+=value

     def display_info(self):
         print(f"ID:{self.ID}, Name: {self.name}, rewards: {self.rewards}")

     def set_reward_rate(reward_rate):
         BasicCustomer.reward_rate = reward_rate

    
         
    
         


    
    
