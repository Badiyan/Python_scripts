odd_numbers = []
CRED = '\033[31m'
CGRN = '\033[32m'
CEND = '\033[0m'

def get_value(input_value):
    while True:
        try:
            value = int(input(input_value)) # possible also use isnumeric() func for checking
        except:
            print('{}Input integer digit only!{}'.format(CRED,CEND))
            continue
        else:
            return value
            break



def odd_check(numbers):
    for number in numbers:
        if (number % 2) == 0 and number != 0:
            odd_numbers.append(number)
    return odd_numbers

if __name__ == "__main__":
    first_number = get_value('Input first number [a] :')
    last_number = get_value('Input last number [b] :')
    if first_number == last_number:
        odd_check(range(first_number,first_number+1))
    elif first_number > last_number:
        odd_check(range(last_number,first_number))
    else:
        odd_check(range(first_number, last_number))
    print(
        '{сolor}On the list from {first_number} to {last_number} exists next odd numbers: \n {odd_numbers}{colorend}'.format(
            сolor = CGRN,
            first_number = first_number,
            last_number = last_number,
            odd_numbers = odd_numbers,
            colorend = CEND
        )
    )
