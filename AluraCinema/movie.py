from videoProgram import Video_Program

class Movie (Video_Program):
    
    def __init__(self, name, year, duration) :
        super().__init__(name, year)
        self.duration   = duration

    def toString(self) :
        movieString     =   self.name + " - " + str(super().year) + " - Duration: " + str(self.duration)
        print(movieString)

if (  __name__ == "__main__" ) :
    avengers = Movie("Avengers: Infinity Wars", 2018, 160)

    avengers.add_like()
    print(f"{avengers.name} - {avengers.duration}: {avengers.likes}")

    avengers.add_like()
    print(f"{avengers.name} - {avengers.duration}: {avengers.likes}")

    avengers.toString()
    #print(avengers.name)