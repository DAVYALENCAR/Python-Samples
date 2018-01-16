import fresh_tomatoes
import media

toy_story = media.Movie(
    "Toy Story",
    "A story of a boy and his toys that come to life",
    "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
    "https://www.youtube.com/watch?v=-9oq-uVwDk8")

wonder_woman = media.Movie(
    "Wonder Woman",
    "Is an movie based on the homonym character of DC Comics by Warner",
    "http://br.web.img2.acsta.net/r_1920_1080" +
    "/pictures/16/11/03/16/33/533535.jpg",
    "https://www.youtube.com/watch?v=bldAkEUANWA")

kingsman = media.Movie(
    "Kingsman",
    "A spy organization recruits an unrefined, " +
    "but promising street kid into the agency",
    "http://t0.gstatic.com/images?q=tbn:ANd9GcRjbufWaA7" +
    "TRXS4z_088Y6PKiIcLsV2wro_fTsQ39PuaI-OQnNf",
    "https://youtu.be/LqehHzvyaKw")

movies = [toy_story, wonder_woman, kingsman]
fresh_tomatoes.open_movies_page(movies)
