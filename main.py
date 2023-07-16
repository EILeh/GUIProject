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
        self.__correct_words = ["koiruli", "kisse", "rät", "hevone"]
        self.__keyboard = []
        self.__game_title = ""
        self.__has_word_been_guessed = False
        self.__is_game_type_multiplayer = False
        self.__was_inputted_word_legal = False
        self.__list_length = len(self.__correct_words)
        self.__main_window = Tk()
        self.__random_index_value = 0
        self.__enter_word = Entry()

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

        self.__keyboard = [["q", "w", "e", "r", "t", "y", "u", "i", "o", "p",
                          "å"],
                    ["a", "s", "d", "f", "g", "h", "j", "k", "l", "ö", "ä"],
                    ["z", "x", "c", "v", "b", "n", "m"]]

        current_row = 3
        current_column = 3
        for row in self.__keyboard:
            if current_row == 5:
                current_column = 5

            # self.__another_button = Button(self.__main_window, text=)
            for char in row:

                self.__new_button = Button(self.__main_window, text=char)
                self.__new_button.grid(row=current_row+1,
                                       column=current_column+1)
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