import customtkinter as ctk



def aFunction():
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("green")
    app = ctk.CTk()
    app.geometry("400x400")
    app.title("Minerva Demo")


    def login():

        username = ""
        password = ""
        new_window = ctk.CTkToplevel(app)

        new_window.title("Minerva Demo")

        new_window.geometry("350x150")

        if (user_entry.get() == username and user_pass.get() == password):
            app.destroy()


    label = ctk.CTkLabel(app,text="Welcome to Minerva", font=('Calibri', 30))

    label.pack(pady=20)


    frame = ctk.CTkFrame(master=app)
    frame.pack(pady=20,padx=40,fill='both',expand=True)

    label = ctk.CTkLabel(master=frame,text="Enter Your Login Credentials")
    label.pack(pady=12,padx=10)


    user_entry= ctk.CTkEntry(master=frame,placeholder_text="Username")
    user_entry.pack(pady=12,padx=10)

    user_pass= ctk.CTkEntry(master=frame,placeholder_text="Password",show="*")
    user_pass.pack(pady=12,padx=10)


    button = ctk.CTkButton(master=frame,text='Login',command=login)
    button.pack(pady=12,padx=10)

    checkbox = ctk.CTkCheckBox(master=frame,text='Remember Me')
    checkbox.pack(pady=12,padx=10)


    app.mainloop()