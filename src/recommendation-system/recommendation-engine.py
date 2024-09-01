import pandas as pd
from users import Person

df_dataSet = pd.read_csv('../../dataset/processed_data_set.csv')
columns = df_dataSet.columns

df_userWatchedMovies = pd.DataFrame(columns=columns)

User1 = Person('anass')
User1.watched_movies = df_userWatchedMovies