class WordClass:
    occured_times = 0
    correct_answers = 0
    incorrect_answers = 0
    image = ""
    def __init__(self, japanese_word, english_word, kanji) -> None:
        self.japanese_word = japanese_word
        self.english_word = english_word
        self.kanji = kanji
