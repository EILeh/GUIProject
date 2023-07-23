"""
COMP.CS.100 Ohjelmointi 1 / Programming 1

StudentId: 150541820
Name:      Eetu Kuittinen
Email:     eetu.kuittinen@tuni.fi

StudentId: 151309919
Name:      Elli Lehtimäki
Email:     elli.i.lehtimaki@tuni.fi

This game is a Python implementation of the game classic "The Hangman". This
implementation is developed using Python 3.10 with tkinter in the front-end.

The game starts by asking whether the player wants to by play himself/herself or
with someone. If the player chooses to play alone, the game will randomly
select a word from a pre-determined list of words. This is done by generating a
random value using randrange and then choosing the word in the corresponding
index on the list. If the player plays with someone, the other person decides
the word to be guessed by inputting it into a tkinter Entry object.

The player inputs letters by clicking on tkinter buttons with letters on
them. In case of clicking a correct letter, the game will insert it into text
box (in alphabetical order). If the letter is incorrect, the letter gets
disabled and cannot be clicked again.
"""

from random import randrange
from tkinter import *


class GameGUI:
    def __init__(self):
        # ATTRIBUTES

        # Booleans
        self.__has_word_been_guessed = False
        self.__is_game_type_multiplayer = False
        self.__was_inputted_word_legal = False

        # Integers
        self.__amount_of_mistakes = 0
        self.__list_length = 0
        self.__random_index_value = 0

        # Lists
        self.__correct_words = ["koiruli", "kisse", "rät", "hevone"]
        self.__keyboard = []

        # Strings
        self.__correct_answer = ""
        self.__game_title = ""

        # tkinter objects
        self.__main_window = Tk()
        self.__enter_word = Entry()

        self.__list_length = len(self.__correct_words)

        self.choose_game_type()

        self.generate_game_board()

        if self.__was_inputted_word_legal:
            print("Arvo oli laillinen.")

        self.__main_window.mainloop()

    def choose_game_type(self):

        self.__game_title = Label(self.__main_window, text="Hangman")
        self.__game_title.grid(row=0, columnspan=3)

        self.__singleplayer = Button(self.__main_window, text="Singleplayer",
                                     command=self.generate_random_index_value)
        self.__singleplayer.grid(row=1, column=0)

        self.__multiplayer = Button(self.__main_window, text="Multiplayer",
                                    command=self.input_word_to_be_guessed)
        self.__multiplayer.grid(row=1, column=2)

    def print_a_letter_by_clicking_a_button(self):
        pass

    def generate_random_index_value(self):
        # self.__is_game_type_multiplayer = False
        self.__random_index_value = randrange(self.__list_length)
        self.__correct_answer = self.__correct_words[self.__random_index_value]

        print(f"Random index value: {self.__random_index_value}")
        print(self.__correct_words[self.__random_index_value])

    # def testiprintteri(self):
    #     print("NAPPIA MULTIPLAYER ON PAINETTU!")

    def check_if_word_is_legal(self):
        # print(f"Enter wordin arvo: {self.__enter_word.get()}")

        if not self.is_alpha():
            self.__enter_word.configure(bg='red')
            self.__was_inputted_word_legal = False

        else:
            self.__enter_word.configure(bg='white')
            self.__was_inputted_word_legal = True

            if self.__was_inputted_word_legal:
                print("Arvo oli laillinen.")
                return



            # while not self.is_alpha():


        # while True:
        #
        #     if self.check_if_alpha():
        #         self.__enter_word.configure(bg='white')
        #     else:
        #         self.__enter_word.configure(bg='red')
        #         return




    def input_word_to_be_guessed(self):
        # self.__is_game_type_multiplayer = True
        self.__enter_word = Entry()
        self.__enter_word.grid(row=2, columnspan=3)
        # self.__correct_answer = self.__enter_word.get()
        self.__choose_button = Button(self.__main_window, text="Choose",
                                      command=self.check_if_word_is_legal)
        self.__choose_button.grid(row=2, column=3)
        # if self.__was_inputted_word_legal:
        #     print("Arvo oli laillinen.")




        # lista = []
        # lista.append(self.__enter_word) # [sana]
        #
        # for char in temp_str:
        #     if char.isdigit():
        #         print("Sisälsi numeron!")

    def is_alpha(self):

        if not self.__enter_word.get().isalpha():
            print("Syötit muita kuin kirjaimia!!!")

            return False

        else:
            return True

    def generate_game_board(self):

        letters = [["q", "w", "e", "r", "t", "y", "u", "i", "o", "p",
                          "å"],
                    ["a", "s", "d", "f", "g", "h", "j", "k", "l", "ö", "ä"],
                    ["z", "x", "c", "v", "b", "n", "m"]]

        current_row = 3
        current_column = 3
        for row in letters:
            if current_row == 5:
                current_column = 5

            # self.__another_button = Button(self.__main_window, text=)
            for char in row:

                self.__new_button = Button(self.__main_window, text=char)
                self.__new_button.grid(row=current_row+1,
                                       column=current_column+1)
                self.__keyboard.append(self.__new_button)
                current_column += 1
            current_column = 3
            current_row += 1
        # current_column = 5

        # self.__button_q = Button(self.__main_window, text="Q")
        # self.__button_q.grid()
        #
        # self.__button_w = Button(self.__main_window, text="W")
        # self.__button_w.grid()


def main():
    ui = GameGUI()


if __name__ == "__main__":
    main()