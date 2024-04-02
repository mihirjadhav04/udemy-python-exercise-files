from tkinter import *
import pandas
import random


BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

# to check whether the to learn work is present in the data folder.(Game played for once or not?)
try:
    data = pandas.read_csv("data/words_to_learn.csv")

# will run if the file not found(means running for the first time or didn't knew any words on the firts run. File not created.)
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")

# If there are no errors and list for words to learn is created.
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    """
    To show the next card on the click of the button by randomly choosing the word from the list of cards.
    """
    global current_card, flip_timer
    window.after_cancel(
        flip_timer
    )  # because the delay should work only when the screen is stopped on a word and not when clicked multiple times.
    current_card = random.choice(to_learn)
    # itemconfig is used to configure a particular item widget and change or update it's value/properties.
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    """
    To flip the card after 3 seconds of delay and show the English translation of the word.
    """
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)


def is_known():
    """
    To generate a new list of cards and store it into .csv file for future use by deleting the known word from the list.
    """
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


# Creating tkinter object and basic config settings for the window.
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)
# Canvas widget to show that card and elements on top of eachother
canvas = Canvas(width=800, height=526)


# to add image on to the canvas with PhotoImage.
card_back_img = PhotoImage(file="images/card_back.png")
card_front_img = PhotoImage(file="images/card_front.png")
card_background = canvas.create_image(400, 263, image=card_front_img)


# to change the BG color of the canvas and make the border thickness to 0.
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

# to add some text on the screen at a particular position with the specified fonts.
card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))


# to place the element on the particular row and column.
canvas.grid(row=0, column=0, columnspan=2)

# to display the cancel button on the screen
cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, command=next_card)
unknown_button.grid(row=1, column=0)

# to display the right button on the screen
right_image = PhotoImage(file="images/right.png")
known_button = Button(image=right_image, command=is_known)
known_button.grid(row=1, column=1)


# Calling the card function for the first time after the screen is visible.
next_card()


# to make sure our window is present on the screen(Running).
window.mainloop()
