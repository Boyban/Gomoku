import sys 

class ai:

    def __init__(self, size):
        self.board_size = size
        self.board = []

def start_function(cmd):
    if len(cmd) != 2:
        print("UNKNOW")
    print("start_function")

def begin_function():
    print("begin_function")

def turn_function(cmd):
    if len(cmd) != 3:
        print("UNKNOW")
    print("turn_function")

def board_function():
    print("board_function")

def info_function(cmd):
    if len(cmd) != 3:
        print("UNKNOW")
    print("info_function")

def end_function():
    print("end_function")

def about_function():
    print("about_function")

def cmd_handling(line):
    no_param_dic = { "BEGIN" : begin_function,
    "BOARD" : board_function, 
    "END" : end_function,
    "ABOUT" : about_function }

    param_dic = { "START" : start_function,
    "TURN" : turn_function,
    "INFO" : info_function }

    try:
        cmd = line.split(' ')
        if cmd[0].upper() in no_param_dic and len(cmd) != 1:
            print("UNKNOW")
        elif cmd[0].upper() in no_param_dic:
            no_param_dic[cmd[0].upper()]()
        if cmd[0].upper() in param_dic and (len(cmd) < 2 or len(cmd) > 3):
            print("UNKNOW")
        elif cmd[0].upper() in param_dic:
            param_dic[cmd[0].upper()](cmd)
    except ValueError:
        print("NIKOUMOUK TU MENVOIE DLA KOBA LA D")
        sys.exit(84)

def main():
    while 1:
        line = input()
        cmd_handling(line)
    sys.exit(0)

if __name__ == "__main__":
    main()