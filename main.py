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

Game instructions:
When the game starts, player can choose either to play singleplayer game or
multiplayer game by pressing the buttons on the screen.

Singleplayer game:
If player chooses to play the singleplayer game, the program randomly chooses a
word from a list that the player has to guess to win.

Multiplayer game:
If player chooses to play the multiplayer game, the game can be played with
someone else. After pressing the multiplayer button, an entry appears on the
screen and another player can enter a word that the other player has to guess to
win. The word can be 1-11 letters long and must contain only letters. The choose
button must be pressed for the game to start.

The game functionality:
A keyboard appears on the screen and by pressing the letter the player wants
to guess, the program will check if the letter is found in the chosen or
randomly drawn word. Player has 11 wrong guesses before the game ends. If the
guess is wrong, a hangman picture will appear on the screen and player has
one guess less. If the guess is correct, the letter will appear on the screen at
the correct spot in the word. If player guesses the word before getting 11
wrong guesses, the game has been won. When the game is won or lost, another
screen appears with a text according the end result. On the screen also
appears a quit button that shuts the program once clicked.
"""

from random import randrange
from tkinter import *
import tkinter.font as font


MAX_LENGTH_FOR_WORD_TO_BE_GUESSED = 11
FIRST_MISTAKE = 1
SECOND_MISTAKE = 2
THIRD_MISTAKE = 3
FOURTH_MISTAKE = 4
FIFTH_MISTAKE = 5
SIXTH_MISTAKE = 6
SEVENTH_MISTAKE = 7
EIGHTH_MISTAKE = 8
NINTH_MISTAKE = 9
TENTH_MISTAKE = 10
ELEVENTH_MISTAKE = 11

class GameGUI:
    def __init__(self):
        # ATTRIBUTES

        # Booleans
        self.__has_word_been_guessed = False
        self.__has_game_been_lost = False

        # Dictionaries
        self.__keyboard = {}

        # Integers
        self.__amount_of_mistakes = 0
        self.__amount_of_guessed_letters = 0
        self.__list_length = 0
        self.__random_index_value = 0
        self.__word_appearance_counter = 0

        # Lists
        self.__correct_guesses = []
        self.__correct_words = ["KOIRA", "KISSA", "HIIRI", "HEVONEN", "KIVI",
                                "TUOLI", "AURINKO", "KUOLEMA", "JÄÄTELÖ",
                                "KESÄPÄIVÄ", "TALVIYÖ", "KANGASALA", "HERVANTA"]

        self.__list_of_correct_letters = []

        # Strings
        self.__correct_answer = ""
        self.__current_letter = ""
        self.__game_title = ""

        # tkinter objects
        self.__main_window = Tk()
        self.__myfont = font.Font(family="Helvetica", size=16,
                                  weight="bold")
        self.__multiplayer_user_input_field = Entry()
        self.__text_label_during_game = Label(bg="black", fg="white")

        self.__list_length = len(self.__correct_words)
        self.__main_window.configure(bg="black")

        # Window can't be resized because the objects have a static size,
        # i.e they are not responsive
        self.__main_window.resizable(0,0)

        self.generate_random_index_value()

        self.choose_game_type()

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

        # The game_title is placed on top of the window
        self.__game_title = self.__main_window.title("Hangman")

        self.__singleplayer = Button(self.__main_window, text="Singleplayer",
                                     height=50, width=50,
                                     command=self.generate_keyboard)
        # self.__singleplayer = Button(self.__main_window, text="Singleplayer",
        #                              command=self.generate_keyboard)
        self.__singleplayer.grid(row=1, column=0)

        self.__multiplayer = Button(self.__main_window, text="Multiplayer",
                                    height=50, width=50,
                                    command=self.choose_your_own_word)
        self.__multiplayer.grid(row=1, column=2)


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

        self.__random_index_value = randrange(self.__list_length)
        self.__correct_answer = self.__correct_words[self.__random_index_value]

    def check_if_string_is_legal(self):
        """
        The method checks whether a string is legal. The word is legal
        only if it is alphabetic, i.e. doesn't have any numbers or special
        characters in it. The alphabetic check is done using a seperate method
        Calls the gameboard generation method if the word was legal. Doesn't
        take any external parameters, doesn't return anything (returns None
        implicitely). Modifies attribute boolean values instead.
        """

        self.__correct_answer = (
            self.__multiplayer_user_input_field.get().upper())

        if not self.is_alpha(self.__correct_answer):
            self.__multiplayer_user_input_field.configure(bg='red')

        elif len(self.__correct_answer) > MAX_LENGTH_FOR_WORD_TO_BE_GUESSED:
            self.__multiplayer_user_input_field.configure(bg='red')

        # If the program gets here, the word had only letters in it
        else:
            self.__multiplayer_user_input_field.configure(bg='white')

            self.generate_keyboard()
            self.__choose_button.destroy()
            self.__singleplayer.destroy()

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

        self.__multiplayer_user_input_field.grid(row=1, column=1)
        self.__singleplayer.destroy()
        self.__multiplayer.destroy()
        self.__choose_button = Button(self.__main_window, text="Choose",
                                      command=self.check_if_string_is_legal)
        self.__choose_button.grid(row=1, column=2)

    def is_alpha(self, word):
        """
        The method checks whether a string is alphabetic. First the method
        gets the string from a tkinter Entry object. The word is then checked
        with a built-in method of Python class string. Returns a boolean
        based on the answer. Doesn't take any external parameters.
        """

        if not word.isalpha():
            return False

        else:
            return True

    def generate_keyboard(self):
        """
        Generates the keyboard and how it is positioned on the screen. Goes
        through the list that has lists inside of it and creates a keyboard
        from it. Keyboard's buttons are created from the letters in the list.
        """

        for i in self.__correct_answer:
            self.__list_of_correct_letters.append(i)

        letters = [["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "Å"],
                   ["A", "S", "D", "F", "G", "H", "J", "K", "L", "Ö", "Ä"],
                    ["Z", "X", "C", "V", "B", "N", "M"]]

        current_row = 10
        current_column = 1
        for row in letters:
            if current_row == 12:
                current_column = 3

            for char in row:
                self.__new_button = Button(self.__main_window, text=char,
                                           command=self.on_letter_button_click)
                self.__new_button.config(bg="black", fg="white",
                                         font=self.__myfont, height=2, width=2,
                                         command=lambda b=self.__new_button:
                                         self.on_letter_button_click(b))
                self.__new_button.grid(row=current_row + 1,
                                       column=current_column + 1,
                                       sticky="NESW")
                self.__keyboard[char] = self.__new_button
                self.__multiplayer.destroy()
                self.__singleplayer.destroy()
                self.__multiplayer_user_input_field.destroy()
                self.__main_window.columnconfigure(current_column, weight=1)
                self.__main_window.rowconfigure(current_row, weight=1)
                current_column += 1

            # For aesthetics
            current_column = 1
            current_row += 1

        self.check_if_letter_can_be_shown()

    def check_if_letter_can_be_shown(self, i=""):
        """
        This method reveals the clicked letter from the hidden word. It saves
        the letter and its index value by creating tuples. Correctly clicked
        letters can be revealed from the word.
        """

        current_label_row = 10
        current_label_column = 3

        for index, letter in enumerate(self.__correct_answer):
            if letter == i:
                # If the letter is guessed correctly, update the
                # display immediately
                self.__text_label_during_game = Label(self.__main_window,
                                                      text=letter, bg="black",
                                                      fg="white",
                                                      font=("Helvetica", 16))
            elif letter in self.__correct_guesses:
                # If the letter was guessed correctly before, show it as well
                self.__text_label_during_game = Label(self.__main_window,
                                                      text=letter, bg="black",
                                                      fg="white",
                                                      font=("Helvetica", 16))
            else:
                # For letters that have not been guessed yet, display
                # an underscore
                self.__text_label_during_game = Label(self.__main_window,
                                                      text="__", bg="black",
                                                      fg="white",
                                                      font=("Helvetica", 16))
            self.__text_label_during_game.grid(row=current_label_row,
                                               column=current_label_column +
                                                      1)
            current_label_column += 1


        # If a new letter was guessed correctly, add it to the list of correctly
        # guessed letters
        if i not in self.__correct_guesses:
            self.__correct_guesses.append(i)
    def on_letter_button_click(self, button):
        """
        The method is called when a letter is clicked. It iterates over the
        keyboard and checks for the clicked button to disable it (each button
        can be pressed only once). Keeps track of clicked buttons and also
        checks if the game has finished. Takes the button as a object as an
        external parameter, doesn't return anything (returns None implicitely).
        """

        index = ""
        # The loop iterates over the keyboard and searches for the button that
        # was clicked
        for index, btn in self.__keyboard.items():
            # If the current button in a loop matches the clicked button,
            # it will be disabled. Disabling the button turns the font color
            # to grey and makes it impossible to click.
            if btn == button:
                # self.__is_button_clicked = True
                btn["state"] = "disabled"

                # if button in correct_answer, the hanging tree doesn't grow,
                # but the corresponding letter is revealed from the variable
                # correct_answer
                break

        # Checks how many times the clicked letter appears in the word.
        for i in self.__correct_answer:
            if i == index:
                self.__word_appearance_counter += 1

                self.__current_letter = i
                self.check_if_letter_can_be_shown(i)

        # Adds the information of how many times the clicked letter appears
        # in the word that is being guessed, to the variable
        # self.__amount_of_guessed_letters
        self.__amount_of_guessed_letters += \
            self.__word_appearance_counter

        # Checks if the clicked letter was the last letter that wasn't
        # guessed yet.
        self.was_move_a_winning_move()

        if self.__has_word_been_guessed and not self.__has_game_been_lost:
            self.game_won()

        # If variable self.__word_appearance_counter is over zero,
        # it is reset back to zero that the counter can count how many times
        # another letter appears in the word.
        elif self.__word_appearance_counter > 0:
            self.__word_appearance_counter = 0

        else:
            self.__amount_of_mistakes += 1
            self.check_amount_of_mistakes()

    def check_amount_of_mistakes(self):
        """
        Creates a graphic of the hangman according to the player's
        mistakes. Once there is 11 mistakes, the game will end and no more
        letters can be guessed.
        """

        if self.__amount_of_mistakes == FIRST_MISTAKE:
            self.__hangman_graph_label = Label(self.__main_window, text=" "
                                                                        "___",
                                               bg="black", fg="white")
            self.__hangman_graph_label.grid(row=5, column=4)
            # self.__first_image_label.configure(image=self.__first_image)

        elif self.__amount_of_mistakes == SECOND_MISTAKE:
            self.__hangman_graph_label.configure(text=" |     \n"
                                                    " |     \n"
                                                    " |     \n"
                                                    " |     \n"
                                                    " |     \n"
                                                    "   |___  ")

        elif self.__amount_of_mistakes == THIRD_MISTAKE:
            self.__hangman_graph_label.configure(text="  _____ \n"
                                                    " |     \n"
                                                    " |     \n"
                                                    " |     \n"
                                                    " |     \n"
                                                    " |     \n"
                                                    "   |___  ")
        elif self.__amount_of_mistakes == FOURTH_MISTAKE:
            self.__hangman_graph_label.configure(text="  _____  \n"
                                                    " |/     \n"
                                                    " |      \n"
                                                    " |      \n"
                                                    " |      \n"
                                                    " |      \n"
                                                    "   |___   ")

        elif self.__amount_of_mistakes == FIFTH_MISTAKE:
            self.__hangman_graph_label.configure(text="  _____  \n"
                                                    " |/     |\n"
                                                    " |       \n"
                                                    " |       \n"
                                                    " |       \n"
                                                    " |       \n"
                                                    "   |___   ")

        elif self.__amount_of_mistakes == SIXTH_MISTAKE:
            self.__hangman_graph_label.configure(text="  _____   \n"
                                                    " |/      |\n"
                                                    "  |       o\n"
                                                    " |        \n"
                                                    " |       \n"
                                                    " |       \n"
                                                    "  |___  ")

        elif self.__amount_of_mistakes == SEVENTH_MISTAKE:
            self.__hangman_graph_label.configure(text="  _____   \n"
                                                    " |/     |\n"
                                                    "  |       o\n"
                                                    " |       |\n"
                                                    " |        \n"
                                                    " |        \n"
                                                    "  |___   ")

        elif self.__amount_of_mistakes == EIGHTH_MISTAKE:
            self.__hangman_graph_label.configure(text="  _____   \n"
                                                    " |/     |\n"
                                                    "  |       o\n"
                                                    " |      -|\n"
                                                    " |        \n"
                                                    " |        \n"
                                                    " |___  ")

        elif self.__amount_of_mistakes == NINTH_MISTAKE:
            self.__hangman_graph_label.configure(text="  _____    \n"
                                                    " |/     | \n"
                                                    "  |       o \n"
                                                    "  |     -|-\n"
                                                    " |        \n"
                                                    " |        \n"
                                                    " |___  ")

        elif self.__amount_of_mistakes == TENTH_MISTAKE:
            self.__hangman_graph_label.configure(text="  _____    \n"
                                                    " |/     | \n"
                                                    "  |       o \n"
                                                    " |      -|-\n"
                                                    "  |      /  \n"
                                                    " |        \n"
                                                    " |___  ")

        elif self.__amount_of_mistakes == ELEVENTH_MISTAKE:
            self.__hangman_graph_label.configure(text="  _____    \n"
                                                    " |/     | \n"
                                                    "  |       o \n"
                                                    "  |      -|-\n"
                                                    "  |      / \\\n"
                                                    " |         \n"
                                                    " |___   ")
            self.__keyboard["state"] = "disabled"
            self.__has_game_been_lost = True
            self.game_lost()

    def game_won(self):
        """
        Creates a window on top of the main window that has a text indicating
        victory and a button to quit the game. Doesn't take any external
        parameters, doesn't return anything (returns None implicitely).
        """
        end_screen = Toplevel(self.__main_window)
        end_title = Label(end_screen, text="Voitit pelin!",
                          font=("Helvetica", 16))
        quit_button = Button(end_screen, text="Quit",
                             command=self.quit)
        end_title.grid(row=0, column=0)
        quit_button.grid(row=1, column=0)

    def game_lost(self):
        """
        Creates a window on top of the main window that has a text indicating
        victory and a button to quit the game. Doesn't take any external
        parameters, doesn't return anything (returns None implicitely).
        """
        end_screen = Toplevel(self.__main_window)
        end_title = Label(end_screen, text="Hävisit pelin!",
                          font=("Helvetica", 16))
        quit_button = Button(end_screen, text="Quit",
                             command=self.quit)
        end_title.grid(row=0, column=0)
        quit_button.grid(row=1, column=0)

    def was_move_a_winning_move(self):
        """
        Checks if the guessed word was last letter of the entire word that
        is being quessed. If the variable self.__amount_of_guessed_letters
        length is same as the length of the list
        self.__list_of_correct_letters. Changes the variable's
        self.__has_word_been_guessed bool value to true if the variable
        self.__amount_of_guessed_letters length is same as the length of the
        list self.__list_of_correct_letters.
        """
        if self.__amount_of_guessed_letters == len(
                self.__list_of_correct_letters):
            self.__has_word_been_guessed = True

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