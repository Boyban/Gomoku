import sys

class ai:

    def __init__(self, size):
        self.board_size = size
        self.board = []


def cmd_handling(cmd):
    try:
        if cmd.split(' ')[5:] == "START":
            print("start")
    except ValueError:
        print("NIKOUMOUK TU MENVOIE DLA KOBA LA D")

def main():
    sys.exit(0)

if __name__ == "__main__":
    main()