class Account :

    def __init__( 
        self, 
        number,
        owner_name,
        initial_value,
        debt_limit
    ) :
        print( "Accound created ... {}".format(self) )

        self.__number       = number
        self.__owner_name   = owner_name
        self.__balance      = initial_value
        self.__debt_limit   = debt_limit

    def statement(self) :
        print("This Account {} has US${}".format(
                self.__number, 
                self.__balance)
        )

    def deposit(self, value) : 
        self.__balance = self.__balance + value

    def witdraw(self, value) :
        self.__balance = self.__balance - value

    def transfer(self, value, to_account) :
        self.witdraw(value)
        to_account.deposit(value)
        print("Transfer from Account {} to Account {} with Value of ${:03.2f}".format(self.__number, to_account.__number, value))

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

account_pedro.transfer(50, account_jubs)

account_pedro.statement()
account_jubs.statement()
