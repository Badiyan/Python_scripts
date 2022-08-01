def summ_and_multiple():
    try:
        number_one,number_two, number_tree = input('Please input 3 numbers separated by space:').split()
        total = (int(number_one) + int(number_two)) * int(number_tree)
        print('The answer is {total}'.format(total=total))
    except:
        print('Invalid argument given!')

if __name__ == '__main__':
    summ_and_multiple()