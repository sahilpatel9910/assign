
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
     reward_rate=100

     def __init__(self,ID,name):
         self.reward_rate=reward_rate

    
    
