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
        self.__game_title = ""
        self.__has_word_been_guessed = False
        self.__is_game_type_multiplayer = False
        self.__list_length = len(self.__correct_words)
        self.__main_window = Tk()
        self.__random_index_value = 0
        self.__enter_word = Entry()

        self.choose_game_type()

        self.generate_game_board()
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

    def generate_random_index_value(self):
        # self.__is_game_type_multiplayer = False
        self.__random_index_value = randrange(self.__list_length)

    # def testiprintteri(self):
    #     print("NAPPIA MULTIPLAYER ON PAINETTU!")

    def check_if_word_is_correct(self):

        if not self.is_alpha():
            self.__enter_word.configure(bg='red')

        else:
            self.__enter_word.configure(bg='white')


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

        self.__choose_button = Button(self.__main_window, text="Choose",
                                      command=self.check_if_word_is_correct)
        self.__choose_button.grid(row=2, column=3)



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
        pass


def main():
    ui = GameGUI()


if __name__ == "__main__":
    main()

