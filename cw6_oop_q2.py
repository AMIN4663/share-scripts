class BankAccount:
    def __init__(self,balance:int):
        self.__balance = balance
        
    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self,value:int):
        if value < 0:
            raise ValueError("Balance cannot be negative")
        self.__balance=value
          
    @classmethod
    def from_string(cls,data:str):
        if isinstance(data,str):
            data=data.split(",")
            owner=data[0]
            cls.balance=int(data[1])
        
        return f"owner:{owner},balance:{cls.balance}"

    

new_user=BankAccount(100)
print(new_user.balance)

owner=new_user.from_string("ali,1500")
print(owner)


