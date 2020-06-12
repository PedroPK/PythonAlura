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
        self.initial_value = initial_value
        self.debt_limit = debt_limit