"""
COMP.CS.100 Ohjelmointi 1 / Programming 1

Example: 15 game
"""

from tkinter import *

# By changing this constant the game board will
# automatically scale to a smaller or larger dimensions.
SIZE = 4


class GameGUI:
    def __init__(self):
        self.__mainw = Tk()
        self.__mainw.title(f"{SIZE**2 - 1} Game")
        self.__mainw.option_add("*Font", "Verdana 36")

        quit_button = Button(self.__mainw, text="Quit", command=self.quit)
        quit_button.grid(row=SIZE, column=0, columnspan=SIZE, sticky=W+E)

        # The following loop will initialize the two lists __buttons
        # and __commands to be SIZE×SIZE matrices (lists within a list)
        # with all elements initialized as None.  These two lists
        # will contain bookkeeping information about locations of
        # the game's push buttons and command functions connected
        # to a button in a particular location on the board.
        self.__buttons = [ ]
        self.__commands = [ ]
        for row in range(SIZE):
            self.__buttons.append([None] * SIZE)
            self.__commands.append([None] * SIZE)

        # In the beginning of the game the empty place is on
        # the bottom right corner of the game board i.e. on the
        # coordinates (SIZE - 1, SIZE - 1).
        self.__empty_y_coord = SIZE - 1
        self.__empty_x_coord = SIZE - 1

        # Lets generate SIZE * SIZE command-functions and
        # SIZE * SIZE - 1 push buttons, store the information
        # about them in the lists __buttons and __commands.
        # The buttons will also be placed on the game board.
        slate_number = 1
        for y in range(SIZE):
            for x in range(SIZE):
                # The command function to handle a button press on
                # game piece in coordinates (y, x).
                def button_press(button_y_coord=y, button_x_coord=x):
                    self.move_slate(button_y_coord, button_x_coord)

                # The defined function needs to be stored for later use
                # in the move_slate method.
                self.__commands[y][x] = button_press

                # The last game piece is not created since there
                # needs to be an empty place on the board.
                if y == SIZE - 1 and x == SIZE - 1:
                    break

                # The new button in placed on coordinated (y, x) and
                # its command function is the one defined earlier
                # which gets as its parameter the location (y, x) of the
                # button when clicked.
                new_button = Button(self.__mainw,
                                    text=slate_number,
                                    width=3,
                                    heigh=2,
                                    command=button_press)

                # The newly created button is also stored into
                # the bookkeeping matrix.
                self.__buttons[y][x] = new_button

                # The button's location in the beginning of the game
                # is at coordinates (y, x).
                new_button.grid(row=y, column=x)

                slate_number += 1

        self.__mainw.mainloop()

    def move_slate(self, y, x):
        """
        When a button on the game board is clicked, we will end up
        here.  The parameters y and x contain the coordinated of the
        button which was clicked. That button (i.e. game piece) should
        move to the empty position if possible.
        """

        # Helper variables to make the code easier to understand.
        activated_button = self.__buttons[y][x]
        target_y = self.__empty_y_coord
        target_x = self.__empty_x_coord

        # If the clicked plate is not by the empty space, move
        # is not possible, we don't even need to try it.
        if abs(y - target_y) > 1 or abs(x - target_x) > 1 \
             or (abs(y - target_y) == 1 and abs(x - target_x) == 1):
            return

        # Move the button on the user interface where the empty space was.
        activated_button.grid(row=target_y, column=target_x)

        # Update the moved buttons command so that the next time it
        # is clicked, the command function handling the button in the
        # new coordinates will be called.
        activated_button.configure(command=self.__commands[target_y][target_x])

        # Update the bookkeeping information for the button locations.
        self.__buttons[target_y][target_x] = activated_button
        self.__buttons[y][x] = None

        # Update the bookkeeping information for the empty space's location.
        self.__empty_y_coord = y
        self.__empty_x_coord = x

    def quit(self):
        self.__mainw.destroy()


def main():
    gamegui = GameGUI()


if __name__ == "__main__":
    main()
