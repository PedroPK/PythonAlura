class Video :

    def __init__(self, name, year) :
        self.__name     =   name.title()
        self.__year     =   year
        self.__likes    =   0


    def __str__(self) :
        video_string    =   (
            f"Type: Video Program - "
            f"Name: {self.__name} - "
            f"Year: {self.__year} - "
            f"Likes: {self.likes}"
        )
        return video_string

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
    sessao_da_tarde =   Video("Sessão da Tarde", 1983)
    print(sessao_da_tarde)

    #hoc         =   Serie("house of Cards", 2013, 6)
    #avengers    =   Movie("Avengers: Infinity Wars", 2018, 160)

