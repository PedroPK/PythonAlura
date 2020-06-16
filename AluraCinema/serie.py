from movie import Movie
from videoProgram import Video_Program


class Serie(Video_Program):

    def __init__(self, name, year, season) :
        super().__init__(name, year)
        self.season     =   season

    def toString(self) :
        serieString     =   self.name + " - " + str(super().year) + " - Seasons: " + str(self.season)
        print(serieString)

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

    hoc         =   Serie("house of Cards", 2013, 6)
    avengers    =   Movie("Avengers: Infinity Wars", 2018, 160)

    videos = [hoc, avengers]
    for video in videos :
        video.toString()
