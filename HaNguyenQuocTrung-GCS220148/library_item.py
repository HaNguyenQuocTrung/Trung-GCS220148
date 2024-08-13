class LibraryItem:
    def __init__(self, name, director, rating, type, tempo, mp3_file):
        """
        Initialize a new LibraryItem object.

        Parameters:
        - name (str): The name of the video or audio item.
        - director (str): The name of the director or creator of the item.
        - rating (int): The rating of the item, typically out of 5.
        - type (str): The genre or category of the item (e.g., 'Pop', 'Blues').
        - tempo (str): The tempo or mood of the item (e.g., 'Upbeat', 'Calm').
        - mp3_file (str): The filename of the associated audio file (e.g., 'song.mp3').

        The play count is initialized to 0.
        """
        self.name = name  # Name of the item
        self.director = director  # Director or creator of the item
        self.rating = rating  # Rating of the item
        self.type = type  # Genre or type of the item
        self.tempo = tempo  # Tempo or mood of the item
        self.mp3_file = mp3_file  # Filename of the associated MP3 file
        self.play_count = 0  # Initialize play count to 0

    def info(self):
        """
        Returns a string containing detailed information about the item.

        Format: "name by director (type, tempo) - rating"

        Example:
        For an item with name="Joyful", director="Neura-Flow", type="Pop", tempo="Optimistic", and rating=5,
        the method would return "Joyful by Neura-Flow (Pop, Optimistic) - 5".
        """
        return f"{self.name} by {self.director} ({self.type}, {self.tempo}) - {self.rating}"

    def play(self):
        """
        Increment the play count by 1 each time the item is played.
        """
        self.play_count += 1  # Increment play count when the item is played

    def reset_play_count(self):
        """
        Resets the play count to 0. Useful for resetting statistics.
        """
        self.play_count = 0  # Reset play count to 0

    def stars(self):
        """
        Generates a string of stars (*) representing the item's rating.

        Returns:
        - stars (str): A string with a number of stars equal to the rating.
        
        Example:
        For a rating of 3, the method returns "***".
        """
        stars = ""  # Initialize an empty string for stars
        for i in range(self.rating):  # Loop through the range of the rating
            stars += "*"  # Append a star for each point in the rating
        return stars  # Return the star string
