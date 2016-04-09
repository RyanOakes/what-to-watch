
import csv



                                #CLASSES
#------------------------------------------------------------------------------#

class Movie():
    def __init__(self, row):
        self.id = int(row[0])
        self.title = row[1]


    def __str__(self):
        return str(self.id + " " + self.title)
                            #+ " , " + self.open


class User():
    pass


class Rating():
    def __init__(self, user, item, rating):
        self.user = user
        self.item = item
        self.rating = rating

    def __str__(self):
        return str(self.user + ", " + self.item + ", " + self.rating)

    def __repr__(self):
        return self.__str__()


                              #FUNCTIONS
#------------------------------------------------------------------------------#


def import_core_data():
    master_rating_list = []

    with open('core_data.csv') as f:
        reader = csv.reader(f, delimiter='\t')
        headers = next(reader)
        # print(headers)
        # print('------')
        for row in reader:

            master_rating_list.append(Rating(row[0], row[1], row[2]))

        # i = 0
        # naked_list = []
        # while i<len(master_rating_list):
        #     naked_list.append(master_rating_list[i:i+1])
        #     i += 1
        #
        # master_rating_list = naked_list

        return master_rating_list

def import_movie_data():
    with open('movie_data.csv', 'r', encoding='latin_1') as f:
        reader = csv.reader(f, delimiter='|')
        headers = next(reader)
        # print(headers)
        # print('------')
        return


def import_user_info():
    with open('user_info.csv') as f:
        reader = csv.reader(f, delimiter='|')
        headers = next(reader)
        # print(headers)
        # print('------')
        # for row in reader:
        #     print(row)
        # for row in reader:
        #     movie_list.append(Movie(row))




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




# def create_rating_data(master_rating_list):
#
#     user_rating_list = []
#
#     user_rating_list = master_rating_list.append[0]
#
master_rating_list = import_core_data()

print(master_rating_list[0].rating)

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
