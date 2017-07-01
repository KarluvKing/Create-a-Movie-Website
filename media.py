import webbrowser
'''The Movie class allows create objects with the parameters title, storyline, poster image and youtube trailer. '''
class Movie(): 
	'''Initial function of the class Movie that allows to define and initialize the parameters of one object belongs a class Movie.'''
	def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube
	'''Function that allows to show the movie trailer on youtube by launching the browser.'''	
	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)