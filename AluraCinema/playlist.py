
from    videoProgram    import  Video
from    movie           import  Movie
from    serie           import  Serie

class Playlist(list) :

    def __init__(self, name, video_list) :
        self.__name     = name
        #self.videos   =   video_list
        super().__init__(video_list)
    
    def size(self) :
        return len(self.videos)
    
if ( __name__ == "__main__" ) :
    avengers        =   Movie("Avengers: Infinity Wars", 2018, 160)
    office          =   Serie("The Office", 2005, 9)
    modern_family   =   Serie("Modern Family", 2009, 11)
    matrix          =   Movie("The Matrix", 1999, 136)

    matrix.add_like()
    office.add_like()
    modern_family.add_like()
    avengers.add_like()

    matrix.add_like()
    office.add_like()
    modern_family.add_like()

    office.add_like()
    modern_family.add_like()

    office.add_like()

    video_list      =   [avengers, matrix, modern_family, office]
    playlist        =   Playlist("The Best videos", video_list)

    for video in playlist :
        print(video)

