import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

ramanujan = media.Movie("Ramanujan",
                        "An indian mathematician in Camebridge",
                        "https://teaser-trailer.com/wp-content/uploads/The-Man-Who-Knew-infinity-International-Poster.jpg",
                        "https://www.youtube.com/watch?v=oXGm9Vlfx4w")


#print(toy_story.storyline)
#print(avatar.storyline)
#avatar.show_trailer()
#ramanujan.show_trailer()

movies = [toy_story, avatar, ramanujan]
fresh_tomatoes.open_movies_page(movies)
#print (media.Movie.VALID_RATINGS)
#print (media.Movie.__doc__)
