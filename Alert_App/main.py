import customtkinter

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        customtkinter.set_appearance_mode("dark")
        self.full_screen_setup()
        self.button = customtkinter.CTkButton(self, text="Close", command=self.on_btn_click)
        self.button.pack(padx=20, pady=20)

    def full_screen_setup(self):
        self.attributes("-fullscreen", True)  
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        self.geometry(f"{screen_width}x{screen_height}")  # Set geometry to screen size

    def on_btn_click(self):
        print("Closing...")
        self.destroy()

app = App()
app.mainloop()
