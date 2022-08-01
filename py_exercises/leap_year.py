list_exept_years = [1756,1921,1943,2001,2012,2020,2050,2055]
leap_years = []
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


def add_exept_year(i_val):
    while True:
        try:
            list_exept_years.append(int(input(i_val)))
        except:
            print('{}Input integer digit only!{}'.format(CRED,CEND))
            continue
        else:
            break

def year_dialog():
    while True:
        print('List of exeption years:', list_exept_years)
        answer = input('Add more exeption year? y/n ')
        if answer == 'y' or answer == 'n':
            if answer == 'y':
                add_exept_year('Input year value wich you wnat to add:')
                continue
            else:
                print('List of exeption years:', list_exept_years)
                break
        else:
            print('Choose "y" or "n" answer')
            continue

def leap_year_check(years):
    for year in years:
        print(year)
        except_check = year in list_exept_years
        print(except_check)
        if except_check == False:
            if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
                leap_years.append(year)
            else:
                continue
        else:
            continue

if __name__ == '__main__':
    first_year = get_value('Input first of years list [a] :')
    last_year = get_value('Input last years list [b] :')
    year_dialog()
    if first_year == last_year:
        leap_year_check(range(first_year, first_year + 1))
    elif first_year > last_year:
        leap_year_check(range(last_year, first_year))
    else:
        leap_year_check(range(first_year, last_year))
    print(
        '{сolor}On the list of years from {first_year} to {last_year} \n Except next years: {list_exept_years} \n Exists next leap years: \n {leap_years}{colorend}'.format(
            сolor=CGRN,
            first_year=first_year,
            last_year=last_year,
            list_exept_years = list_exept_years,
            leap_years=leap_years,
            colorend=CEND
        )
    )







