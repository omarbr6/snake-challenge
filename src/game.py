import itertools

class Board:
    
    def __init__(self, ncols, nrows):
        self.rows = nrows # Number of board rows
        self.cols = ncols # Number of board columns
        self.board = [[0 for col in range(self.cols)] for row in range(self.rows)] # Initialize board with zeroes. 0 means empty, 1 means snake spot.

    def __str__(self):
        return '\n'.join(' | '.join(map(str, row)) for row in self.board)  # str method to see snake moves

    def getBoard(self):
        return [self.rows, self.cols]

    def snakeInBoard(self, snake): #Method to insert snake positions into board.
        self.board = [[0 for col in range(self.cols)] for row in range(self.rows)] #Reset board before inserting new snake

        coln = 0
        while coln <= self.cols:
            for row in range(self.rows):
                for i in reversed(range(snake.length)):
                    if coln == snake.snake[i][0] and row == snake.snake[i][1]:
                        self.board[row][coln] = 1
                        break

            coln+=1

        print(self)


class Snake:

    def __init__(self, initial_config):
        self.snake = initial_config
        self.length = len(self.snake)
        self.head = initial_config[0] #Define snake's head, it will lead the moves.


class Game:

    def __init__(self, board, snake, depth): #Game class includes the board and the snake.
        self.board = board
        self.initial_snake = snake
        self.snake = snake
        self.depth = depth
        self.moves = ['L', 'R', 'U', 'D']
        self.board.snakeInBoard(self.snake)

    def move(self, dir): #Method to define one single move of the snake attribute in the board attribute based on LRUD movements. Returns 'True' if movement is valid, if not it returns 'False'

        #Depending on the direction, we define the new head of the snake

        if dir == 'L':
            print("Moving LEFT:")
            new_head = [sum(x) for x in zip(snake.head, [-1, 0])]

        elif dir == 'R':
            print("Moving RIGHT:")
            new_head = [sum(x) for x in zip(snake.head, [1, 0])]

        elif dir == 'U':
            print("Moving UP:")
            new_head = [sum(x) for x in zip(snake.head, [0, -1])]

        elif dir == 'D':
            print("Moving DOWN:")
            new_head = [sum(x) for x in zip(snake.head, [0, 1])]

        else:
            print("Not supported direction.")
            return False

        try:
            if self.board.board[new_head[1]][new_head[0]] == 1:  #Check if cell is not '1' in order to avoid snake intersection
                print("Illegal move.")
                return False

            elif (new_head[0] not in range(0, board.cols)) or (new_head[1] not in range(0, board.rows)): #Avoid out of board bouds
                print("Illegal move.")
                return False

            else: #If there is no snake intersection and we are in board's bounds, we insert the new head in the first position of the snake list and we remove the tail, in order to simulate the snake's movement.
                self.snake.snake.insert(0, new_head)
                self.snake.head = new_head
                self.snake.snake.pop()

                self.board.snakeInBoard(self.snake) #Print snake after movement into board.
                return True
        except:
            print("Illegal move: out of bounds")
            return False


if __name__ == "__main__":
    board = Board(4, 3)
    snake = Snake([[2,2], [3,2], [3,1], [3,0], [2,0], [1,0], [0,0]])
    depth = 3

    game = Game(board, snake, depth)

    possibleCombinations = [p for p in itertools.product(game.moves, repeat=game.depth)] # We define a list with all the permutations of length "depth" for the LRUD values, allowing repetition

    validCombinations = 0 # Number of valid combinations definition

    for combination in range(len(possibleCombinations)): # For each comination in possibleCombinations list
        #Reset game for each combination of movements
        
        board = Board(4, 3)
        snake = Snake([[2,2], [3,2], [3,1], [3,0], [2,0], [1,0], [0,0]])
        depth = 3
        play = True

        game = Game(board, snake, depth)

        for i in range(game.depth): # For each movement of each combination, we try the move
            play = game.move(possibleCombinations[combination][i])
            if(not play): # Check if movement is valid
                break
            else:
                print(i)
                print(play)
                if i == game.depth-1: #Once we have a 'depth' number of consecutive movements, we sum one to the valid combinations.
                    validCombinations+=1
                    print("CORRECT COMBINATION!!!")

    print("Number of valid combinations: " + str(validCombinations))
