"""
Name:M.Madhusudhanan
Reg no:3122225002067
"""


class Movie:
    def __init__(self, title, director, year, genre, *args, **kwargs):
        self.title = title
        self.director = director
        self.year = year
        self.genre = genre
        self.additional_args = args
        self.additional_kwargs = kwargs

    def display_info(self):
        print(f"Title: {self.title}, Director: {self.director}, Year: {self.year}, Genre: {self.genre}")
        if self.additional_args:
            print(f"Additional Args: {self.additional_args}")
        if self.additional_kwargs:
            print(f"Additional Kwargs: {self.additional_kwargs}")

class Movielist(Movie):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.actor = ""
        self.actress = ""
        self.budget = ""

    def add_info(self):
        self.actor = input("Enter the actor of the movie: ")
        self.actress = input("Enter the actress of the movie: ")
        self.budget = input("Enter the budget of the movie: ")

    def display_info(self):
        super().display_info()
        print("Additional Information: ")
        print(f"Actor: {self.actor}, Actress: {self.actress}, Budget: {self.budget}")

# Create instances and use the classes
movie1 = Movielist("Leo", "Loki", 2023, "Action")
movie1.add_info()
movie1.display_info()

movie2 = Movielist("Jailer", "Nelson", 2022, "Adventure", "Worstfilm", additional_info="Don't watch this movie this a shitt")
movie2.add_info()
movie2.display_info()
