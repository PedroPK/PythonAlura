class Video_Program :

    def __init__(self, name, year) :
        self.__name     =   name.title()
        self.__year     =   year
        self.__likes    =   0


    def __str__(self) :
        return f"Type: Video Program - Name: {self.__name} - Year: {self.__year} - Likes: {self.__likes}"

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

if ( __name__ == "__main__" ) :
    sessao_da_tarde =   Video_Program("Sessão da Tarde", 1983)
    print(sessao_da_tarde)

    #hoc         =   Serie("house of Cards", 2013, 6)
    #avengers    =   Movie("Avengers: Infinity Wars", 2018, 160)

