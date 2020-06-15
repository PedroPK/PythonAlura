from videoProgram import Video_Program

class Serie (Video_Program):

    def __init__(self, name, year, season) :
        super().__init__(name, year)
        self.season     =   season

hoc     =   Serie("House of Cards", 2013, 6)

hoc.add_like()
print(f"{hoc.name} - {hoc.season}: {hoc.likes}")

hoc.add_like()
print(f"{hoc.name} - {hoc.season}: {hoc.likes}")
#print(f"Name: {hoc.name} - Year: {hoc.year}")