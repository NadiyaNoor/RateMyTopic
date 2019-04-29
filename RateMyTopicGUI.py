import os
from tkinter import Tk, Button, Entry, Label, END, PhotoImage, font, ttk, Toplevel
from PIL import Image, ImageTk
from RateMyTopic import RateThis

def getTweets(): 
    ''' Getting Tweets and Displaying Ratings'''  
        
    global topicEnt
    global numEnt


    # Read height and weight from user
    topic = topicEnt.get() 
    num = int(numEnt.get())
        
    newWin = Toplevel(root)
    newWin['bg'] = '#B3CCF8'


    # Logo
    logoLabel2 = Label(newWin, image=img, height=100, width=100)
    logoLabel2.grid(row=0, columnspan=3) 
    logoLabel2['bg'] = '#B3CCF8'


    # Title
    titleLabel2 = Label(newWin, text='Rate My Topic', font=("Trebuchet MS bold", 18))
    titleLabel2.grid(row=1, columnspan=3, pady=(0, 50)) 
    titleLabel2['bg'] = '#B3CCF8'


    # Results Label 
    resultsLabel = Label(newWin, text="Rating '{}' Using {} Tweets".format(topic, num), font=("Trebuchet MS", 14)) 
    resultsLabel.grid(row=2, columnspan=3, padx=20, pady=20) 
    resultsLabel['bg'] = '#B3CCF8'


    rateThis = RateThis()
    positive, neutral, negative = rateThis.analyzeTweets(topic, num)
    
    # Polarity Label 
    polarityLabel = Label(newWin, text="Rating:\n {}% Positive\n {}% Neutral\n {}% Negative".format(positive, neutral, negative), 
        font=("Trebuchet MS", 14)) 
    polarityLabel.grid(row=3, columnspan=3, padx=20, pady=20) 
    polarityLabel['bg'] = '#B3CCF8'


    # Clear entry
    topicEnt.delete(0, END) 
    numEnt.delete(0, END) 


root = Tk()
root['bg'] = '#B3CCF8'


# Logo
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
img = ImageTk.PhotoImage(Image.open((os.path.join(__location__, 'twitterLogo.png'))))
logoLabel = Label(root, image=img, height=100, width=100)
logoLabel.grid(row=0, columnspan=2) 
logoLabel['bg'] = '#B3CCF8'


# Title
titleLabel = Label(root, text='Rate My Topic', font=("Trebuchet MS bold", 18))
titleLabel.grid(row=1, columnspan=2, pady=(0, 50)) 
titleLabel['bg'] = '#B3CCF8'


# Topic Label
tologoLabel = Label(root, text='Enter the Topic: ', font=("Trebuchet MS", 14)) 
tologoLabel.grid(row=2, column=0, padx=20, pady=20) 
tologoLabel['bg'] = '#B3CCF8'


# Topic Entry
topicEnt = Entry(root, font=("Trebuchet MS", 14)) 
topicEnt.grid(row=2, column=1)


# Number Label 
numLabel = Label(root, text='Enter Number of Tweets to Search:', font=("Trebuchet MS", 14)) 
numLabel.grid(row=3, column=0, padx=20, pady=20) 
numLabel['bg'] = '#B3CCF8'


# Number Entry 
numEnt = Entry(root, font=("Trebuchet MS", 14))
numEnt.grid(row=3, column=1, padx=20, pady=20)


# Submit Button 
submitButton = Button(root, text='Submit', font=("Trebuchet MS", 12), command=getTweets)
submitButton.grid(row=5, columnspan=3, padx=20, pady=20) 


root.mainloop()