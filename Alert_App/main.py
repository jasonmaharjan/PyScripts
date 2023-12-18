import customtkinter

class MainFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # add label widget onto the frame:
        # self.label = customtkinter.CTkLabel(self, text="Ohnoo An Alerto is here")
        # self.label.grid(row=0, column=0, padx=20, pady=20)

        # button widget
        self.button = customtkinter.CTkButton(self, text="Eyes off the screen now!!", 
                                              command=self.on_click, font=("Consolas", 60),
                                              fg_color="transparent", text_color="gold"
                                              )
        # self.button.grid(row=1, column=1, padx=200, pady=100)
        self.button.place(relx=0.5, rely=0.5, anchor="center")
        self.blink()

    def blink(self):
        current_state = self.button.cget('state')
        if current_state == "normal":
            self.button.configure(state="disabled")
        else:
            self.button.configure(state="normal")

        self.after(1000, self.blink)  # Blink every 500 milliseconds

    def on_click(self):
        print("Closing...")
        self.destroy()


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        customtkinter.set_appearance_mode("dark")

        self.full_screen_setup()

        self.main_frame = MainFrame(master=self)
        self.main_frame.grid(row=0, column=0, padx=500, pady=500, sticky="nsew")
        self.grid_rowconfigure(0, weight=10)  
        self.grid_columnconfigure(0, weight=10)

        self.auto_close_timer()

    def full_screen_setup(self):
        self.attributes("-fullscreen", True)  
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        self.geometry(f"{screen_width}x{screen_height}")  

    def auto_close_timer(self):
        # Set the timer to close the window after 2 seconds
        self.after(8000, self.on_auto_close)

    def on_auto_close(self):
        print("Auto-closing App...")
        self.destroy()

app = App()
# this will set the ctkinter window on top of other applications
app.attributes("-topmost", True)
app.mainloop()
