from board import GameBoard


def create_game():
    game = GameBoard()
    if game.restart:
        create_game()


if __name__ == "__main__":
    create_game()
