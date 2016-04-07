import csv


    #IMPORT USER RATINGS
# with open('core_data.csv') as f:
#     reader = csv.reader(f, delimiter='\t')
#     headers = next(reader)
#     print(headers)
#     print('------')
#     for row in reader:
#         print(row)


    #IMPORT MOVIE INFO
# with open('movie_data.csv', 'r', encoding='latin_1') as f:
#     reader = csv.reader(f, delimiter='|')
#     headers = next(reader)
#     # print(headers)
#     # print('------')
#     for row in reader:
#         print(row)


    #IMPORT USER INFO
with open('user_info.csv') as f:
    reader = csv.reader(f, delimiter='|')
    headers = next(reader)
    print(headers)
    print('------')
    for row in reader:
        print(row)


# with open('movie_data.csv', encoding='latin_1') as f:
#
#     reader = csv.DictReader(f, fieldnames=['movie_id', 'movie_title', '', '', 'something_else'], delimiter='|')
#     for row in reader:
#         print (row)
#
#     with open('movie_data.csv', 'r', encoding='latin_1') as f:
#         reader = csv.reader(f, delimiter= '|')
#         headers = next(reader)
#         print(headers)
#         print('------')
#         for row in reader:
#             print(row)

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


# The number of users, items, and ratings in the u data set.
#
# 943 users
# 1682 items
# 100000 ratings
