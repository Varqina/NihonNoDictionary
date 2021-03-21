from WordClass import WordClass
import tkinter 
from tkinter import *
from CreateToolTipClass import CreateToolTip
import math
import pandas
import random

BACKGROUND_COLOR = "#D5F5E3"

def adjust_image(photo_image_object):
    width = photo_image_object.width()
    height = photo_image_object.height()
    size_factor = 0
    if width > 430 or height > 200:
        if width > 430:
            size_factor = math.ceil(width / 430)
        else:
            size_factor = math.ceil(height / 200)
        
    return photo_image_object.subsample(size_factor)

def set_word_on_gui():
    global session_correct_answers_amount, session_incorrect_answers_amount
    word = get_word()
    canvas.itemconfig(japan_word_canvas, text=word.japanese_word)
    canvas.itemconfig(english_word_canvas, text='*' * len(word.english_word))
    canvas.itemconfig(word_association_canvas, text=word.association)
    canvas.itemconfig(kanji_canvas, text=word.kanji)
    total_score_label.config(text=f"Total : {word.correct_answers}/{word.incorrect_answers}")
    occurred_times_label.config(text=f"Occurred: {word.occurred_times}")
    score_label.config(text=f"Score: {session_correct_answers_amount}/{session_incorrect_answers_amount}")
    
    # if 17 < len(word.english_word) < 20 and not "/n" in word.english_word:
    #     canvas.itemconfig(english_word_canvas, font=("Arial", 24, "bold"))
    # elif 20 < len(word.english_word):
    #     canvas.itemconfig(english_word_canvas, font=("Arial", 20, "bold"))
    # else:
    #     canvas.itemconfig(english_word_canvas, font=("Arial", 30, "bold"))
    if word.image is not None:
        word_image = PhotoImage(file=word.image)
        word_image = adjust_image(word_image)
        canvas.itemconfig(word_image_canvas, image=word_image)
    global word_on_the_screen
    word_on_the_screen = word

def get_word():
    word = main_word_list[random.randint(0, len(main_word_list) -1)]
    return word

def setup_translation_visibility():
    if '*' in canvas.itemcget(english_word_canvas, 'text'):
        canvas.itemconfig(english_word_canvas, text=word_on_the_screen.english_word)
    else:
        canvas.itemconfig(english_word_canvas, text='*' * len(word_on_the_screen.english_word))
    
def add_association():
    inpt_window = Toplevel()
    inpt_window.config(bg=BACKGROUND_COLOR, padx=10, pady=10)
    inpt_window.title("Set association")
    association_label = Label(inpt_window, text=f"Provide association for the word {word_on_the_screen.japanese_word}",
                                                 bg=BACKGROUND_COLOR, font=("Arial", 14, "bold"))
    association_entry = Entry(inpt_window, width = 50)
    def save_association():
        user_association = association_entry.get()
        global word_on_the_screen
        word_on_the_screen.association = user_association
        canvas.itemconfig(word_association_canvas, text=word_on_the_screen.association)
        inpt_window.destroy()    
    save_button = Button(inpt_window, text="Save", command=save_association)
    association_label.pack()
    association_entry.pack()
    save_button.pack()

def incorrect_answer():
    global word_on_the_screen
    word_on_the_screen.incorrect_answers += 1
    global session_incorrect_answers_amount
    session_incorrect_answers_amount += 1
    set_word_on_gui()

def correct_answer():
    global word_on_the_screen
    word_on_the_screen.correct_answers += 1
    global session_correct_answers_amount
    session_correct_answers_amount += 1
    set_word_on_gui()

#Read data from CSV file and load to main word list
data = pandas.read_csv("JLPTN5.csv").to_dict('list')
word_bank = data['Phrase']
main_word_list =  []
for word in word_bank:
    word = word.split('-')
    english_word = word[1]
    word = word[0].replace(" ","").split(',')
    if len(word) == 2:
        kanji = word[0]
        japanese_word = word[1]
    else:
        kanji = ""
        japanese_word = word[0]
    main_word_list.append(WordClass(japanese_word, english_word, kanji))


session_correct_answers_amount = 0
session_incorrect_answers_amount = 0

window = tkinter.Tk()
window.config(bg=BACKGROUND_COLOR, padx=10, pady=10)
window.title("日本の辞書")

#Canvas definition
canvas = Canvas(width=860, height=570, bg=BACKGROUND_COLOR, highlightthickness=0)
front_image = PhotoImage(file="images/card_front.png")
canvas.create_image(430, 300, image=front_image)
word_image_canvas = canvas.create_image(215, 400)
japan_word_canvas = canvas.create_text(200, 130, text="", font=("Arial", 30, "bold"))
english_word_canvas = canvas.create_text(630, 130, width=200, text="", font=("Arial", 30, "bold"))
word_association_canvas = canvas.create_text(430, 200, text="", font=("Arial", 30, "bold"))
kanji_canvas = canvas.create_text(615, 400, text="", font=("Arial", 50, "bold"))
canvas.grid(column=0, row=1, columnspan=5, pady=20, padx=20)

#Labels section
score_label = Label(font=("Arial", 20, "bold"), bg=BACKGROUND_COLOR, width=15)
total_score_label = Label(font=("Arial", 20, "bold"), bg=BACKGROUND_COLOR, width=15)
occurred_times_label = Label(font=("Arial", 20, "bold"), bg=BACKGROUND_COLOR, width=15)
holder1 = Label(font=("Arial", 20, "bold"), bg=BACKGROUND_COLOR, width=15)
holder2 = Label(font=("Arial", 20, "bold"), bg=BACKGROUND_COLOR, width=15)
score_label.grid(column=0, row=0)
total_score_label.grid(column=1, row=0)
occurred_times_label.grid(column=2, row=0)
holder1.grid(column=3, row=0)
holder2.grid(column=4, row=0)

#Buttons section
add_image_icon = PhotoImage(file="images/addPhoto.png")
add_image = Button(text="Add Image", image=add_image_icon)

add_association_icon = PhotoImage(file="images/add-text.png")
add_association_button = Button(text="Add Association Text", image=add_association_icon, command=add_association)
add_association_hint = CreateToolTip(add_association_button, "Click to add text association")

plus_button_icon = PhotoImage(file="images/right.png")
plus_button = Button(text="+", image=plus_button_icon, bg=BACKGROUND_COLOR, command=correct_answer)

minus_button_icon = PhotoImage(file="images/wrong.png")
minus_button = Button(text="-", image=minus_button_icon, command=incorrect_answer)

kanji_button_icon = PhotoImage(file="images/kanji.png")
kanji_button = Button(text="kanji", image=kanji_button_icon)
kanji_hint = CreateToolTip(kanji_button, "Click to add kanji")

english_flag_image = PhotoImage(file="images/englishflag.png")
english_flag_button = Button(text="English flag", image=english_flag_image, command=setup_translation_visibility)
english_flag_button_window = canvas.create_window(480, 120, window=english_flag_button)

plus_button.grid(column=0, row=4)
minus_button.grid(column=1, row=4)
add_image.grid(column=2, row=4)
add_association_button.grid(column=3, row=4)
kanji_button.grid(column=4, row=4)

set_word_on_gui()
window.mainloop()
