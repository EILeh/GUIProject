"""
COMP.CS.100 Ohjelmointi 1 / Programming 1

StudentId: 150541820
Name:      Eetu Kuittinen
Email:     eetu.kuittinen@tuni.fi

StudentId: 151309919
Name:      Elli Lehtimäki
Email:     elli.i.lehtimaki@tuni.fi
"""

from random import randrange
from tkinter import *


class Game_GUI:
    def __init__(self):
        self.__amount_of_mistakes = 0
        self.__correct_answer = ""
        self.__correct_words = ["hevonen", "kaupunki", "Suomi"]
        self.__has_word_been_guessed = False
        self.__mainwindow = Tk()
        self.__random_index_value = 0
        self.__list_length = len(self.__correct_words)

    def start(self):
        """
        Starts the mainloop.
        """
        self.__mainwindow.mainloop()


    def generate_random_index_value(self):
        return randrange(self.__list_length)





def main():
    ui = Game_GUI()
    ui.start()
if __name__ == "__main__":
    main()