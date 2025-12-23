import pandas as pd

movies = pd.read_csv('movies.csv')
credit = pd.read_csv('credits.csv')
rating = pd.read_csv('ratings.csv')

#
# Calculate a weighted rating

# WR = (v/(v+m))R+(m/(v+m)) C
#
# v- number of votes for a movie
#
# m- minimum number of votes required
#
# R- average rating of the movie
#
# C- average rating across all movis

