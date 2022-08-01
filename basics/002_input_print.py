
def get_name():
    user_name = str(input(
                          'What is you name traveler?:'
    ))
    if user_name == '':
        return 'John'
    else:
        return user_name


def get_surname():
    user_surname = str(input(
        'Ok) Good, and what is you surname?:'
    ))
    if user_surname == '':
        return 'Doe'
    else:
        return user_surname

def print_greating(name = str,surname = str):
    print(
        'Hi, {user_name} {user_surname} !'.format(
            user_name = name,
            user_surname = surname
        ))


if __name__ == '__main__':
    print_greating(get_name(),get_surname())