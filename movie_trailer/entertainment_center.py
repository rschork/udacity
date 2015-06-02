#Import move class from media.py and html creation procedure from fresh_tomatoes.py
import media
import fresh_tomatoes


#Create list of my three favorite movies by instantiating 3 movie classes
Snatch = media.Movie('Snatch','Unscrupulous boxing promoters, violent bookmakers, a Russian gangster, incompetent amateur robbers, and supposedly Jewish jewelers fight to track down a priceless stolen diamond.','http://t3.gstatic.com/images?q=tbn:ANd9GcT99CTVO4nyRGm0UcmDLo7Gv_InmxIoJkVlCDB1pdHho_vYjpig','https://www.youtube.com/watch?v=hiHc2HzO_TA')

Lebowski = media.Movie('The Big Lebowski',"'The Dude' Lebowski, mistaken for a millionaire Lebowski, seeks restitution for his ruined rug and enlists his bowling buddies to help get it.",'http://ia.media-imdb.com/images/M/MV5BMTQ0NjUzMDMyOF5BMl5BanBnXkFtZTgwODA1OTU0MDE@._V1__SX1303_SY615_.jpg','https://www.youtube.com/watch?gl=SG&v=cd-go0oBF4Y&hl=en-GB')

WeddingCrashers = media.Movie('Wedding Crashers','John Beckwith and Jeremy Grey, a pair of committed womanizers who sneak into weddings to take advantage of the romantic tinge in the air, find themselves at odds with one another when John meets and falls for Claire Cleary.','http://ia.media-imdb.com/images/M/MV5BMTc4NTUyNzU4MV5BMl5BanBnXkFtZTcwMzcyMTkyMQ@@._V1__SX1303_SY615_.jpg','https://www.youtube.com/watch?v=ZeUSo8voIXM')

#Generate HTML for static web page and launch
fresh_tomatoes.open_movies_page([Snatch,Lebowski,WeddingCrashers])
