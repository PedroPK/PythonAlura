from videoProgram import Video

class Movie (Video):
    
    def __init__(self, name, year, duration) :
        super().__init__(name, year)
        self.duration   = duration

    def __str__(self) :
        movieString     =   f"Type: Movie - Name: {self.name}  - Year: {super().year} Duration: {self.duration}"
        return movieString

if (  __name__ == "__main__" ) :
    avengers = Movie("Avengers: Infinity Wars", 2018, 160)

    avengers.add_like()
    print(f"{avengers.name} - {avengers.duration}: {avengers.likes}")

    avengers.add_like()
    print(f"{avengers.name} - {avengers.duration}: {avengers.likes}")

    print(avengers)
    #print(avengers.name)