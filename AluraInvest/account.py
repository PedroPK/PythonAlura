class Account :

    def __init__( 
        self, 
        number,
        owner_name,
        initial_value,
        debt_limit
    ) :
        print( "Accound created ... {}".format(self) )

        self.number = number
        self.owner_name = owner_name
        self.balance = initial_value
        self.debt_limit = debt_limit

    def statement(self) :
        print("This Account {} has US${}".format(
                self.number, 
                self.balance)
        )

    def deposit(self, value) : 
        self.balance = self.balance + value

    def witdraw(self, value) :
        self.balance = self.balance - value

#if ( __name__ == "__main__" ) :
conta = Account(123, "Pedro", 30.0, 500)
conta.statement()

conta.deposit( 70.0 )
conta.statement()

conta.witdraw(25)
conta.statement()