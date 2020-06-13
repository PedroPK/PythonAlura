class Date :

    def __init__(
        self,
        day,
        month,
        year
    ) :
        self.day    = day
        self.month  = month
        self.year   = year

    def format(self) :
        date = "{:02}/{:02}/{:04}".format(self.day, self.month, self.year)

        return date
        
d = Date(13, 6, 2020)
print(d.format())
