import pandas as pd
from sklearn.preprocessing import MinMaxScaler

class Person:
    def __init__(self, full_name = 'user X'):
        self.full_name = full_name
        self.watched_movies = None
        self.user_profile = None # a dataframe of all movies charactiristics with a score for each one ( so 1 line)

    def calculate_user_profile(self):
        '''we calculate here the user profile : it is a vector that represents how much the user likes each characteristic e.g : language_french , drama ...'''
        self.watched_movies.iloc[:,1 :-1] = self.watched_movies.iloc[:,1 :-1].multiply(self.watched_movies.iloc[:, -1], axis=0)
        self.user_profile = self.watched_movies.iloc[:, 1:-1].sum().to_frame().T
        scaler = MinMaxScaler()
        self.user_profile.iloc[0, :] = scaler.fit_transform(self.user_profile.iloc[[0], :].T).T   

    def add_movie(self, movie_name ,rating ,movies_dataframe):
        new_movie = movies_dataframe.loc[movies_dataframe['title'] == movie_name].copy()
        new_movie['rating'] = rating
        self.watched_movies = pd.concat([self.watched_movies, new_movie], ignore_index=True)

    def delete_movie(self, index):
        if self.watched_movies is not None and not self.watched_movies.empty:
            self.watched_movies = self.watched_movies.drop(index).reset_index(drop=True)
            if self.watched_movies.empty:
                self.watched_movies = None

    def movies_score(self,df_dataSet):
        '''calculate the score of all movies using the user_profile , 
        the score represents how much the user will likely like it ,
        the bigger the sccore the higher the chance
        he will like it'''
        # Calculate the dot product
        scores = df_dataSet.iloc[:, 1:].dot(self.user_profile.iloc[0])
        # Create the result DataFrame
        result_df = pd.DataFrame({
            'Movie': df_dataSet['title'],
            'Score': scores
        })
        result_df.sort_values(by='Score', ascending=False)
        result_df = result_df[~result_df['Movie'].isin(self.watched_movies['title'])]

        return result_df

    def __str__(self):
        return f"{self.full_name}"
