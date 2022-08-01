if __name__ == '__main__':
    user_name = str(input('What is you name traveler?:'))
    if user_name == '':
        print('Okay, stranger - have a good day)')
    else:
        print('Hi, {user_name} !'.format(user_name = user_name))

