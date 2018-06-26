import webbrowser

class Movie(object):
	def __init__(self, movie_title, movie_storyline, movie_youtube_url, movie_poster_url):
		self.title = movie_title
		self.storyline = movie_storyline
		self.youtube_url = movie_youtube_url
		self.poster_url = movie_poster_url
	
	def play_youtube_video(self):
		webbrowser.open(self.youtube_url)
