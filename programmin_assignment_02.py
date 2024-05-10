
class Customer:
    def __init__(self,ID,name,reward):
        self.ID=ID
        self.name=name
        self.reward=reward
        
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
        self.reward+=value

     def display_info(self):
         print(f"ID:{self.ID}, Name: {self.name}, rewards: {self.reward}")

     @staticmethod
     def set_reward_rate(reward_rate):
         BasicCustomer.reward_rate = reward_rate


class VIPCustomer(Customer):
    reward_rate=100
    discount_rate=0.08

    def get_discount(self,total_cost):
        total_cost=total_cost * self.discount_rate
        return total_cost
    
    def get_reward(self,total_cost):
        discount=self.get_discount(total_cost)
        total_cost= total_cost-discount
        reward= round(total_cost+self.reward_rate )
        return reward
    
    def update_reward(self,value):
        self.reward+= value
    
    def display_info(self):
        print(f"ID: {self.ID}, Name: {self.name}, Reward: {self.reward}, Discount Rate: {self.discount_rate}")

    @staticmethod
    def set_reward_rate(reward_rate):
        VIPCustomer.reward_rate = reward_rate

    def set_discount_rate(self, discount_rate):
        self.discount_rate = discount_rate

    


    
         
    
         


    
    
