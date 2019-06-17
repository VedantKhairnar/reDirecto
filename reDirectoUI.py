import webbrowser
from tkinter import *

class UI:
    @staticmethod
    def google():
        print("Opening Google Search")
        webbrowser.open('https://www.google.com/', new=2)

    @staticmethod
    def gmail():
        print("Opening Google Mail(GMAIL)")
        webbrowser.open('https://www.google.com/gmail/', new=2)

    @staticmethod
    def drive():
        print("Opening Google Drive")
        webbrowser.open('https://www.google.com/drive/', new=2)

    @staticmethod
    def whatsapp():
        print("Opening WhatsApp")
        webbrowser.open('https://web.whatsapp.com', new=2)

    @staticmethod
    def instagram():
        print("Opening Instagram")
        webbrowser.open('https://instagram.com', new=2)

    @staticmethod
    def facebook():
        print("Opening Facebook")
        webbrowser.open('https://facebook.com', new=2)

    @staticmethod
    def twitter():
        print("Opening Twitter")
        webbrowser.open('https://twitter.com/', new=2)

    @staticmethod
    def snapchat():
        print("Opening Snapchat")
        webbrowser.open('https://www.snapchat.com/', new=2)

    @staticmethod
    def amazon():
        print("Opening Amazon")
        webbrowser.open('https://www.amazon.in/', new=2)

    @staticmethod
    def flipkart():
        print("Opening Flipkart")
        webbrowser.open(' https://www.flipkart.com/', new=2)

    @staticmethod
    def myntra():
        print("Opening Myntra")
        webbrowser.open('https://www.myntra.com/', new=2)

    @staticmethod
    def jabong():
        print("Opening Jabong")
        webbrowser.open('https://www.jabong.com/', new=2)

    @staticmethod
    def youtube():
        print("Opening YouTube")
        webbrowser.open('https://www.youtube.com/', new=2)

    @staticmethod
    def wiki():
        print("Opening Wikipedia")
        webbrowser.open('https://www.wikipedia.org/', new=2)


    def __init__(self):
        self.root = Tk()
        self.root.geometry('1400x1000')
        self.root.title("reDirecto")

        photo = PhotoImage(file="OFFICIAL.png")
        wall =Label(self.root,image=photo)
        wall.place(x=-10,y=0)

#.............................................GOOGLE...............................................

        photogoogle = PhotoImage(file="google.png")
        buttongoogle = Button(self.root, compound=TOP, width=150, height=130, image=photogoogle, text="google",bg='black', borderwidth= 0, command=self.google)
        buttongoogle.place(x=10,y=100)

        photogmail = PhotoImage(file="gmail.png")
        buttongmail = Button(self.root, compound=TOP, width=150, height=130, image=photogmail, bg='black',borderwidth= 0,command=self.gmail)
        buttongmail.place(x=200,y=100)

        photodrive = PhotoImage(file="drive.png")
        buttondrive = Button(self.root, compound=TOP, width=150, height=130, image=photodrive,bg='black',borderwidth= 0, command=self.drive)
        buttondrive.place(x=400,y=100)
#.......................................SOCIAL MEDIA SERVICES.................................................

        photowhatsapp = PhotoImage(file="whatsapp.png")
        buttonwhatsapp = Button(self.root, compound=TOP, width=150, height=130, image=photowhatsapp,bg='black',borderwidth= 0, command=self.whatsapp)
        buttonwhatsapp.place(x=10,y=300)

        photoinstagram = PhotoImage(file="instagram.png")
        buttoninstagram = Button(self.root, compound=TOP, width=150, height=130, image=photoinstagram,bg='black',borderwidth= 0, command=self.instagram)
        buttoninstagram.place(x=200,y=300)

        photofacebook = PhotoImage(file="facebook.png")
        buttonfacebook = Button(self.root, compound=TOP, width=150, height=130, image=photofacebook,bg='black',borderwidth= 0, command=self.facebook)
        buttonfacebook.place(x=400,y=300)

        phototwitter = PhotoImage(file="twitter.png")
        buttontwitter = Button(self.root, compound=TOP, width=150, height=130, image=phototwitter,bg='black',borderwidth= 0, command=self.twitter)
        buttontwitter.place(x=600,y=300)

        photosnapchat = PhotoImage(file="snapchat.png")
        buttonsnapchat = Button(self.root, compound=TOP, width=150, height=130, image=photosnapchat,bg='black',borderwidth= 0, command=self.snapchat)
        buttonsnapchat.place(x=800,y=300)

#............................................ONLINE SHOPPINNG SERVICES...................................

        photoamazon = PhotoImage(file="amazon.png")
        buttonamazon = Button(self.root, compound=TOP, width=150, height=155, image=photoamazon, bg='white',borderwidth= 0,command=self.amazon)
        buttonamazon.place(x=10,y=450)

        photoflipkart = PhotoImage(file="flipkart.png")
        buttonflipkart = Button(self.root, compound=TOP, width=150, height=155, image=photoflipkart, bg='black',borderwidth= 0,command=self.flipkart)
        buttonflipkart.place(x=200,y=450)

        photomyntra = PhotoImage(file="myntra.png")
        buttonmyntra = Button(self.root, compound=TOP, width=150, height=155, image=photomyntra, bg='black',borderwidth= 0,command=self.myntra)
        buttonmyntra.place(x=400,y=450)

        photojabong = PhotoImage(file="jabong.png")
        buttonjabong = Button(self.root, compound=TOP, width=150, height=155, image=photojabong, bg='white',borderwidth= 0,command=self.jabong)
        buttonjabong.place(x=600,y=450)

#...............................................OTHERS..........................................
        photoyoutube = PhotoImage(file="youtube.png")
        buttonyoutube = Button(self.root, compound=TOP, width=150, height=130, image=photoyoutube, text="youtube",bg='black',borderwidth= 0, command=self.youtube)
        buttonyoutube.place(x=200,y=620)

        photowiki = PhotoImage(file="wiki.png")
        buttonwiki = Button(self.root, compound=TOP, width=150, height=130, image=photowiki, text="wiki", bg='black',borderwidth= 0,command=self.wiki)
        buttonwiki.place(x=10,y=620)

        name = Label(self.root, text="reDirecto", bg='black',fg='red',font=100)
        name.config(font=("magneto", 30))
        name.place(x=900, y=100)
#...................................................................................................................................

        self.root.mainloop()
s = UI()
