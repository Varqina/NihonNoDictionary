class WordClass:
    occurred_times = 0
    correct_answers = 0
    incorrect_answers = 0
    image = None
    association = ""
    
    def __init__(self, japanese_word, english_word, kanji):
        self.japanese_word = japanese_word
        self.kanji = kanji
        if ',' in english_word:
            english_word = english_word.split(',')
            english_word = '\n'.join(english_word)
        self.english_word = english_word
