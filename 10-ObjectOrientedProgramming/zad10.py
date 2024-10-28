class Constructor():
    def __init__(self, artist,titletrack,album,year):
        self.artist=artist
        self.titletrack=titletrack
        self.album=album
        self.year=year
    def __str__(self):
        return f"Performer: {self.artist}\n Song: {self.titletrack}\n Album {self.album}\n Year: {self.year}\n"
     
    
song_data=Constructor("Taylor Swift", "Cruel Summer", "Lover", "2019")
print(song_data)

