def get_numbers():
    numbers = input('Please input 3 numbers separated by space:').split()
    return numbers

def math_operation(numbers):
    try:
        first_num = float(numbers[0])
        second_num = float(numbers[1])
        third_num = float(numbers[2])
        result = (first_num + second_num) * third_num
        print('The answer is {result}'.format(result=result))
    except:
        print('Invalid argument given!')

if __name__ == '__main__':
    math_operation(get_numbers())