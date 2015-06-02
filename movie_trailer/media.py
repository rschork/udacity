#Import webbrowser to launch link containing Youtube trailer
import webbrowser

#Create class definition for Movie. Initiates with 4 attributes:
#Movie Title, Storyline, Poster Image (via URL), Youtube Tailer (via URL)
class Movie:
  '''Creates a template for a movie webpage'''
  def __init__(self,movie_title,movie_storyline,poster_image_url,trailer_youtube_url):
    self.title=movie_title
    self.movie_storyline=movie_storyline
    self.poster_image_url=poster_image_url
    self.trailer_youtube_url=trailer_youtube_url

#Create procedure to launch youtube trailer. Launched on click from static website.
  def show_trailer(self):
    webbrowser.open(self.trailer_youtube_url)
