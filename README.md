# Project-2: Recommender Systems

## Our Kaggle Implementation


## Introduction

Recommender Systems are software tools and techniques providing suggestions for items to be consumed by a user. The suggestions provided are aimed at supporting their users in various decision-making processes, such as what items to buy, what movie to watch, or what news to read. Recommender systems have proven to be valuable means for online users to cope with the information overload and have become one of the most powerful and popular tools in electronic commerce. Correspondingly, various techniques for recommendation generation have been proposed and during the last decade(s), many of them have also been successfully deployed in commercial environments.
### Task : Movie Rating Prediction 

Develop a recommender system that is able to predict the rating of a user for a given movie. The metadata of the movies can be used as wished and are allowed to use external movie metadata sources.

Full details of the project can be found in the [Report](./Report.pdf).

## Dataset

The MovieLens dataset is a widely used benchmark dataset in RS. This dataset describes 5-star rating and free-text tagging activity. It contains 100,836 ratings randomly split into a training set (80% of the ratings) and a test set (20% of the ratings). Additionally, the dataset contains 3,683 tag applications across 9,742 movies. These data were created by 610 users between March 29, 1996 and September 24, 2018. Users were selected at random for inclusion. All selected users had rated at least 20 movies.
The metadata of all the movies found in the training and test sets is also provided in the files tags.csv, movies.csv and links.csv.
In the dataset folder you will find the following files:

Train Ratings Data File Structure (train_ratings.csv)
All train ratings are contained in the file train_ratings.csv. Each line of this file after the header row represents one rating of one movie by one user, and has the following format:
userId,movieId,rating,timestamp
ratings are made on a 5-star scale, with half-star increments (0.5 stars - 5.0 stars).
timestamps represent seconds since midnight Coordinated Universal Time (UTC) of January 1, 1970.


Test Data File Structure (test_set_no_ratings.csv)
All test pairs (userId, movieId) are contained in the file test_set_no_ratings.csv. An additional index Id maps each test pair to a single Id.


Tags Data File Structure (tags.csv)
All tags are contained in the file tags.csv. Each line of this file after the header row represents one tag applied to one movie by one user, and has the following format:
userId,movieId,tag,timestamp
tags are user-generated metadata about movies. Each tag is typically a single word or short phrase. The meaning, value, and purpose of a particular tag is determined by each user.


Movie Data File Structure (movies.csv)
Movie information is contained in the file movies.csv. Each line of this file after the header row represents one movie, and has the following format:
movieId,title,genres
Movie titles are entered manually or imported from <https://www.themoviedb.org/>, and include the year of release in parentheses. Errors and inconsistencies may exist in these titles.

genres are a pipe-separated list, and are selected from the following: 
Action, Adventure, Animation, Children's Comedy, Crime, Documentary, Drama, Fantasy, Film-Noir, Horror, Musical, Mystery, Romance, Sci-Fi, Thriller, War, Western, (no genres listed).


Links Data File Structure (links.csv)
Identifiers that can be used to link to other sources of movie data are contained in the file links.csv. Each line of this file after the header row represents one movie, and has the following format:
movieId,imdbId,tmdbId
movieId is an identifier for movies used by <https://movielens.org>. E.g., the movie Toy Story has the link <https://movielens.org/movies/1>.

imdbId is an identifier for movies used by <http://www.imdb.com>. E.g., the movie Toy Story has the link <http://www.imdb.com/title/tt0114709/>.

tmdbId is an identifier for movies used by <https://www.themoviedb.org>. E.g., the movie Toy Story has the link <https://www.themoviedb.org/movie/862>.
## Project Evaluation

The project was evaluated based on the following criteria:

### Results - Metrics

The Root Mean Squared Error (RMSE) is a standard metric to evaluate rating prediction.

## Constraints of project
- It is prohibited to use existing implementations of recommender systems (addressing rating prediction or next-item prediction tasks), even if found in mentioned ressources, except for the purpose of comparing your own models.
- libraries allowed are : standard data manipulation and analysis libraries and machine learning / deep learning frameworks, Numpy, Scipy, Scikit-learn, Pandas, Keras, Gensim, NLTK, or PyTorch that are not implementations of recommender systems (addressing rating prediction or next-item prediction tasks).

