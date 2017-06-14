import fresh_tomatoes
import media

toy_story = media.Movie("Titulo do Filme",
						"Descricao do filme",
						"https://images-na.ssl-images-amazon.com/images/M/MV5BNjkwMjAwMTAtM2M3NS00Mzg2LTk5MjUtYjg1MGZiMWNkNDBhXkEyXkFqcGdeQXVyMDY4MzkyNw@@._V1_UY1200_CR65,0,630,1200_AL_.jpg", "https://www.youtube.com/watch?v=QiGN5pey8TM")

#print (toy_story.storyline)

avatar = media.Movie("22Titulo do Filme22",
						"22Descricao do filme22",
						"https://s-media-cache-ak0.pinimg.com/originals/86/9d/98/869d981b871f279da424254c0fad650a.jpg", "https://www.youtube.com/watch?v=6NppN7Gggbw")

#print (avatar.storyline)
#avatar.show_trailer()

movies = [toy_story, avatar]
fresh_tomatoes.open_movies_page(movies)

