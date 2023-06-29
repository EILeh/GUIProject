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


class GameGUI:
    def __init__(self):
        # Attributes
        self.__amount_of_mistakes = 0
        self.__correct_answer = ""
        self.__correct_words = ["xyzz:-)", "kaupunki:D", "SuomiÖ", "moi:)"]
        self.__has_word_been_guessed = False
        self.__is_game_type_multiplayer = False
        self.__list_length = len(self.__correct_words)
        self.__main_window = Tk()
        self.__random_index_value = 0


        if self.choose_game_type():
            self.generate_random_index_value()

        else:
            self.input_word_to_be_guessed()

        self.generate_game_board()
        self.__main_window.mainloop()

    def choose_game_type(self):

        self.__singleplayer = Button(self.__main_window, text="Singleplayer")
        self.__singleplayer.grid(row=0, column=0)

        self.__multiplayer = Button(self.__main_window, text="Multiplayer")
        self.__multiplayer.grid(row=0, column=1)

    def generate_random_index_value(self):
        self.__random_index_value = randrange(self.__list_length)

    def input_word_to_be_guessed(self):
        pass

    def generate_game_board(self):
        pass


def main():
    ui = GameGUI()


if __name__ == "__main__":
    main()

