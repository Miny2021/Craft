import os
def print_screen(texts,msg):
    columns = os.get_terminal_size().columns+1
    lines = os.get_terminal_size().lines
    msg = msg[:columns-3]
    msgforlong = 0
    umsgforlong = 0
    for line in range(1,lines):
        for column in range(1,columns):
            space=True
            pntmsg = True
            if (line == 1 or line == lines-1) and column != 1 and column !=columns-1:
                print('=',end='')
                space = False
                pntmsg = False
            if column == 1 or column == columns-1:
                print('|',end='')
                space = False
                pntmsg = False
            if line == lines-3 and column != 1 and column !=columns-1:
                print('-',end='')
                space = False
                pntmsg = False
            if msg != '' and column != 1 and column !=columns-1:
                if line == lines-2:
                    if column == 2:
                        print(msg,end='')
                        msglong=len(list(msg))
                    if msgforlong < msglong:
                        space = False
                        pntmsg = False
                        msgforlong +=1
            for text in texts.items():
                if column == text[0][0] and pntmsg:
                    if line == text[0][1]:
                        print(text[1][:1],end='')
                        space = False
            if space:
                print(' ',end='')
                space=True                                   
def main():
    msg = 'Welcome for used!'
    texts = {}
    while True:
        if os.name == 'posix':
            os.system('clear')
        if os.name == 'nt':
            os.system('cls')
        print_screen(texts,msg)
        command = input('>')
        msg = ''
        if command[:9] == '/setblock':
            try:
                cmd = command.split()
                texts[int(cmd[1]),int(cmd[2])]=cmd[3]
                msg = 'setblock'
            except:
                msg = 'The command of you input has got a error.'
        if command[:4] == '/del':
            try:
                cmd = command.split()
                if (int(cmd[1]),int(cmd[2])) in texts.keys():
                    del texts[(int(cmd[1]),int(cmd[2]))]
            except:
                msg = 'The command of you input has got a error.'
        if command[:5] == '/list':
            msg = str(texts)
        else:
            msg = command
main()