from collections import deque

class Person:
    def __init__(self, full_name):
        self.full_name = full_name
        self.watched_movies = None
        #self.Watched_movies = deque() # add elements using .happend()

    def __str__(self):
        return f"{self.full_name} "