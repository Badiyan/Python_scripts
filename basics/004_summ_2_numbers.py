def summ_numbers():
    try:
        number_one,number_two = input('Please input 2 numbers separated by space:').split()
        total = int(number_one) + int(number_two)
        print('The total is {total}'.format(total=total))
    except:
        print('Invalid argument given!')

if __name__ == '__main__':
    summ_numbers()