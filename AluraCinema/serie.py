from movie import Movie
from videoProgram import Video


class Serie(Video):

    def __init__(self, name, year, season) :
        super().__init__(name, year)
        self.season     =   season

    def __str__(self) :
        serieString     =  f"Type: Serie - Name: {self.name}  - Year: {super().year} - Seasons: {self.season}"
        return serieString

if ( __name__ == "__main__" ) :
    '''
    hoc = Serie("house of Cards", 2013, 6)

    hoc.add_like()
    print(f"{hoc.name} - {hoc.season}: {hoc.likes}")

    hoc.add_like()
    print(f"{hoc.name} - {hoc.season}: {hoc.likes}")
    #print(f"Name: {hoc.name} - Year: {hoc.year}")

    hoc.toString()
    '''

    sessao_da_tarde =   Video("Sessão da Tarde", 1987)
    hoc             =   Serie("house of Cards", 2013, 6)
    avengers        =   Movie("Avengers: Infinity Wars", 2018, 160)

    videos = [sessao_da_tarde, hoc, avengers]
    for video in videos :
        print(video)
