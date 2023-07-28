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
# from tkinter.constants import DISABLED, NORMAL


class GameGUI:
    def __init__(self):
        # ATTRIBUTES

        # Booleans
        self.__has_word_been_guessed = False
        # self.__is_button_clicked = False
        self.__is_game_type_multiplayer = False
        self.__was_inputted_word_legal = False

        # Integers
        self.__amount_of_mistakes = 0
        self.__amount_of_guessed_letters = 0
        self.__list_length = 0
        self.__random_index_value = 0
        self.__word_appearance_counter = 0

        # Lists
        self.__correct_words = ["koiruli", "kisse", "rät", "hevone"]
        self.__keyboard = {}
        self.__list_of_correct_letters = []
        self.__single_letter_labels = []

        # Strings
        self.__correct_answer = ""
        self.__current_letter = ""
        self.__game_title = ""

        # tkinter objects
        self.__main_window = Tk()
        self.__enter_word = Entry()

        self.__list_length = len(self.__correct_words)

        self.generate_random_index_value()

        self.choose_game_type()

        if self.__was_inputted_word_legal:
            print("Arvo oli laillinen.")



        # self.__quit_button = Button(self.__main_window, text="QUIT",
        #                              command=self.quit)
        # self.__quit_button.grid(row=1, column=5)

        self.__first_image = PhotoImage(file="pictures/1.png")
        # self.__first_image_label = Label(self.__main_window,
        #                                  image=self.__first_image)
        # self.__first_image_label.grid(row=4, column=0)
        self.__second_image = PhotoImage(file="pictures/2.png")
        self.__third_image = PhotoImage(file="pictures/3.png")
        self.__fourth_image = PhotoImage(file="pictures/4.png")
        self.__fifth_image = PhotoImage(file="pictures/5.png")
        self.__sixth_image = PhotoImage(file="pictures/6.png")
        self.__seventh_image = PhotoImage(file="pictures/7.png")
        self.__eighth_image = PhotoImage(file="pictures/8.png")
        self.__ninth_image = PhotoImage(file="pictures/9.png")
        self.__tenth_image = PhotoImage(file="pictures/10.png")
        self.__eleventh_image = PhotoImage(file="pictures/11.png")

        self.__main_window.mainloop()

    def choose_game_type(self):
        """
        This method generates all the buttons required for choosing the
        game type. The buttons are mapped to respective functions and are run
        based on player choises. If a player clicks multiplayer and then
        regrets it, it's possible to switch to singleplayer if the player
        hasn't chosen a word yet. Doesn't take any external parameters, doesn't
        return anything (returns None implicitely).
        """


        self.__game_title = Label(self.__main_window, text="Hangman")
        self.__game_title.grid(row=0, columnspan=3)

        self.__singleplayer = Button(self.__main_window, text="Singleplayer",
                                     command=self.generate_game_board)
        self.__singleplayer.grid(row=1, column=0)

        self.__multiplayer = Button(self.__main_window, text="Multiplayer",
                                    command=self.choose_your_own_word)
        self.__multiplayer.grid(row=1, column=2)

    # def print_a_letter_by_clicking_a_button(self):
    #     pass

    def generate_random_index_value(self):
        """
        This method generates a random integer value by using random from
        randrange library. This value later becomes the index of the correct
        word. For example, if the value is 1, the correct answer becomes the
        word in the second index. The high limit to this value is the length of
        the list since the random value has to correspond to an existing
        index on the list of available correct words. Doesn't take
        any external parameters, doesn't return anything (returns None
        implicitely).
        """

        # self.__is_game_type_multiplayer = False
        self.__random_index_value = randrange(self.__list_length)
        self.__correct_answer = self.__correct_words[self.__random_index_value]

        print(f"Random index value: {self.__random_index_value}")
        print(self.__correct_words[self.__random_index_value])

        # for i in self.__correct_answer:
        #     self.__list_of_correct_letters.append(i)

    # def testiprintteri(self):
    #     print("NAPPIA MULTIPLAYER ON PAINETTU!")

    def check_if_string_is_legal(self):
        """
        The method checks whether a string is legal. The word is legal
        only if it is alphabetic, i.e. doesn't have any numbers or special
        characters in it. The alphabetic check is done using a seperate method
        Calls the gameboard generation method if the word was legal. Doesn't
        take any external parameters, doesn't return anything (returns None
        implicitely).
        """

        # print(f"Enter wordin arvo: {self.__enter_word.get()}")

        self.__correct_answer = self.__enter_word.get()

        if not self.is_alpha():
            self.__enter_word.configure(bg='red')
            self.__was_inputted_word_legal = False

        # If the program gets here, the word had only letters in it
        else:
            self.__enter_word.configure(bg='white')
            self.__was_inputted_word_legal = True

            if self.__was_inputted_word_legal:
                self.generate_game_board()

                # self.__singleplayer["state"] = "disabled"
                # self.__multiplayer["state"] = "disabled"
                self.__choose_button["state"] = "disabled"
                self.__singleplayer["state"] = "disabled"
                print(f"{self.__correct_answer}")
                # for i in self.__correct_answer:
                #     self.__list_of_correct_letters.append(i)
                return

    def choose_your_own_word(self):
        """
        This method is called when a player chooses to play multiplayer. When
        this happens, his/her co-player gets to choose the correct word of a
        game. This method creates the buttons for the multiplayer
        (choose button and the entry/input box). When the co-player clicks
        choose, the word is then run through a check which is done in a seperate
        method. Doesn't take any external parameters, doesn't return anything
        (returns None implicitely).
        """

        # self.__is_game_type_multiplayer = True
        # self.__enter_word = Entry()

        self.__enter_word.grid(row=2, columnspan=3)

        # self.__correct_answer = self.__enter_word.get()
        self.__choose_button = Button(self.__main_window, text="Choose",
                                      command=self.check_if_string_is_legal)
        self.__choose_button.grid(row=2, column=3)

        # self.__correct_answer = self.__enter_word.get()

        # if self.__was_inputted_word_legal:
        #     print("Arvo oli laillinen.")

        # lista = []
        # lista.append(self.__enter_word) # [sana]
        #
        # for char in temp_str:
        #     if char.isdigit():
        #         print("Sisälsi numeron!")

    def is_alpha(self):
        """The method checks whether a string is alphabetic. First the method
        gets the string from a tkinter Entry object. The word is then checked
        with a built-in method of Python class string. Returns a boolean
        based on the answer. Doesn't take any external parameters."""

        if not self.__enter_word.get().isalpha():
            print("Syötit muita kuin kirjaimia!!!")

            return False

        else:
            return True

    def generate_game_board(self):

        for i in self.__correct_answer:
            self.__list_of_correct_letters.append(i)

        letters = [["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "å"],
                   ["a", "s", "d", "f", "g", "h", "j", "k", "l", "ö", "ä"],
                   ["z", "x", "c", "v", "b", "n", "m"]]

        current_row = 3
        current_column = 3
        for row in letters:
            if current_row == 5:
                current_column = 5

            # self.__another_button = Button(self.__main_window, text=)
            for char in row:
                self.__new_button = Button(self.__main_window, text=char,
                                           command=self.on_button_click)
                self.__new_button.config(command=lambda b=self.__new_button:
                                         self.on_button_click(b))
                self.__new_button.grid(row=current_row + 1,
                                       column=current_column + 1)
                self.__keyboard[char] = self.__new_button
                self.__multiplayer["state"] = "disabled"
                self.__singleplayer["state"] = "disabled"

                self.__enter_word.destroy()
                current_column += 1
            current_column = 3
            current_row += 1

        self.hidden_word()

    def hidden_word(self, i=""):

        current_label_row = 3
        current_label_column = 3

        for letter in self.__correct_answer:

            self.__current_letter = letter

            boi = Label(self.__main_window, text="_")
            boi.grid(row=current_label_row, column=current_label_column + 1)
            current_label_column += 1

            if self.__current_letter == i:
                # boi = Label(self.__main_window, text=letter)
                boi.configure(text=letter)

        # [] [] [] [] [] [] [] [] [] []

        # current_column = 5

        # self.__button_q = Button(self.__main_window, text="Q")
        # self.__button_q.grid()
        #
        # self.__button_w = Button(self.__main_window, text="W")
        # self.__button_w.grid()

    def on_button_click(self, button):

        # for i in self.__correct_answer:
        #     self.__list_of_correct_letters.append(i)

        index = ""
        for index, btn in self.__keyboard.items():
            if btn == button:
                # self.__is_button_clicked = True
                btn["state"] = "disabled"
                print(f"Button {index} was clicked.")
                # self.__enter_word.con

                # if button in correct_answer, hirsipuu ei "kasva",
                # vaan kyseinen kirjain paljastetaan muuttujasta correct_answer

                # if button in correct_answer, the hanging tree doesn't grow,
                # but the corresponding letter is revealed from the variable
                # correct_answer
                break

        for i in self.__correct_answer:
            if i == index:
        # if index in self.__correct_answer:
        #     # self.__list_of_correct_letters.append(index)
        #     for i in self.__correct_answer:
        #         if i == index:
                self.__word_appearance_counter += 1

                self.__current_letter = i
                self.hidden_word(i)
                # joku label -> configure -> kyseisen kirjain paljastetaan
                # tietyltä i:n kohdalta (?)

        self.__amount_of_guessed_letters += \
            self.__word_appearance_counter
        self.was_move_a_winning_move()

        if self.__has_word_been_guessed:
            print("VOITIT")

        elif self.__word_appearance_counter > 0:

            self.__word_appearance_counter = 0

        else:
            self.__amount_of_mistakes += 1
            self.check_amount_of_mistakes()
            # quit()

    def check_amount_of_mistakes(self):

        if self.__amount_of_mistakes == 1:
            self.__first_image_label = Label(self.__main_window,
                                             image=self.__first_image)
            self.__first_image_label.grid(row=7, columnspan=1)
            self.__first_image_label.configure(image=self.__first_image)

        elif self.__amount_of_mistakes == 2:
            self.__second_image_label = Label(self.__main_window,
                                             image=self.__second_image)
            self.__second_image_label.grid(row=7, columnspan=1)
            self.__second_image_label.configure(image=self.__second_image)
            self.__first_image_label.destroy()

        elif self.__amount_of_mistakes == 3:
            self.__third_image_label = Label(self.__main_window,
                                             image=self.__third_image)
            self.__third_image_label.grid(row=7, columnspan=1)
            self.__third_image_label.configure(image=self.__third_image)
            self.__second_image_label.destroy()

        elif self.__amount_of_mistakes == 4:
            self.__fourth_image_label = Label(self.__main_window,
                                             image=self.__fourth_image)
            self.__fourth_image_label.grid(row=7, columnspan=1)
            self.__fourth_image_label.configure(image=self.__fourth_image)
            self.__third_image_label.destroy()

        elif self.__amount_of_mistakes == 5:
            self.__fifth_image_label = Label(self.__main_window,
                                             image=self.__fifth_image)
            self.__fifth_image_label.grid(row=7, columnspan=1)
            self.__fifth_image_label.configure(image=self.__fifth_image)
            self.__fourth_image_label.destroy()

        elif self.__amount_of_mistakes == 6:
            self.__sixth_image_label = Label(self.__main_window,
                                             image=self.__sixth_image)
            self.__sixth_image_label.grid(row=7, columnspan=1)
            self.__sixth_image_label.configure(image=self.__sixth_image)
            self.__fifth_image_label.destroy()

        elif self.__amount_of_mistakes == 7:
            self.__seventh_image_label = Label(self.__main_window,
                                             image=self.__seventh_image)
            self.__seventh_image_label.grid(row=7, columnspan=1)
            self.__seventh_image_label.configure(image=self.__seventh_image)
            self.__sixth_image_label.destroy()

        elif self.__amount_of_mistakes == 8:
            self.__eighth_image_label = Label(self.__main_window,
                                             image=self.__eighth_image)
            self.__eighth_image_label.grid(row=7, columnspan=1)
            self.__eighth_image_label.configure(image=self.__eighth_image)
            self.__seventh_image_label.destroy()

        elif self.__amount_of_mistakes == 9:
            self.__ninth_image_label = Label(self.__main_window,
                                             image=self.__ninth_image)
            self.__ninth_image_label.grid(row=7, columnspan=1)
            self.__ninth_image_label.configure(image=self.__ninth_image)
            self.__eighth_image_label.destroy()

        elif self.__amount_of_mistakes == 10:
            self.__tenth_image_label = Label(self.__main_window,
                                             image=self.__tenth_image)
            self.__tenth_image_label.grid(row=7, columnspan=1)
            self.__tenth_image_label.configure(image=self.__tenth_image)
            self.__ninth_image_label.destroy()

        elif self.__amount_of_mistakes == 11:
            self.__eleventh_image_label = Label(self.__main_window,
                                             image=self.__eleventh_image)
            self.__eleventh_image_label.grid(row=7, columnspan=1)
            self.__eleventh_image_label.configure(image=self.__eleventh_image)
            self.__tenth_image_label.destroy()
            print("HÄVISIT")
            # quit()



    def was_move_a_winning_move(self):
        # list_of_correct_letters = []
        # for i in self.__correct_answer:
        #     self.__list_of_correct_letters.append(i)
        if self.__amount_of_guessed_letters == len(
                self.__list_of_correct_letters):
            self.__has_word_been_guessed = True
        #     return True
        #
        # return False

    def quit(self):
        """
        The method exits the progarm. Takes no external parameters.
        """
        self.__main_window.destroy()

def main():
    """
    Starts the tkinter program. The program is run totally inside the GUI class.
    """
    ui = GameGUI()


if __name__ == "__main__":
    main()
