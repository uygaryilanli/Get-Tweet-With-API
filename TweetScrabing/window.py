import tkinter
from users import Users

class Window:
    def __init__(self) -> None:
        #SCRREEN
        self.users = Users()
        self.window = tkinter.Tk()
        self.window.minsize(height=500, width=700)
        self.window.title("Login Window")
        self.window.config(padx=20, pady=20, bg="white", highlightthickness=0)
        #LOGO
        self.canvas = tkinter.Canvas(width=360, height=360)
        self.canvas.config(bg="white", highlightthickness=0)
        self.logo_image = tkinter.PhotoImage(file="tweet.png")
        self.canvas.create_image(175, 175, image=self.logo_image)
        self.canvas.pack()
        #LOGIN INPUTS
        self.email_input = tkinter.Entry(width=25)
        self.email_input.place(x=60, y=350)
        self.email_label = tkinter.Label(text="Email:")
        self.email_label.place(x=10, y=350)
        self.email_label.config(bg="white", highlightthickness=0)
        self.password_input = tkinter.Entry(width=25)
        self.password_input.place(x=60, y=375)
        self.password_label = tkinter.Label(text="Password:")
        self.password_label.place(x=0, y=375)
        self.password_label.config(bg="white", highlightthickness=0)
        self.login_title_label = tkinter.Label(text="Giriş Yap")
        self.login_title_label.place(x=100, y=310)
        self.login_title_label.config(font=35, bg="white")
        #REGISTER INPUTS
        self.reg_email_input = tkinter.Entry(width=25)
        self.reg_email_input.place(x=475, y=275)
        self.reg_email_label = tkinter.Label(text="Email:")
        self.reg_email_label.place(x=425, y=275)
        self.reg_email_label.config(bg="white", highlightthickness=0)
        self.reg_password_input = tkinter.Entry(width=25)
        self.reg_password_input.place(x=475, y=300)
        self.reg_password_label = tkinter.Label(text="Password:")
        self.reg_password_label.place(x=415, y=300)
        self.reg_password_label.config(bg="white", highlightthickness=0)
        self.reg_country_input = tkinter.Entry(width=25)
        self.reg_country_input.place(x=475, y=325)
        self.reg_country_label = tkinter.Label(text="Ülke(TR, EN):")
        self.reg_country_label.place(x=400, y=325)
        self.reg_country_label.config(bg="white", highlightthickness=0)
        self.reg_name_input = tkinter.Entry(width=25)
        self.reg_name_input.place(x=475, y=350)
        self.reg_name_label = tkinter.Label(text="Name:")
        self.reg_name_label.place(x=425, y=350)
        self.reg_name_label.config(bg="white", highlightthickness=0)
        self.reg_surname_input = tkinter.Entry(width=25)
        self.reg_surname_input.place(x=475, y=375)
        self.reg_surname_label = tkinter.Label(text="Surname:")
        self.reg_surname_label.place(x=410, y=375)
        self.reg_surname_label.config(bg="white", highlightthickness=0)
        self.reg_age_input = tkinter.Entry(width=25)
        self.reg_age_input.place(x=475, y=400)
        self.reg_age_label = tkinter.Label(text="Age:")
        self.reg_age_label.place(x=430, y=400)
        self.reg_age_label.config(bg="white", highlightthickness=0)
        self.register_title_label = tkinter.Label(text="Kayıt Ol")
        self.register_title_label.place(x=510, y=225)
        self.register_title_label.config(font=35, bg="white")
        #BUTTONS
        self.login_button = tkinter.Button(text="Login", width=21, command=lambda: self.users.get_login(email_input=self.email_input, password_input=self.password_input, window=self.window))
        self.login_button.place(x=60, y=400)
        self.register_button = tkinter.Button(text="Register", width=21, command=lambda: self.users.post_register(
            self.reg_country_input,
            self.reg_name_input,
            self.reg_surname_input,
            self.reg_age_input,
            self.reg_email_input,
            self.reg_password_input
        ))
        self.register_button.place(x=475, y=425)
        
        
        
        self.window.mainloop()