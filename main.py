from graphics import *

class Game():
    def __init__(self) -> None:
        print("Game Object Initialised")
        # Initialise window
        self.__win = self.__init_win(
            width= 500,
            height= 500
        )
        # Initialise board
        self.__board_obj = self.__init_board(
            win= self.__win
        )
        # Initialise snake
        # Start game loop
        # Close window + destroy objects
        self.__win.getMouse()
        self.__win.close()

    def __init_win(self, width: int, height: int) -> None:
        win = GraphWin("Snake", width, height)
        win.setBackground("#000000")
        return win
    
    def __init_board(self, win: GraphWin):
        return Board(win=win)
    

class Board():
    def __init__(self, win: GraphWin) -> None:
        print("Board Object Initialised")
        self.__win = win
        # Intialise fruit    


if __name__ == "__main__":
    game_obj = Game()
