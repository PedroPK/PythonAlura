class Serie :

    def __init__(self, name, year, season) :
        self.__name       =   name
        self.year       =   year
        self.season     =   season
        self.__likes      =   0

    @property
    def likes(self) :
        return self.__likes

    def add_like(self) :
        self.__likes = self.__likes + 1

    @property
    def name(self) :
        return self.__name
    
    @name.setter
    def name(self, name) :
        self.__name     =   name

hoc     =   Serie("House of Cards", 2013, 6)
print(f"Name: {hoc.name} - Year: {hoc.year}")