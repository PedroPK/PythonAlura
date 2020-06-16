#from serie import Serie
#from movie import Movie

class Video_Program (object) :

    def __init__(self, name, year) :
        self.__name     =   name.title()
        self.__year     =   year
        self.__likes    =   0

    @property
    def year(self) :
        return self.__year
    
    @year.setter
    def year(self, year) :
        self.__year = year

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

#hoc         =   Serie("house of Cards", 2013, 6)
#avengers    =   Movie("Avengers: Infinity Wars", 2018, 160)

