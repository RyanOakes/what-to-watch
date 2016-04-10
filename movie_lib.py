import csv
import os


                                #CLASSES
#------------------------------------------------------------------------------#

class Movie():
    def __init__(self, movie_id, title):
        self.id = movie_id
        self.title = title


    def __str__(self):
        return str(self.id + " : " + self.title)

    def __repr__(self):
        return str(self)



class User():
    def __init__(self, user_id, occupation):
        self.user_id = user_id
        self.occupation = occupation

    def __str__(self):
        return str(self.user_id + " : " + self.occupation)

    def __repr__(self):
        return str(self)



class Rating():
    def __init__(self, user, item, rating):
        self.user = user
        self.item = int(item)
        self.rating = int(rating)

    def __str__(self):
        return str("User: {}, Item: {}, Rating: {}".format(self.user, self.item, self.rating))

    def __repr__(self):
        return self.__str__()


                              #FUNCTIONS
#------------------------------------------------------------------------------#

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def import_user_ratings():

    ratings_list = []

    with open('user_ratings.csv') as f:
        reader = csv.reader(f, delimiter='\t')
        headers = next(reader)
        # print(headers)
        # print('------')
        for row in reader:

            ratings_list.append(Rating(row[0], row[1], row[2]))

        # Turns list into list within master_rating
        # i = 0
        # naked_list = []
        # while i<len(master_rating_list):
        #     naked_list.append(master_rating_list[i:i+1])
        #     i += 1

        # master_rating_list = naked_list

        return ratings_list


def import_movie_data():
    with open('movie_data.csv', 'r', encoding='latin_1') as f:
        reader = csv.reader(f, delimiter='|')
        headers = next(reader)
        # print(headers)
        # print('------')
        return reader


def import_user_info():

    user_info_list = []

    with open('user_info.csv') as f:
        reader = csv.reader(f, delimiter='|')
        headers = next(reader)
        # print(headers)
        # print('------')
        # for row in reader:
        #     print(row)
        # for row in reader:
        #     movie_list.append(Movie(row))

        for row in reader:
            user_info_list.append(User(row[0], row[3]))

        return user_info_list



def create_dict_of_user_id_and_occupation():

    user_info_list = {}

    with open('user_info.csv', encoding = 'latin1') as f:
        reader = csv.DictReader(f, delimiter='|', fieldnames=['user_id', 'Age', 'Sex', 'occupation', "ZipCode"])
        headers = next(reader)

        for row in reader:
            user = User(row['user_id'], row['occupation'])
            user_info_list[int(user.user_id)] = user.occupation


        return user_info_list



def create_dict_of_movie_title_and_id():

    movies = {}

    with open('movie_data.csv', encoding='latin_1') as item_file:
    	reader = csv.DictReader(item_file, delimiter='|', fieldnames=['movie_id', 'title'])
    	for row in reader:
    		movie = Movie(row['movie_id'], row['title'])
    		movies[int(movie.id)] = movie.title

    #Turn dict into list
    # movies = [movies[key] for key in movies]

    return(movies)


def user_inputs_movie_id():

    user_input = int(input("\nGimme a movie ID (1-1682) please: "))

    return user_input



def get_ratings_from_users_movie_choice(user_input):

    user_movie = user_input
    list_of_ratings_for_movie = []
    movie_average = []

    for thing in ratings_list:
        if thing.item == user_input:
            list_of_ratings_for_movie.append(thing)

    # print(list_of_ratings_for_movie)

    for movie in list_of_ratings_for_movie:
        movie_average.append(movie.rating)


    sum_of_scores = sum(movie_average)
    length_of_scores = len(movie_average)
    average_of_score = sum_of_scores / length_of_scores
    average = float(average_of_score)
    average = format(average, ".2f")


    print("\nBased off {} reviews, the average score of ".format(length_of_scores) + movies[user_movie] + " is {}!\n".format(average))

    return average




def user_selects_from_main_screen_options():

    print("""Please choose from the follow options: \n
(1) Find a film's average rating by movie ID.
(2) Find a film's average rating by movie title.
(3) Browse the Top 25 films!
(4) Browse the Top 25 films you haven't seen!
(5) Browse the Top 10 films according to your occupational peers!
(6) Exit this cinematic wasteland!
""")

    user_input = input("What would you like to do? ")
    validity_check = check_validity_of_user_selection(user_input)

    if not validity_check:
        print("\nNice try space cadet - please make a valid selection!\n")
        return user_selects_from_main_screen_options()

    return int(user_input)



