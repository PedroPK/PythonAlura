class Video_Program :

    def __init__(self, name, year) :
        self.__name     =   name
        self.__year     =   year
        self.__likes    =   0

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