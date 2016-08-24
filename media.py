import webbrowser
class Song:
    def __init__(self,songname,songmovie,songimage,songyoutube):
        self.title=songname
        self.storyline=songmovie
        self.poster_image_url=songimage
        self.trailer_youtube_url=songyoutube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
