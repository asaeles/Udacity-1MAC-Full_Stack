import webbrowser

class Movie(object):
	def __init__(self, movie_title, movie_year, movie_storyline, movie_poster_url, movie_trailer_url):
		self.title = movie_title
		self.year = movie_year
		self.storyline = movie_storyline
		self.poster_image_url = movie_poster_url
		self.trailer_youtube_url = movie_trailer_url
	
	def play_youtube_video(self):
		webbrowser.open(self.trailer_youtube_url)