def check_validity_of_user_selection(user_input):

    return user_input.isnumeric() and int(user_input) in range (1,7)



def initiate_user_selection(user_mode_choice):

    if user_mode_choice == 1:
        return film_average_by_movie_id()

    if user_mode_choice == 6:
        return user_mode_choice


def film_average_by_movie_id():
    movie_id = user_inputs_movie_id()
    average = get_ratings_from_users_movie_choice(movie_id)




def game_over():

    print("\nThanks for visiting! Don't forget to check out our kiosk at your local Blockbuster!\n")
    return True






                              #MAIN
#------------------------------------------------------------------------------#


genre_dict = {

    0: 'unknown',
    1: 'Action',
    2: 'Adventure',
    3: 'Animation',
    4: "Children's",
    5: 'Comedy',
    6: 'Crime',
    7: 'Documentary',
    8: 'Drama',
    9: 'Fantasy',
    10: 'Film-Noir',
    11: 'Horror',
    12: 'Musical',
    13: 'Mystery',
    14: 'Romance',
    15: 'Sci-Fi',
    16: 'Thriller',
    17: 'War',
    18: 'Western'
}


ratings_list = import_user_ratings()
movies = create_dict_of_movie_title_and_id()
user_info_list = import_user_info()

clear()

print("\nWelcome to The Cinematic Emporium!\n")

while True:


    user_mode_choice = user_selects_from_main_screen_options()


    clear()
    initiate_user_selection(user_mode_choice)



    if user_mode_choice == 6:
        break


    # list_of_ratings_for__users_movie = get_ratings_from_users_movie_choice(user_input)


    # user_info_list = import_user_info()
    #
    # print(user_info_list[4])
    #
    # user_job_list = create_dict_of_user_id_and_occupation()
    #
    # print(user_job_list)


game_over()















# print(list_of_ratings_for__users_movie)


# print(list_of_ratings_for__users_movie)










#Creating dictionary of movie.id and movie.title
# movies_dict = create_dict_of_movie_title_and_id()
# print(movies_dict[50])




#
#
# FIND ALL RATINGS FOR MOVIE BY ID
#
# user item rating
# 196	  242	 3


# random_dict = create_dict_of_movie_title_and_id()
#
# print(random_dict)



# ratings_list = import_user_ratings()
#
# print(ratings_list)
















# master_movie_list = import_movie_data()

# print(master_rating_list[0])
# print(master_rating_list[0].rating)

#
# user_id_list = []
#
# for mini_list in master_rating_list:
#
#     for user_list in mini_list:
#
#         user_id_list.append(user_list[0])
#
# print(user_id_list)




# def create_rating_data(master_rating_list):
#
#     user_rating_list = []
#
#     user_rating_list = master_rating_list.append[0]

#
# i = 0
# naked_list = []
# while i<len(master_rating_list):
#     naked_list.append(master_rating_list[i:i+1])
#     i += 1


#
#     for row in reader:
#         movie_list.append(Movie(row))
#
#
# for movie in movie_list:
#     movie_dict[movie.id] = movie.title
#
#
# print(movie_dict)


#dict practice

    # for row in reader:
    #     print(row['movie_id'], row['title']



    # for movie in movie_list:
    #     print(movie.id)

    # movie_list = dict(movie_list)
    #
    # movie_dict = {key: value for (key, value) in movie_list}
    # for item in movie_list:
    #     movie_dict = for key in movie_list
#
# movie_dict = { movie_list for (k,v) in zip(keys, values)}


# movie_dict = {}
# ​
# with open('movie_data.csv') as f:
# 	reader = csv.DictReader(f, delimiter='|')
# 	for row in reader:
# 		row = {key: row[key] for key in row if key in headers}
# ​
# 		test = EODData(row)
#
# 		a_list.append(test)



# Find all ratings for a movie by id
# Find the average rating for a movie by id
# Find the name of a movie by id
# Find all ratings for a user


# The number of users, items, and ratings in the u data set.
#
# 943 users
# 1682 items
# 100000 ratings
