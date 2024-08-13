import tkinter as tk
import tkinter.scrolledtext as tkst
import pygame
import video_library as lib
import font_manager as fonts

def set_text(text_area, content):
    """
    Utility function to set the content of a text area.
    
    Parameters:
    - text_area (tk.Text): The Tkinter Text widget where the content will be set.
    - content (str): The content to display in the text area.
    """
    text_area.delete("1.0", tk.END)  # Clear the text area
    text_area.insert("1.0", content)  # Insert the new content at the beginning

class CreateVideoList:
    def __init__(self, window):
        """
        Initialize the CreateVideoList class with the main Tkinter window.
        
        Parameters:
        - window (tk.Tk): The main Tkinter window object.
        """
        self.window = window  # Store the window object
        self.sound_player = pygame.mixer  # Initialize the pygame mixer for playing sounds
        self.sound_player.init()  # Initialize the mixer
        window.geometry("750x350")  # Set the size of the window
        window.title("Create Video List")  # Set the window title

        # Set Facebook-like colors
        self.bg_color = "#4267B2"  # Background color (Facebook blue)
        self.fg_color = "#1C1E21"  # Text color (Dark text)
        self.button_color = "#1877F2"  # Button color (Facebook blue)
        self.button_hover_color = "#365899"  # Button hover color (Darker blue)
        self.button_text_color = "#FFFFFF"  # Button text color (White)

        # Configure the main window with the background color
        window.configure(bg=self.bg_color)

        # Initialize playlist and total play count
        self.playlist = []  # List to store video numbers in the playlist
        self.total_plays = 0  # Total number of plays (not currently used)

        # Create and place widgets in the window
        self.create_widgets()

    def create_widgets(self):
        """
        Create and place all the widgets in the main window.
        """
        # Label for entering video number
        enter_lbl = tk.Label(self.window, text="Enter Video Number", bg=self.bg_color, fg=self.fg_color,
                             font=("Helvetica", 11))
        enter_lbl.grid(row=0, column=0, padx=10, pady=10)  # Place label at grid position (0, 0)

        # Entry widget for video number input
        self.input_txt = tk.Entry(self.window, width=5, font=("Helvetica", 11), bg="#F0F0F0", fg=self.fg_color, borderwidth=0)
        self.input_txt.grid(row=0, column=1, padx=10, pady=10)  # Place entry widget at grid position (0, 1)

        # Button to add video to playlist
        add_btn = tk.Button(self.window, text="Add to Playlist", command=self.add_to_playlist,
                            bg=self.button_color, fg=self.button_text_color, font=("Helvetica", 11, "bold"),
                            relief="flat", height=2, width=18, borderwidth=0)
        add_btn.grid(row=0, column=2, padx=10, pady=10)  # Place button at grid position (0, 2)
        add_btn.bind("<Enter>", lambda e: self.on_button_hover(add_btn))  # Change color on hover
        add_btn.bind("<Leave>", lambda e: self.on_button_leave(add_btn))  # Revert color when leaving

        # Button to play selected video from playlist
        play_selected_btn = tk.Button(self.window, text="Play Selected", command=self.play_selected,
                                      bg=self.button_color, fg=self.button_text_color, font=("Helvetica", 11, "bold"),
                                      relief="flat", height=2, width=18, borderwidth=0)
        play_selected_btn.grid(row=1, column=0, padx=10, pady=10)  # Place button at grid position (1, 0)
        play_selected_btn.bind("<Enter>", lambda e: self.on_button_hover(play_selected_btn))
        play_selected_btn.bind("<Leave>", lambda e: self.on_button_leave(play_selected_btn))

        # Button to stop the currently playing song
        self.stop_button = tk.Button(self.window, text="Stop Song", command=self.stop_sound,
                                     bg=self.button_color, fg=self.button_text_color, font=("Helvetica", 11, "bold"),
                                     relief="flat", height=2, width=18, borderwidth=0)
        self.stop_button.grid(row=1, column=1, padx=10, pady=10)  # Place button at grid position (1, 1)
        self.stop_button.bind("<Enter>", lambda e: self.on_button_hover(self.stop_button))
        self.stop_button.bind("<Leave>", lambda e: self.on_button_leave(self.stop_button))

        # Button to reset the playlist
        reset_btn = tk.Button(self.window, text="Reset Playlist", command=self.reset_playlist,
                              bg=self.button_color, fg=self.button_text_color, font=("Helvetica", 11, "bold"),
                              relief="flat", height=2, width=18, borderwidth=0)
        reset_btn.grid(row=1, column=2, padx=10, pady=10)  # Place button at grid position (1, 2)
        reset_btn.bind("<Enter>", lambda e: self.on_button_hover(reset_btn))
        reset_btn.bind("<Leave>", lambda e: self.on_button_leave(reset_btn))

        # Button to reset play counts of videos in the playlist
        reset_plays_btn = tk.Button(self.window, text="Reset Plays", command=self.reset_plays,
                                    bg=self.button_color, fg=self.button_text_color, font=("Helvetica", 11, "bold"),
                                    relief="flat", height=2, width=18, borderwidth=0)
        reset_plays_btn.grid(row=2, column=0, padx=10, pady=10)  # Place button at grid position (2, 0)
        reset_plays_btn.bind("<Enter>", lambda e: self.on_button_hover(reset_plays_btn))
        reset_plays_btn.bind("<Leave>", lambda e: self.on_button_leave(reset_plays_btn))

        # ScrolledText widget to display the playlist
        self.playlist_txt = tkst.ScrolledText(self.window, width=50, height=12, wrap="none",
                                              bg="#F0F0F0", fg=self.fg_color, font=("Helvetica", 11), borderwidth=0)
        self.playlist_txt.grid(row=2, column=1, columnspan=2, sticky="W", padx=10, pady=10)  # Place scrolled text widget

        # Label to display status messages
        self.status_lbl = tk.Label(self.window, text="", bg=self.bg_color, fg=self.fg_color, font=("Helvetica", 11))
        self.status_lbl.grid(row=3, column=0, columnspan=3, sticky="W", padx=10, pady=10)  # Place status label

    def play_selected(self):
        """
        Play the selected video from the playlist.
        """
        try:
            selected_text = self.playlist_txt.get("sel.first", "sel.last").strip()  # Get the selected text
            if not selected_text:
                self.status_lbl.configure(text="No song selected.")  # Display an error if nothing is selected
                return

            song_index = int(selected_text.split(".")[0]) - 1  # Extract the index from the selected text
            if song_index < 0 or song_index >= len(self.playlist):
                self.status_lbl.configure(text="Selected index out of range.")  # Display an error if index is invalid
                return

            video_num = self.playlist[song_index]  # Get the video number from the playlist
            mp3_file = lib.get_mp3_file(video_num)  # Get the correct MP3 file path

            if mp3_file:
                self.sound_player.music.load(mp3_file)  # Load the MP3 file
                self.sound_player.music.play()  # Play the MP3 file
                self.status_lbl.configure(text=f"Playing: {mp3_file}")  # Update the status label

                # Increment the play count for the selected video
                lib.increment_play_count(video_num)

                # Update the playlist display to show the new play count
                playlist_str = "\n".join([f"{i+1}. {lib.get_name(video)} ({lib.get_play_count(video)})" for i, video in enumerate(self.playlist)])
                set_text(self.playlist_txt, playlist_str)  # Update the playlist text area
            else:
                self.status_lbl.configure(text="MP3 file not found.")  # Display an error if the file is not found
        except pygame.error as e:
            self.status_lbl.configure(text=f"Error: {e}")  # Handle pygame errors
        except tk.TclError:
            self.status_lbl.configure(text="No song selected.")  # Handle Tkinter errors
        except ValueError:
            self.status_lbl.configure(text="Invalid selection.")  # Handle invalid selections

    def stop_sound(self):
        """
        Stop the currently playing sound.
        """
        self.sound_player.music.stop()  # Stop the music
        self.status_lbl.configure(text="Song stopped.")  # Update the status label

    def add_to_playlist(self):
        """
        Add a video to the playlist based on the video number entered by the user.
        """
        video_num = self.input_txt.get().strip()  # Get the video number from the input
        if not video_num:
            self.status_lbl.configure(text="Please enter a video number.")  # Display an error if input is empty
            return

        name = lib.get_name(video_num)  # Get the name of the video
        if name is not None:
            # Check if the video is already in the playlist
            if video_num not in self.playlist:
                self.playlist.append(video_num)  # Add the video number to the playlist
                playlist_str = "\n".join([f"{i+1}. {lib.get_name(video)}" for i, video in enumerate(self.playlist)])
                set_text(self.playlist_txt, playlist_str)  # Update the playlist text area
                self.status_lbl.configure(text=f"Added {name} to the playlist.")  # Update the status label
            else:
                self.status_lbl.configure(text=f"{name} is already in the playlist.")  # Display a message if already in the playlist
        else:
            self.status_lbl.configure(text=f"Video {video_num} not found.")  # Display an error if the video is not found

    def reset_playlist(self):
        """
        Reset the playlist by clearing all videos from it.
        """
        self.playlist = []  # Clear the playlist
        self.total_plays = 0  # Reset the total play count
        set_text(self.playlist_txt, "")  # Clear the playlist text area
        self.status_lbl.configure(text="Playlist has been reset.")  # Update the status label

    def reset_plays(self):
        """
        Reset the play counts of all videos in the playlist.
        """
        for video_num in self.playlist:
            lib.reset_play_count(video_num)  # Reset the play count for each video in the playlist
        playlist_str = "\n".join([f"{i+1}. {lib.get_name(video)} ({lib.get_play_count(video)})" for i, video in enumerate(self.playlist)])
        set_text(self.playlist_txt, playlist_str)  # Update the playlist text area
        self.status_lbl.configure(text="Play counts have been reset.")  # Update the status label

    def on_button_hover(self, button):
        """
        Change the button's background color when hovered over.
        
        Parameters:
        - button (tk.Button): The button that is being hovered over.
        """
        button.configure(bg=self.button_hover_color)

    def on_button_leave(self, button):
        """
        Revert the button's background color when the mouse leaves.
        
        Parameters:
        - button (tk.Button): The button that the mouse has left.
        """
        button.configure(bg=self.button_color)

if __name__ == "__main__":
    window = tk.Tk()  # Create the main Tkinter window
    fonts.configure()  # Configure fonts using the font_manager module
    CreateVideoList(window)  # Instantiate the CreateVideoList class
    window.mainloop()  # Start the Tkinter event loop
