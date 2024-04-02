from tkinter import *

# window = Tk()

# to change the title of the window
# window.title("My GUI Window")

# to give our window a minimum height and width.
# window.minsize(width=500, height=300)

# my_label = Label(text="I am a Label")
# my_label.pack()  # packer is needed to show our label on the screen.


def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)


window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

# Label
my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

# Button
button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

new_button = Button(text="New Button")
new_button.grid(column=2, row=0)

# Entry
input = Entry(width=10)
print(input.get())
input.grid(column=3, row=2)


# To keep the window on the screen and it should be always on the bottom of your code.
window.mainloop()
