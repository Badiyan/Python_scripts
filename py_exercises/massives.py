not_int_values = []
numeric_mass = []

def mass_cleaner(mass):
    for element in mass:
        if type(element) == int or type(element) == float:
            numeric_mass.append(element)
        else:
            not_int_values.append(element)
    return numeric_mass


def sum_mass(mass):
    sum = 0
    for number in mass_cleaner(mass):
        sum += number
    return sum


def max_mass(mass): # also possible to use default max() func
    max_number = mass[0]
    for index, number in enumerate(mass_cleaner(mass)):
        if number > max_number:
            max_number = number
            max_index = index
        else:
            continue
    return max_number,max_index


if __name__ == '__main__':
    mass = [10, 2, 3, 4, 5, 'hello']
    print('Array sum: ',sum_mass(mass))
    print('Not int values: ', not_int_values)
    print('Max number and his index:', max_mass(mass))







