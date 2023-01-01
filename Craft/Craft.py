import os

def print_window(columns,lines,line3text,text):
    for line in range(lines-1):
        for column in range(columns-1):
            if line == 0 and column == 0:
                print("_",end="")
            if line == 0:
                print("_",end="")
            elif line == lines-2:
                if column == 0:
                    print("|",end="")
                elif column == columns-2:
                    print("|")
                else:
                    print("_",end="")
            elif column == 0:
                print("|",end="")
            elif column == columns-2:
                print("|")
            
            else:
                print(" ",end="")


    
def reset_size():
    global win_column
    global win_line
    win_column = os.get_terminal_size().columns
    win_line = os.get_terminal_size().lines

def main():
    reset_size()
    global text
    text = {(10,10):"a"}
    
    print_window(win_column, win_line, "Main Terminal Window", text)

if __name__ == '__main__':
    main()