# password generator app

import pyperclip
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle

# ------------ CONSTANT ------------- #

GREENISH_YELLOW = "#E6EDB7"
GREENISH_WHITE = "#FDFCEF"
LIGHT_SKY = "#C0E5E4"
LIGHT_GREEN = "#92E3A9"
COURIER_FONT = "Courier"

# ------------ UI SETUP --------------------------------- #

# creating window object
window = Tk()

# window title
window.title("Password Generator")

# add custom favicon
window.iconbitmap(r'favicon.ico')

# add padding and background color
window.config(padx=60, pady=60, bg=GREENISH_WHITE)

# canvas size
canvas = Canvas(height=300, width=300, bg=GREENISH_WHITE, highlightthickness=0)

# assign the image location to a variable
logo_image = PhotoImage(file="security.png")
# add image in the canvas in the center by "/" half of the dimension
canvas.create_image(150, 150, image=logo_image)
# assign the grid for the canvas
canvas.grid(row=0, column=1)
