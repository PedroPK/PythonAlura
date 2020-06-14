class Movie :
    pass

    
    def __init__(self, name, year, duration) :
        self.name       = name
        self.year       = year
        self.duration   = duration
    

avengers = Movie("Avengers: Infinity Wars", 2018, 160 )
print(avengers)