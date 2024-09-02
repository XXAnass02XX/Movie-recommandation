import pandas as pd
from users import Person
from sklearn.preprocessing import MinMaxScaler

df_dataSet = pd.read_csv('../../dataset/processed_data_set.csv')
columns = df_dataSet.columns
#todo : save the columns

User1 = Person()
User1.watched_movies = pd.DataFrame(columns=columns)
User1.watched_movies['rating'] = 0

#adding the user movies

row_to_add = df_dataSet.loc[df_dataSet['title'] == 'Inception']
User1.watched_movies = pd.concat([User1.watched_movies,row_to_add], ignore_index=True)
User1.watched_movies.loc[User1.watched_movies['title'] == 'Inception', 'rating'] = 10
row_to_add = df_dataSet.loc[df_dataSet['title'] == 'The Shawshank Redemption']
User1.watched_movies = pd.concat([User1.watched_movies,row_to_add], ignore_index=True)
User1.watched_movies.loc[User1.watched_movies['title'] == 'The Shawshank Redemption', 'rating'] = 7
row_to_add = df_dataSet.loc[df_dataSet['title'] == 'Avatar']
User1.watched_movies = pd.concat([User1.watched_movies,row_to_add], ignore_index=True)
User1.watched_movies.loc[User1.watched_movies['title'] == 'Avatar', 'rating'] = 1

User1.calculate_user_profile()

#TODO normalize the values

scaler = MinMaxScaler()

User1.user_profile.iloc[0, :] = scaler.fit_transform(User1.user_profile.iloc[[0], :].T).T

def movies_score(user):
    user_profile = user.user_profile
    movie_features = df_dataSet.iloc[:, 1:]
    # Calculate the dot product
    scores = df_dataSet.iloc[:, 1:].dot(user_profile.iloc[0])
    # Create the result DataFrame
    result_df = pd.DataFrame({
        'Movie': df_dataSet['title'],
        'Score': scores
    })
    result_df.sort_values(by='Score', ascending=False)

    return result_df

movies_rating_prediction = movies_score(User1)
movies_rating_prediction = movies_rating_prediction[~movies_rating_prediction['Movie'].isin(User1.watched_movies['title'])]

print(movies_rating_prediction.head())