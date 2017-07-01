# Import fresh_tomatoes, to make the movies available on a web page
import fresh_tomatoes
# Import media to gain access to the class that defines each movie or instance
import media

# The Wolf of Wall Street movie:
# Movie title, storyline, poster image and movie trailer
theWolfofWallStreet = media.Movie(
  "The Wolf of Wall Street",
  "Based on the true story of Jordan Belfort, from his rise to a wealthy"
  "stock-broker living the high life to his fall involving crime, corruption"
  "and the federal government.",
  "https://images-na.ssl-images-amazon.com/images/M/MV5BMjIxMjgxNTk0MF5BMl5BanBnXkFtZTgwNjIyOTg2MDE@._V1_SY1000_CR0,0,674,1000_AL_.jpg",  # NOQA
  "https://www.youtube.com/watch?v=iszwuX1AK6A"
  )

# The Conjuring movie:
# Movie title, storyline, poster image and movie trailer
theConjuring = media.Movie(
  "The Conjuring",
  "Paranormal investigators Ed and Lorraine Warren work to"
  "help a family terrorized by a dark presence in their farmhouse.",
  "https://images-na.ssl-images-amazon.com/images/M/MV5BMTM3NjA1NDMyMV5BMl5BanBnXkFtZTcwMDQzNDMzOQ@@._V1_SY1000_CR0,0,674,1000_AL_.jpg",  # NOQA
  "https://www.youtube.com/watch?v=k10ETZ41q5o"
  )

# The Lone Survivor movie:
# Movie title, storyline, poster image and movie trailer
loneSurvivor = media.Movie(
  "Lone Survivor",
  "Marcus Luttrell and his team set out on a mission to capture or kill"
  "notorious Taliban leader Ahmad Shah, in late June 2005. Marcus and his"
  "team are left to fight for their lives in one of the most valiant efforts"
  "of modern warfare.",
  "https://images-na.ssl-images-amazon.com/images/M/MV5BMjA0NTgwOTk5Ml5BMl5BanBnXkFtZTcwMjE3NDc5OQ@@._V1_SY1000_SX675_AL_.jpg",  # NOQA
  "https://www.youtube.com/watch?v=WGexkC-lvh4"
  )

# The 12 Years a Slave movie:
# Movie title, storyline, poster image and movie trailer
yearsaSlave = media.Movie(
  "12 Years a Slave",
  "In the antebellum United States, Solomon Northup, a free black man from"
  "upstate New York is abducted and sold into slavery.",
  "https://images-na.ssl-images-amazon.com/images/M/MV5BMjExMTEzODkyN15BMl5BanBnXkFtZTcwNTU4NTc4OQ@@._V1_.jpg",  # NOQA
  "https://www.youtube.com/watch?v=z02Ie8wKKRg"
  )

# The Rush movie:
# Movie title, storyline, poster image and movie trailer
rush = media.Movie(
  "Rush",
  "The merciless 1970s rivalry between Formula One rivals James Hunt and"
  "Niki Lauda.",
  "https://images-na.ssl-images-amazon.com/images/M/MV5BOWEwODJmZDItYTNmZC00OGM4LThlNDktOTQzZjIzMGQxODA4XkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SY1000_SX675_AL_.jpg",  # NOQA
  "https://www.youtube.com/watch?v=lzNbGH1oZJc"
  )

# The Dallas Buyers Club movie:
# Movie title, storyline, poster image and movie trailer
dallasBuyersClub = media.Movie(
  "Dallas Buyers Club",
  "In 1985 Dallas, electrician and hustler Ron Woodroof works around the"
  "system to help AIDS patients get the medication they need after he is"
  "diagnosed with the disease.",
  "https://images-na.ssl-images-amazon.com/images/M/MV5BMTYwMTA4MzgyNF5BMl5BanBnXkFtZTgwMjEyMjE0MDE@._V1_SY1000_CR0,0,674,1000_AL_.jpg",  # NOQA
  "https://www.youtube.com/watch?v=U8utPuIFVnU"
  )

# The Lovelace movie:
# Movie title, storyline, poster image and movie trailer
lovelace = media.Movie(
  "Lovelace",
  "The story of Linda Lovelace, who is used and abused by the porn industry"
  "at the behest of her coercive husband, before taking control"
  "of her life.",
  "https://images-na.ssl-images-amazon.com/images/M/MV5BOTM0Mzc2MjgyN15BMl5BanBnXkFtZTcwOTIzNDQ4OQ@@._V1_.jpg",  # NOQA
  "https://www.youtube.com/watch?v=HPJY-g-WoQo"
  )

# The Yi dai zong shi movie:
# Movie title, storyline, poster image and movie trailer
yidaizongshi = media.Movie(
  "Yi dai zong shi",
  "The story of martial-arts master Ip Man, the man who trained Bruce Lee.",
  "https://images-na.ssl-images-amazon.com/images/M/MV5BMTY1NDYxNDA5OF5BMl5BanBnXkFtZTcwNjk3NDk0OQ@@._V1_SY1000_CR0,0,716,1000_AL_.jpg",  # NOQA
  "https://www.youtube.com/watch?v=LfJz4C81nu0"
  )

# The Stalingrad movie:
# Movie title, storyline, poster image and movie trailer
stalingrad = media.Movie(
  "Stalingrad",
  "A band of Russian soldiers fight to hold a strategic building in their"
  "devastated city against a ruthless German army, and in the process"
  "become deeply connected to two Russian women who have been living there.",
  "https://images-na.ssl-images-amazon.com/images/M/MV5BMTU2NjE5NTE5MV5BMl5BanBnXkFtZTgwODMxMjMyMTE@._V1_SY1000_CR0,0,676,1000_AL_.jpg",  # NOQA
  "https://www.youtube.com/watch?v=OlMw8CjyV80"
  )

# List of movies that will be "uploaded" later on fresh_tomatoes
movies = [
  theWolfofWallStreet,
  theConjuring,
  loneSurvivor,
  yearsaSlave,
  rush,
  dallasBuyersClub,
  lovelace,
  yidaizongshi,
  stalingrad
  ]
# Upload the list of movies in fresh_tomatoes which will then allow to
# open the HTML and view the website.
fresh_tomatoes.open_movies_page(movies)
