
CRED = '\033[31m'
CGRN = '\033[32m'
CEND = '\033[0m'
c_green = (CGRN,CEND)
c_red = (CRED,CEND)

def colorize(value = 'value not defined',color = c_red):
    return str(value).join(color)



def printer(msg = 'Message not defined', type = 'error',  *args):
    if len(args) == 0:
        if type == 'info':
            print(
                colorize(msg,c_green)
            )
        elif type == 'error':
            print(
                colorize(msg,c_red)
            )
        else:
            print(msg)
    elif len(args) == 1:
        print(msg, colorize(args[0],c_green))
    elif len(args) > 1:
        first_v = colorize(args[0],c_green)
        second_v = colorize(args[1],c_green)
        extra_msg = (second_v,' in ',first_v)
        print(msg,' ',extra_msg)








