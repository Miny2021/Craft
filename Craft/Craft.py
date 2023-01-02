import os
import time
firsttext="Please Wait |"
for i in range(int((os.get_terminal_size().columns-len(list(firsttext)))/5)):
    firsttext += "-"
    time.sleep(0.01)
    print(f"{firsttext}\r",end="")
def print_window(columns,lines,texts):
    printed_space = True
    for line in range(lines-1):
        for column in range(columns-1):
            for text in texts.items():
                if line == text[0][0]:
                    if column == text[0][1]:
                        printed_space = False
                        if printed_space == False:
                            print(text[1][:1],end="")
            if line == 0 and column == 0:
                printed_space = False
                print("_",end="")
            if line == 0:
                printed_space = False
                print("_",end="")
            elif line == lines-2:
                printed_space = False
                if column == 0 or column == columns - int(columns * 0.2):
                    print("|",end="")
                elif column == columns-2:
                    print("|")
                else:
                    print("_",end="")
            elif column == 0 or column == columns - int(columns * 0.2):
                printed_space = False
                print("|",end="")
            elif column == columns-2:
                printed_space = False
                print("|")

            if printed_space:
                print(" ",end="")
            printed_space = True
for i in range(int((os.get_terminal_size().columns-len(list(firsttext)))/5)):
    firsttext += "-"
    time.sleep(0.01)
    print(f"{firsttext}\r",end="")

    
def reset_size():
    global win_column
    global win_line
    win_column = os.get_terminal_size().columns
    win_line = os.get_terminal_size().lines
for i in range(int((os.get_terminal_size().columns-len(list(firsttext)))/5)):
    firsttext += "-"
    time.sleep(0.01)
    print(f"{firsttext}\r",end="")
def command_if(cmd):
    None
for i in range(int((os.get_terminal_size().columns-len(list(firsttext)))/5)):
    firsttext += "-"
    time.sleep(0.01)
    print(f"{firsttext}\r",end="")
def main():
    reset_size()
    global text
    global run
    text = {}
    run = True
    while run:
        os.system("cls")
        print_window(win_column, win_line, text)
        command = input("> ")
        
        if command == "exit":
            run = False
        command_if(command)
for i in range(int((os.get_terminal_size().columns-len(list(firsttext)))/5+26)):
    firsttext += "-"
    time.sleep(0.01)
    print(f"{firsttext}\r",end="")
if __name__ == '__main__':

    main()