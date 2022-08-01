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
        extra_msg = (str(second_v)+' in '+str(first_v))
        print(msg,' ',str(extra_msg))

def checker(first_input,second_input):
    if type(first_input) is int and type(second_input) is int: # int checking
        printer('Both values have type :', 'info', 'int')
        if first_input == second_input:
            printer('Both numbers are:', 'info', first_input)
        elif first_input > second_input:
            printer('The bigger number is:', 'info', first_input)
        else:
            printer('The bigger number is:', 'info', second_input)
    elif type(first_input) is str and type(second_input) is str: # str checking
        printer('Both values have type :', 'info', 'str')
        if first_input.find(second_input) >= 0:
            printer('Substring finded', 'info', first_input,second_input)
        else:
            printer('No substrings finded', 'error')
    else:
        printer('Error values are unsuitable on this task!', 'error')

def get_value(input_value):
    in_value = input(input_value)
    try:
        out_value = int(in_value)
    except:
        out_value = in_value
    finally :
        return out_value

if __name__ == "__main__":
    f_number = get_value('Input first value [a] :')
    l_number = get_value('Input last value [b] :')
    checker(f_number, l_number)