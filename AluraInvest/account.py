class Account :

    def __init__( 
        self, 
        number,
        owner_name,
        initial_value,
        debt_limit,
        bank_code = "001"
    ) :
        print( "Accound created ... {}".format(self) )

        self.__number       = number
        self.__owner_name   = owner_name
        self.__balance      = initial_value
        self.__debt_limit   = debt_limit
        self.__bank_code    = bank_code

    def statement(self) :
        print("This Account {} has US${}".format(
                self.__number, 
                self.__balance)
        )

    def deposit(self, value) : 
        self.__balance = self.__balance + value

    def witdraw(self, value) :
        if ( self.__can_witdraw(value) ):
            self.__balance = self.__balance - value
            print("Withdraw was done successfully")
        else : 
            print(f"You dont have enought Balance and Limit to Witdraw the Value of ${value:,.2f}")

    def __can_witdraw(self, value) :
        return (abs(self.__balance) + self.__debt_limit) >= value

    def transfer(self, value, to_account) :
        if ( self.__balance < abs(value) ) :
            print(f"The Account {self.__number} there is no enoght Balance to transfer")
        else :
            self.witdraw(value)
            to_account.deposit(value)
            print(f"Transfer from Account {self.__number} to Account {to_account.__number} with Value of ${value:,.2f}")

    @property
    def limit(self):
        print("Invoking def limit @property")
        print(f"The Limit of the Account {self.__number} is ${self.__debt_limit:,.2f}")
        return self.__debt_limit

    @limit.setter
    def limit(self, new_limit):
        print("Invoking limit.setter")
        if (new_limit >= 0) :
            self.__debt_limit = new_limit
            print(f"Limit modified to ${self.__debt_limit}")
        else: 
            print("You cannot use a Negative Limit Value")

    @property
    def number(self):
        print("Invoking def number @property")
        print(f"The Account Number is {self.__number}")
        return self.__number

    @property 
    def owner_name(self):
        print("Invoking def owner_name @property")
        print(f"The Owner of Account {self.__number} is {self.__owner_name}")
        return self.__owner_name

    @staticmethod
    def bank_codes() :
        banks = {
            "BB"        : "001",
            "CEF"       : "104",
            "Bradesco"  : "237"
        }
        print(banks)
        return banks

#if ( __name__ == "__main__" ) :
'''
conta = Account(123, "Pedro", 30.0, 500)
conta.statement()

conta.deposit( 70.0 )
conta.statement()

conta.witdraw(25)
conta.statement()
'''

account_pedro   =   Account(123, "Pedro", 250.0, 500.0)
account_jubs    =   Account(456, "Jubs",  750, 250)

account_pedro.statement()
account_jubs.statement()

account_pedro.limit
account_pedro.limit = 750

account_pedro.transfer(50, account_jubs)

account_pedro.statement()
account_jubs.statement()

account_pedro.witdraw(83.0)
account_pedro.statement()

Account.bank_codes()