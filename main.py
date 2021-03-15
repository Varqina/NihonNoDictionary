import tkinter as tk
from tkinter import *

from CreateToolTipClass import CreateToolTip

BACKGROUND_COLOR = "#D5F5E3"

window = tk.Tk()
window.config(bg=BACKGROUND_COLOR, padx=10, pady=10)
window.title("日本の辞書")

canvas = Canvas(height=570, width=860, bg=BACKGROUND_COLOR, highlightthickness=0)
front_image = PhotoImage(file="images/card_front.png")
canvas.create_image(430, 300, image=front_image)
canvas.grid(column=0, row=0, columnspan=4, pady=20, padx=20)

add_image_icon = PhotoImage(file="images/addPhoto.png")
add_image = Button(text="Add Image", image=add_image_icon)

# Add association button definition #
add_association_icon = PhotoImage(file="images/add-text.png")
add_association_button = Button(text="Add Association Text", image=add_association_icon)
add_association_hint = CreateToolTip(add_association_button, "some text")

plus_button_icon = PhotoImage(file="images/right.png")
plus_button = Button(text="+", image=plus_button_icon, bg=BACKGROUND_COLOR)
minus_button_icon = PhotoImage(file="images/wrong.png")
minus_button = Button(text="-", image=minus_button_icon)
add_image.grid(column=2, row=3)
add_association_button.grid(column=3, row=3)
plus_button.grid(column=0, row=3)
minus_button.grid(column=1, row=3)

tk.mainloop()
