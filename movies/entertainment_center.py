import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story", 1995, "Toy Story's storyline", r'https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg', r'https://www.youtube.com/watch?v=Ny_hRfvsmU8')
a_bugs_life = media.Movie("A Bug's Life", 1998, "A Bug's Life's storyline", r'https://upload.wikimedia.org/wikipedia/en/c/cc/A_Bug%27s_Life.jpg', r'https://www.youtube.com/watch?v=mE35XQFxbeo')
toy_story_2 = media.Movie("Toy Story 2", 1999, "Toy Story 2's storyline", r'https://upload.wikimedia.org/wikipedia/en/c/c0/Toy_Story_2.jpg', r'https://www.youtube.com/watch?v=Lu0sotERXhI')
monsters_inc = media.Movie("Monsters, Inc.", 2001, "Monsters, Inc.'s storyline", r'https://upload.wikimedia.org/wikipedia/en/6/63/Monsters_Inc.JPG', r'https://www.youtube.com/watch?v=6tCxnHCqqxg')
finding_nemo = media.Movie("Finding Nemo", 2003, "Finding Nemo's storyline", r'https://upload.wikimedia.org/wikipedia/en/2/29/Finding_Nemo.jpg', r'https://www.youtube.com/watch?v=SPHfeNgogVs')
the_incredibles = media.Movie("The Incredibles", 2004, "The Incredibles's storyline", r'https://upload.wikimedia.org/wikipedia/en/e/ec/The_Incredibles.jpg', r'https://www.youtube.com/watch?v=eZbzbC9285I')
cars = media.Movie("Cars", 2006, "Cars's storyline", r'https://upload.wikimedia.org/wikipedia/en/3/34/Cars_2006.jpg', r'https://www.youtube.com/watch?v=SbXIj2T-_uk')
ratatouille = media.Movie("Ratatouille", 2007, "Ratatouille's storyline", r'https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg', r'https://www.youtube.com/watch?v=jOGDozdW9Yo')
wall_e = media.Movie("WALL-E", 2008, "WALL-E's storyline", r'https://upload.wikimedia.org/wikipedia/en/c/c2/WALL-Eposter.jpg', r'https://www.youtube.com/watch?v=8-_9n5DtKOc')
up = media.Movie("Up", 2009, "Up's storyline", r'https://upload.wikimedia.org/wikipedia/en/0/05/Up_%282009_film%29.jpg', r'https://www.youtube.com/watch?v=HWEW_qTLSEE')
toy_story_3 = media.Movie("Toy Story 3", 2010, "Toy Story 3's storyline", r'https://upload.wikimedia.org/wikipedia/en/6/69/Toy_Story_3_poster.jpg', r'https://www.youtube.com/watch?v=2BlMNH1QTeE')
cars_2 = media.Movie("Cars 2", 2011, "Cars 2's storyline", r'https://upload.wikimedia.org/wikipedia/en/7/7f/Cars_2_Poster.jpg', r'https://www.youtube.com/watch?v=oFTfAdauCOo')
brave = media.Movie("Brave", 2012, "Brave's storyline", r'https://upload.wikimedia.org/wikipedia/en/9/96/Brave_Poster.jpg', r'https://www.youtube.com/watch?v=TEHWDA_6e3M')
monsters_university = media.Movie("Monsters University", 2013, "Monsters University's storyline", r'https://upload.wikimedia.org/wikipedia/en/2/2a/Monsters_University_poster_3.jpg', r'https://www.youtube.com/watch?v=xBzPioph8CI')
inside_out = media.Movie("Inside Out", 2015, "Inside Out's storyline", r'https://upload.wikimedia.org/wikipedia/en/0/0a/Inside_Out_%282015_film%29_poster.jpg', r'https://www.youtube.com/watch?v=yRUAzGQ3nSY')
the_good_dinosaur = media.Movie("The Good Dinosaur", 2015, "The Good Dinosaur's storyline", r'https://upload.wikimedia.org/wikipedia/en/8/80/The_Good_Dinosaur_poster.jpg', r'https://www.youtube.com/watch?v=O-RgquKVTPE')
finding_dory = media.Movie("Finding Dory", 2016, "Finding Dory's storyline", r'https://upload.wikimedia.org/wikipedia/en/3/3e/Finding_Dory.jpg', r'https://www.youtube.com/watch?v=JhvrQeY3doI')
cars_3 = media.Movie("Cars 3", 2017, "Cars 3's storyline", r'https://upload.wikimedia.org/wikipedia/en/9/94/Cars_3_poster.jpg', r'https://www.youtube.com/watch?v=2LeOH9AGJQM')
coco = media.Movie("Coco", 2017, "Coco's storyline", r'https://upload.wikimedia.org/wikipedia/en/9/98/Coco_%282017_film%29_poster.jpg', r'https://www.youtube.com/watch?v=Rvr68u6k5sI')
incredibles_2 = media.Movie("Incredibles 2", 2018, "Incredibles 2's storyline", r'https://upload.wikimedia.org/wikipedia/en/2/27/The_Incredibles_2.jpg', r'https://www.youtube.com/watch?v=i5qOzqD9Rms')

movies = [toy_story, a_bugs_life, toy_story_2, monsters_inc, finding_nemo,
	the_incredibles, cars, ratatouille, wall_e, up, toy_story_3, cars_2,
	brave, monsters_university, inside_out, the_good_dinosaur,
	finding_dory, cars_3, coco, incredibles_2]

fresh_tomatoes.open_movies_page(movies)