import sys
from random import randint


class ai:

    def __init__(self):
        self.board = []
        self.size = 0
        self.last_move = tuple((-1, -1))
        self.direction = -1  # 1 = up, 2 = right, 3 = down, 4 = left

    def reset(self):
        self.__init__()

    def init_board(self, size):
        self.size = size
        for x in range (0, size):
            self.board.append([])
            for c in range(0, size):
                self.board[x].append(0)

    def set_move(self, x, y, dir):
        self.last_move = (x, y)
        self.direction = dir

    def set_status_case(self, x, y, player):
        self.board[x][y] = player

    def can_playup(self, x, y):
        if x - 4 <= 0:
            return False
        if self.board[x - 1][y] != 2 and self.board[x - 2][y] != 2 and self.board[x - 3][y] != 2 and self.board[x - 4][y] != 2:
            return True
        return False

    def can_playright(self, x, y):
        if y + 4 >= self.size:
            return False
        if self.board[x][y + 1] != 2 and self.board[x][y + 2] != 2 and self.board[x][y + 3] != 2 and self.board[x][y + 4] != 2:
            return True
        return False

    def can_playdown(self, x, y):
        if x + 4 <= self.size:
            return False
        if self.board[x + 1][y] != 2 and self.board[x + 2][y] != 2 and self.board[x + 3][y] != 2 and self.board[x + 4][y] != 2:
            return True
        return False

    def can_playleft(self, x, y):
        if y - 4 <= 0:
            return False
        if self.board[x][y - 1] != 2 and self.board[x][y - 2] != 2 and self.board[x][y - 3] != 2 and self.board[x][y - 4] != 2:
            return True
        return False

    def find_new_move(self):
        x = -1
        y = -1
        dir = -1
        t = []
        for x in range(0, self.size):
            for y in range(0, self.size):
                if self.board[x][y] == 1:
                    if self.can_playup(x, y):
                        t.append(x - 1)
                        t.append(y)
                        t.append(1)
                        return t
                    if self.can_playright(x, y):
                        t.append(x)
                        t.append(y + 1)
                        t.append(2)
                        return t
                    if self.can_playdown(x, y):
                        t.append(x + 1)
                        t.append(y)
                        t.append(3)
                        return t
                    if self.can_playleft(x, y):
                        t.append(x)
                        t.append(y - 1)
                        t.append(4)
                        return t
        while True:
            xrand = randint(0, self.size - 1)
            yrand = randint(0, self.size - 1)
            if self.board[xrand][yrand] == 0:
                if self.can_playup(xrand, yrand):
                    t.append(xrand - 1)
                    t.append(yrand)
                    t.append(1)
                    return t
                if self.can_playright(xrand, yrand):
                    t.append(xrand)
                    t.append(yrand + 1)
                    t.append(2)
                    return t
                if self.can_playdown(xrand, yrand):
                    t.append(xrand + 1)
                    t.append(yrand)
                    t.append(3)
                    return t
                if self.can_playleft(xrand, yrand):
                    t.append(xrand)
                    t.append(yrand - 1)
                    t.append(4)
                    return t

    def need_defense(self, x, y):
        return False

    def play(self):
        x = -1
        y = -1
        dir = self.direction

        if self.direction == 1 and self.board[self.last_move[0] - 1][self.last_move[1]] == 0:
            x =  self.last_move[0] - 1
            y =  self.last_move[1]
        elif self.direction == 2 and self.board[self.last_move[0]][self.last_move[1] + 1] == 0:
            x =  self.last_move[0]
            y =  self.last_move[1] + 1
        elif self.direction == 3 and self.board[self.last_move[0] + 1][self.last_move[1]] == 0:
            x = self.last_move[0] + 1
            y = self.last_move[1]
        elif self.direction == 4 and self.board[self.last_move[0]][self.last_move[1] - 1] == 0:
            x = self.last_move[0]
            y = self.last_move[1] - 1
        else:
            data = self.find_new_move()
            x = data[0]
            y = data[1]
            dir = data[2]
        self.set_move(x, y, dir)
        self.set_status_case(x, y, dir)
        print(str(x)+","+str(y))



def start_function(cmd):
    global basic_ai

    if len(cmd) != 2:
        print("ERROR message - unsupported size or other error")
    else:
        try:
            size = int(cmd[1])
            basic_ai.init_board(size)
            print("OK")
        except ValueError:
            print("ERROR message - unsupported size or other error")
            return

def begin_function():
    global basic_ai

    basic_ai.set_move(0, 0, 3)
    basic_ai.set_status_case(0, 0, 1)
    print("0,0")

def turn_function(cmd):
    global basic_ai

    if len(cmd) != 2:
        print("ERROR bad coordinates")
    else:
        try:
            n = cmd[1].split(',')
            x = int(n[0])
            y = int(n[1])
            basic_ai.set_status_case(x, y, 2)
            if not basic_ai.need_defense(x, y):
                basic_ai.play()
        except ValueError:
            print("ERROR bad coordinates")
            return

def board_function(cmd):
    global basic_ai

    if cmd[0] == "BOARD":
        return
    elif cmd[0] == "DONE":
        print("9,9")
        return
    number = cmd[0].split(',')
    try:
        x = int(number[0])
        y = int(number[1])
        player = int(number[2])
        basic_ai.set_status_case(x, y, player)
    except ValueError:
        print(ValueError)

def info_function(cmd):
    global basic_ai

    return

def end_function():
    global basic_ai

    basic_ai.reset()
    sys.exit(0)

def about_function():
    print("name=\"GOMOKENBrain\", version=\"1.0\", author=\"GOMOKENTeam\", country=\"USA\"")

def cmd_handling(line):
    no_param_dic = {
        "BEGIN": begin_function,
        "END": end_function,
        "ABOUT": about_function
    }

    param_dic = {
        "START": start_function,
        "TURN": turn_function,
        "BOARD": board_function,
        "INFO": info_function
    }
    global board

    line = line.upper()
    try:
        cmd = line.split(' ')
        if cmd[0] == "BOARD":
            board = True
        if cmd[0].upper() in no_param_dic:
            no_param_dic[cmd[0].upper()]()
        elif cmd[0].upper() in param_dic or board:
            param_dic[cmd[0].upper()](cmd)
        else:
            print(cmd[0])
        if cmd[0] == "DONE" and board:
            board = False
    except ValueError:
        print(ValueError)
        sys.exit(84)

def main():
    basic_ai.init_board(19)
    while 1:
        line = input()
        cmd_handling(line)
    sys.exit(0)


basic_ai = ai()
board = False

if __name__ == "__main__":
    main()