import tkinter as tk
import font_manager as fonts
from check_videos import CheckVideos
from create_video_list import CreateVideoList
from update_videos import UpdateVideos

# Function that handles the "Check Videos" button click event
def check_videos_clicked():
    # Update the status label to indicate the button was clicked
    status_lbl.configure(text="Check Videos button was clicked!")
    # Open a new Toplevel window for the CheckVideos functionality
    CheckVideos(tk.Toplevel(window))

# Function that handles the "Create Video List" button click event
def create_video_list_clicked():
    # Update the status label to indicate the button was clicked
    status_lbl.configure(text="Create Video List button was clicked!")
    # Open a new Toplevel window for the CreateVideoList functionality
    CreateVideoList(tk.Toplevel(window))

# Function that handles the "Update Videos" button click event
def update_videos_clicked():
    # Update the status label to indicate the button was clicked
    status_lbl.configure(text="Update Videos button was clicked!")
    # Open a new Toplevel window for the UpdateVideos functionality
    UpdateVideos(tk.Toplevel(window))

# Initialize the main application window
window = tk.Tk()
# Set the size of the window
window.geometry("520x150")
# Set the title of the window
window.title("Video Player")

# Configure fonts using the font_manager module
fonts.configure()

# Set Facebook-like colors for the application
bg_color = "#4267B2"         # Facebook blue
fg_color = "#c0c0c0"         # White text
button_color = "#4267B2"     # Facebook blue
button_hover_color = "#3b5998"  # Darker blue

# Configure the background color of the window
window.configure(bg=bg_color)

# Create a header label with instructional text
header_lbl = tk.Label(window, text="Select an option by clicking one of the buttons below", 
                      bg=bg_color, fg=fg_color, font=("Helvetica", 12))
header_lbl.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# Create the "Check Videos" button
check_videos_btn = tk.Button(window, text="Check Videos", command=check_videos_clicked,
                             bg=button_color, fg=fg_color, font=("Helvetica", 11, "bold"),
                             relief="flat", height=2, width=16, borderwidth=0)
check_videos_btn.grid(row=1, column=0, padx=10, pady=10)
check_videos_btn.bind("<Enter>", lambda e: check_videos_btn.configure(bg=button_hover_color))
check_videos_btn.bind("<Leave>", lambda e: check_videos_btn.configure(bg=button_color))

# Create the "Create Video List" button
create_video_list_btn = tk.Button(window, text="Create Video List", command=create_video_list_clicked,
                                  bg=button_color, fg=fg_color, font=("Helvetica", 11, "bold"),
                                  relief="flat", height=2, width=16, borderwidth=0)
create_video_list_btn.grid(row=1, column=1, padx=10, pady=10)
create_video_list_btn.bind("<Enter>", lambda e: create_video_list_btn.configure(bg=button_hover_color))
create_video_list_btn.bind("<Leave>", lambda e: create_video_list_btn.configure(bg=button_color))

# Create the "Update Videos" button
update_videos_btn = tk.Button(window, text="Update Videos", command=update_videos_clicked,
                              bg=button_color, fg=fg_color, font=("Helvetica", 11, "bold"),
                              relief="flat", height=2, width=16, borderwidth=0)
update_videos_btn.grid(row=1, column=2, padx=10, pady=10)
update_videos_btn.bind("<Enter>", lambda e: update_videos_btn.configure(bg=button_hover_color))
update_videos_btn.bind("<Leave>", lambda e: update_videos_btn.configure(bg=button_color))

# Create a status label to display messages
status_lbl = tk.Label(window, text="", bg=bg_color, fg=fg_color, font=("Helvetica", 10))
status_lbl.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

# Start the Tkinter main loop to keep the application running
window.mainloop()
