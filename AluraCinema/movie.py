class Movie :
    
    def __init__(self, name, year, duration) :
        self.__name     = name
        self.year       = year
        self.duration   = duration
        self.__likes     = 0
    
    @property
    def likes(self) :
        return self.__likes

    def add_like(self) :
        self.__likes    =   self.__likes + 1

    @property
    def name(self) :
        return self.__name

    @name.setter
    def name(self, name) :
        self.__name     =   name
    

avengers = Movie("Avengers: Infinity Wars", 2018, 160 )
print(avengers.name)