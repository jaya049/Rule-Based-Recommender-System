import pandas as pd

movies_df = pd.read_csv(r'C:\Users\jaya0\OneDrive\Documents\Self_Learning\ml32m\movies.csv')  # Replace with your actual file path
print(movies_df.head())
#Ensure movieID is an int
movies_df['movieId'] = movies_df['movieId'].astype(int)
def recommend_movies(genre, num_recommendations=5):
    """
    Recommends movies based on a given genre.

    Args:
        genre (str): The genre to search for.
        num_recommendations (int): The number of movie recommendations to return.

    Returns:
        pandas.DataFrame: A DataFrame containing the recommended movies.  Returns an empty DataFrame if no movies found.
    """

    # Filter movies by genre
    recommended_movies = movies_df[movies_df['genres'].str.contains(genre, case=False, na=False)]

    # Select a random sample of movies.  Important for variety.
    if not recommended_movies.empty:
        recommended_movies = recommended_movies.sample(n=min(num_recommendations, len(recommended_movies))) # Ensure you don't try to sample more than exist
        return recommended_movies[['movieId', 'title', 'genres']]  #Return specific columns
    else:
        print(f"No movies found for the genre: {genre}")
        return pd.DataFrame()  # Return an empty DataFrame if no movies are found.

# Example Usage:
genre_to_recommend = 'Comedy'
recommendations = recommend_movies(genre_to_recommend)

if not recommendations.empty:
    print(f"Recommended movies for genre '{genre_to_recommend}':")
    print(recommendations)
    
genre_input = input("Enter a genre: ")
recommendations = recommend_movies(genre_input)
if not recommendations.empty:
    print(recommendations)