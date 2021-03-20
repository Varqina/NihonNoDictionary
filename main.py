import tkinter as tk
from tkinter import *
from PIL import Image


from CreateToolTipClass import CreateToolTip

BACKGROUND_COLOR = "#D5F5E3"

window = tk.Tk()
window.config(bg=BACKGROUND_COLOR, padx=10, pady=10)
window.title("日本の辞書")

canvas = Canvas(width=860, height=570, bg=BACKGROUND_COLOR, highlightthickness=0)
front_image = PhotoImage(file="images/card_front.png")
word_image = Image("images/test.png")
word_image

canvas.create_image(430, 300, image=front_image)
canvas.create_image(215, 400, image=word_image)
#allow width = 430, height=200


canvas.create_text(200, 110, text="nihonnowordo", font=("Arial", 20, "bold"))
canvas.create_text(630, 110, text="porandonowordo", font=("Arial", 20, "bold"))
canvas.create_text(430, 200, text="Word's description", font=("Arial", 30, "bold"))
canvas.create_text(615, 400, text="漢字", font=("Arial", 100, "bold"))

canvas.grid(column=0, row=0, columnspan=5, pady=20, padx=20)

# Add image button definition #
add_image_icon = PhotoImage(file="images/addPhoto.png")
add_image = Button(text="Add Image", image=add_image_icon)

# Add association button definition #
add_association_icon = PhotoImage(file="images/add-text.png")
add_association_button = Button(text="Add Association Text", image=add_association_icon)
add_association_hint = CreateToolTip(add_association_button, "Click to add text association")

#Add plus button
plus_button_icon = PhotoImage(file="images/right.png")
plus_button = Button(text="+", image=plus_button_icon, bg=BACKGROUND_COLOR)

#Add minus button
minus_button_icon = PhotoImage(file="images/wrong.png")
minus_button = Button(text="-", image=minus_button_icon)

#Add kanji button
kanji_button_icon = PhotoImage(file="images/kanji.png")
kanji_button = Button(text="kanji", image=kanji_button_icon)
kanji_hint = CreateToolTip(kanji_button, "Click to add kanji")

#Button placement
plus_button.grid(column=0, row=3)
minus_button.grid(column=1, row=3)
add_image.grid(column=2, row=3)
add_association_button.grid(column=3, row=3)
kanji_button.grid(column=4, row=3)

ploand_flag_image = PhotoImage(file="images/polskaflaga.png")
poland_flag_button = Button(text="Poland flag", image=ploand_flag_image)
poland_flag_button_window = canvas.create_window(630, 70, window=poland_flag_button)

47/30
tk.mainloop()
