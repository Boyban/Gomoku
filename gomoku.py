import sys 

class ai:

    def __init__(self, size):
        self.board_size = size
        self.board = []

def start_function(cmd):
    if len(cmd) != 2:
        print("ERROR bad START parameter")
    else:
        try:
            int(cmd[1])
        except ValueError:
            print("ERROR bad START parameter")
            return
        print("OK")

def begin_function():
    print("begin_function")

def turn_function(cmd):
    if len(cmd) != 3:
        print("ERROR bad coordinates")
    else:
        try:
            int(cmd[1])
            int(cmd[2])
        except ValueError:
            print("ERROR bad coordinates")
            return
        print(cmd)
        print("turn_function")

def board_function():
    print("board_function")

def info_function(cmd):
    if len(cmd) != 3:
        print("UNKNOW")
    else:
        try:
            int(cmd[1])
            int(cmd[2])
        except ValueError:
            print("UNKNOW")
            return
        print(cmd)
        print("info_function")

def end_function():
    print("end_function")

def about_function():
    print("about_function")

def cmd_handling(line):
    no_param_dic = {
        "BEGIN" : begin_function,
        "BOARD" : board_function, 
        "END" : end_function,
        "ABOUT" : about_function }

    param_dic = {
        "START" : start_function,
        "TURN" : turn_function,
        "INFO" : info_function }

    try:
        cmd = line.split(' ')
        if cmd[0].upper() in no_param_dic:
            no_param_dic[cmd[0].upper()]()
        elif cmd[0].upper() in param_dic:
            param_dic[cmd[0].upper()](cmd)
        else:
            print("UNKOWN command")
    except ValueError:
        print(ValueError)
        sys.exit(84)

def main():
    while 1:
        line = input()
        cmd_handling(line)
    sys.exit(0)

if __name__ == "__main__":
    main()