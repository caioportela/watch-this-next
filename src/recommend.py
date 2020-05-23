import pandas as pd

ratings_data = pd.read_csv('ratings.csv')
movies_data = pd.read_csv('movies.csv')

movies_data = pd.merge(ratings_data, movies_data, on='movieId')

ratings_mean = movies_data.groupby('title')['rating'].mean()  # Find the average rating of each movie
ratings_count = movies_data.groupby('title')['rating'].count()  # Find the total number of ratings for a movie

ratings_mean_count = pd.DataFrame(ratings_mean)
ratings_mean_count['count'] = pd.DataFrame(ratings_count)

user_ratings = movies_data.pivot_table(index='userId', columns='title', values='rating')  # Create matrix of movie titles and user ratings

forrest_gump_ratings = user_ratings['Forrest Gump (1994)']  # Find ratings for Forrest Gump (1994)

like_forrest_gump = user_ratings.corrwith(forrest_gump_ratings)  # Find all correlated movies

corr_forrest_gump = pd.DataFrame(like_forrest_gump, columns=['Correlation'])
corr_forrest_gump.dropna(inplace=True)
corr_forrest_gump = corr_forrest_gump.sort_values('Correlation', ascending=False)

corr_forrest_gump = corr_forrest_gump.join(ratings_mean_count['count'])  # Add number of ratings
corr_forrest_gump = corr_forrest_gump[corr_forrest_gump['count'] >= 50]  # Filter movies that have more than 50 ratings

top_movies = corr_forrest_gump.head(10)
print(top_movies)
