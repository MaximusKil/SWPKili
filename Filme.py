class Film:
    def __init__(self, titel, release, length):
        self.titel = titel
        self.release = release
        self.length = length

class Horror(Film):
    def __init__(self, titel, release, length, deaths):
        super().__init__(titel, release, length)
        self.deaths = deaths