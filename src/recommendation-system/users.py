from collections import deque

class Person:
    def __init__(self, full_name = 'user X'):
        self.full_name = full_name
        self.watched_movies = None
        self.user_profile = None
        #self.Watched_movies = deque() # add elements using .happend()

    def calculate_user_profile(self):
        self.watched_movies.iloc[:,1 :-1] = self.watched_movies.iloc[:,1 :-1].multiply(self.watched_movies.iloc[:, -1], axis=0)
        self.user_profile = self.watched_movies.iloc[:, 1:-1].sum().to_frame().T

    def __str__(self):
        return f"{self.full_name} "