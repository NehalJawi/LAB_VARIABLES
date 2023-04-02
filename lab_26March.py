from ast import And


my_fav_movie = "The Lion King"
movie_rate :int = 3
movie_popularity_score = 72.65
if movie_rate>=4 and movie_popularity_score > 80:
    print("highly Recommended")
elif movie_rate>=3 and movie_popularity_score > 70:
    print("I recommend it. . It is good ")
elif movie_rate<=2 and movie_popularity_score >60:
    print("you should check it out")
elif movie_rate<=2 and movie_popularity_score <50:
    print("Dont Watch it, Its waste of time")