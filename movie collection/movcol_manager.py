"""
Midterm Practical Exam — Movie Collection Manager
Student: Precious Pauline M. Peralta
"""

movies = []

def display_menu():
    print("\n=== Movie Collection Manager ===")
    print("1. Add a movie")
    print("2. View all movies")
    print("3. Count watched vs unwatched")
    print("4. Find a movie")
    print("5. Exit")
    return
    pass

def add_movie(movie_list):
    print("\n=== ADD MOVIE ===")
    title = input("Enter movie title: ")
    director = input("Enter director: ")
    status = input("Enter status (Watched/Unwatched): ")
    pass