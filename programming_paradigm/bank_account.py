class BankAccount :
    def __init__(self,intial_balance=0) :
        self.__account_balanc = intial_balance

    def deposite(self, amount) :
        if amount > 0 :
            self.__account_balanc += amount

    def withdrow (self, amount) :
        if amount > 0 and self.__account_balanc >= amount:
            self.__account_balanc -= amount
            return True
        return False
    
    def display_balance (self) :
        print(f"Current Balance : {self.__account_balanc}")


        
