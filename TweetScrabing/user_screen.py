import tkinter
from tweet_data import TweetService



class UserScreen:
    
    
    def __init__(self) -> None:
        self.tweet = TweetService()
        #WİNDOW
        self.user_window = tkinter.Tk()
        self.user_window.title("Take Tweets")
        self.user_window.minsize(height=500, width=700)
        self.user_window.config(padx=20, pady=20, bg="white", highlightthickness=0)
        #LOGO
        self.user_canvas = tkinter.Canvas(width=360, height=360)
        self.user_canvas.config(bg="white", highlightthickness=0)
        self.user_logo_image = tkinter.PhotoImage(file="user_tweet.png")
        self.user_canvas.create_image(175, 175, image=self.user_logo_image)
        self.user_canvas.pack()
        #INPUT
        self.username_input = tkinter.Entry(width=25)
        self.username_input.place(x=245, y=375)
        #LABEL
        self.username_input_label = tkinter.Label(text="Lütfen yukarıdaki alana bilgilerini çekmek istediğiniz bilginin ismini giriniz.")
        self.username_input_label.place(x=96, y=410)
        #BUTTON
        self.username_info_button = tkinter.Button(text="Gönder", width=21, command=lambda : self.tweet.get_tweet(tweet_serach=self.username_input))
        self.username_info_button.place(x=245, y=440)
        
        
        
        
        
        self.user_window.mainloop()