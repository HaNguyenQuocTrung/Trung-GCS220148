import tkinter as tk
import tkinter.scrolledtext as tkst
import video_library as lib
import font_manager as fonts

def set_text(text_area, content):
    text_area.configure(state='normal')  # Set the state to normal to enable editing
    text_area.delete("1.0", tk.END)
    text_area.insert("1.0", content)
    text_area.configure(state='disabled')  # Set the state to disabled to disable editing

class CheckVideos:
    def __init__(self, window):
        # Set modern colors similar to Facebook's color scheme
        self.bg_color = "#4267B2"  # Light background color
        self.fg_color = "#1C1E21"  # Dark text color
        self.button_color = "#1877F2"  # Facebook blue
        self.button_hover_color = "#365899"  # Darker blue for hover

        window.geometry("750x350")
        window.title("Check Videos")
        window.configure(bg=self.bg_color)

        # List All Videos Button
        list_videos_btn = tk.Button(window, text="List All Videos", command=self.list_videos_clicked,
                                    bg=self.button_color, fg="#FFFFFF", font=("Helvetica", 11, "bold"),
                                    relief="flat", height=2, width=20)
        list_videos_btn.grid(row=0, column=0, padx=10, pady=10)
        list_videos_btn.bind("<Enter>", lambda e: self.on_button_hover(list_videos_btn))
        list_videos_btn.bind("<Leave>", lambda e: self.on_button_leave(list_videos_btn))

        # Enter Video Number Label and Entry
        enter_lbl = tk.Label(window, text="Enter Video Number", bg=self.bg_color, fg=self.fg_color,
                            font=("Helvetica", 11))
        enter_lbl.grid(row=0, column=1, padx=10, pady=10)

        self.input_txt = tk.Entry(window, width=5, font=("Helvetica", 11), bg="#E9EBEE", fg=self.fg_color, borderwidth=0)
        self.input_txt.grid(row=0, column=2, padx=10, pady=10)

        # Check Video Button
        check_video_btn = tk.Button(window, text="Check Video", command=self.check_video_clicked,
                                    bg=self.button_color, fg="#FFFFFF", font=("Helvetica", 11, "bold"),
                                    relief="flat", height=2, width=20)
        check_video_btn.grid(row=0, column=3, padx=10, pady=10)
        check_video_btn.bind("<Enter>", lambda e: self.on_button_hover(check_video_btn))
        check_video_btn.bind("<Leave>", lambda e: self.on_button_leave(check_video_btn))

        # ScrolledText for video list
        self.list_txt = tkst.ScrolledText(window, width=48, height=12, wrap="none", bg="#E9EBEE", fg=self.fg_color,
                                         font=("Helvetica", 11), borderwidth=0)
        self.list_txt.grid(row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10)
        self.list_txt.configure(state='disabled')  # Set the state to disabled to disable editing

        # Text widget for video details
        self.video_txt = tk.Text(window, width=24, height=8, wrap="none", bg="#E9EBEE", fg=self.fg_color,
                                 font=("Helvetica", 11), borderwidth=0)
        self.video_txt.grid(row=1, column=3, sticky="NW", padx=10, pady=10)
        self.video_txt.configure(state='disabled')  # Set the state to disabled to disable editing

        # Status label
        self.status_lbl = tk.Label(window, text="", bg=self.bg_color, fg=self.fg_color, font=("Helvetica", 10))
        self.status_lbl.grid(row=2, column=0, columnspan=4, sticky="W", padx=10, pady=10)

        self.list_videos_clicked()

    def check_video_clicked(self):
        key = self.input_txt.get()
        name = lib.get_name(key)
        if name is not None:
            director = lib.get_director(key)
            rating = lib.get_rating(key)
            play_count = lib.get_play_count(key)
            video_type = lib.get_type(key)
            tempo = lib.get_tempo(key)
            video_details = (f"Name: {name} \nDirector: {director} \nRating: {rating}\nPlays: {play_count}\nType: {video_type}\nTempo: {tempo}")
            set_text(self.video_txt, video_details)
        else:
            set_text(self.video_txt, f"Video {key} not found")
        self.status_lbl.configure(text="Check Video button was clicked!")

    def list_videos_clicked(self):
        video_list = lib.list_all()
        set_text(self.list_txt, video_list)
        self.status_lbl.configure(text="List Videos button was clicked!")

    def on_button_hover(self, button):
        button.configure(bg=self.button_hover_color)

    def on_button_leave(self, button):
        button.configure(bg=self.button_color)

if __name__ == "__main__":
    window = tk.Tk()
    fonts.configure()
    CheckVideos(window)
    window.mainloop()
