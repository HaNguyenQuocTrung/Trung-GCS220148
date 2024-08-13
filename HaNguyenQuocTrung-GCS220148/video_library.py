from library_item import LibraryItem

# Initialize the library with items
# The 'library' is a dictionary where the keys are video numbers (as strings) and the values are LibraryItem objects.
library = {}
library["01"] = LibraryItem("Nightfall", "SoulProdMusic", 5, "Future Bass", "Future", "nightfall.mp3")
library["02"] = LibraryItem("Goodnight", "FASSounds", 4, "Advertisement", "Cold", "goodnight.mp3")
library["03"] = LibraryItem("Sunshine", "lemonmusicstudio", 4, "Classic", "Summer", "sunshine.mp3")
library["04"] = LibraryItem("Powerful", "MarkJuly", 4, "Blues", "Charm", "Powerful.mp3")
library["05"] = LibraryItem("Joyful", "Neura-Flow", 5, "Pop", "Optimistic", "Joyful.mp3")

# Function to list all items in the library
def list_all():
    # Initialize an empty string to store the output
    output = ""
    # Iterate through each key in the library dictionary
    for key in library:
        # Retrieve the LibraryItem associated with the key
        item = library[key]
        # Append the key and the item's information to the output string
        output += f"{key} {item.info()}\n"
    # Return the complete list of items
    return output

# Function to get the name of an item based on its key
def get_name(key):
    try:
        # Retrieve the LibraryItem associated with the key
        item = library[key]
        # Return the name of the item
        return item.name
    except KeyError:
        # Raise an error if the key is not found in the library
        raise KeyError(f"Key '{key}' not found in the library.")

# Function to get the director of an item based on its key
def get_director(key):
    try:
        # Retrieve the LibraryItem associated with the key
        item = library[key]
        # Return the director of the item
        return item.director
    except KeyError:
        # Return None if the key is not found in the library
        return None

# Function to get the type of an item based on its key
def get_type(key):
    try:
        # Retrieve the LibraryItem associated with the key
        item = library[key]
        # Return the type of the item
        return item.type
    except KeyError:
        # Return None if the key is not found in the library
        return None

# Function to get the tempo of an item based on its key
def get_tempo(key):
    try:
        # Retrieve the LibraryItem associated with the key
        item = library[key]
        # Return the tempo of the item
        return item.tempo
    except KeyError:
        # Return None if the key is not found in the library
        return None

# Function to get the rating of an item based on its key
def get_rating(key):
    try:
        # Retrieve the LibraryItem associated with the key
        item = library[key]
        # Return the rating of the item
        return item.rating
    except KeyError:
        # Return -1 if the key is not found in the library
        return -1

# Function to set the rating of an item based on its key
def set_rating(key, rating):
    try:
        # Retrieve the LibraryItem associated with the key
        item = library[key]
        # Update the rating of the item
        item.rating = rating
    except KeyError:
        # Do nothing if the key is not found in the library
        return

# Function to get the play count of an item based on its key
def get_play_count(key):
    try:
        # Retrieve the LibraryItem associated with the key
        item = library[key]
        # Return the play count of the item
        return item.play_count
    except KeyError:
        # Return -1 if the key is not found in the library
        return -1

# Function to increment the play count of an item based on its key
def increment_play_count(key):
    try:
        # Retrieve the LibraryItem associated with the key
        item = library[key]
        # Increment the play count by 1
        item.play_count += 1
    except KeyError:
        # Do nothing if the key is not found in the library
        return

# Function to reset the play count of an item based on its key
def reset_play_count(key):
    try:
        # Retrieve the LibraryItem associated with the key
        item = library[key]
        # Reset the play count to 0
        item.play_count = 0
    except KeyError:
        # Do nothing if the key is not found in the library
        return

# Function to get the MP3 file name of an item based on its key
def get_mp3_file(key):
    try:
        # Retrieve the LibraryItem associated with the key
        item = library[key]
        # Return the MP3 file name of the item
        return item.mp3_file
    except KeyError:
        # Return None if the key is not found in the library
        return None
