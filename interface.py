import banking


def get_month(month_number):
    months = ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December']

    return months[month_number - 1]


def check_month_year_validness(date):
    year = int(date[:4])
    month = int(date[5:])
    return 1 <= month <= 12 and year > 0


def check_month_year_format(date):
    if len(date) != 7:
        return False
    for i in range(len(date)):
        if i == 4 and date[i] != '-':
            return False
        elif i != 4 and date[i] not in '0123456789':
            return False
    return True


def check_number_correct(number):
    for x in number:
        if x not in '0123456789':
            return False
    return True


def get_date_by_user():
    while True:
        s = input('Give a date in format YYYY-MM:')
        if not check_month_year_format(s):
            print('Wrong format!')
        elif not check_month_year_validness(s):
            print('Uncorrect date!')
        else:
            return s


def get_option_from_menu():
    option = -5
    while True:
        print('Select an option number:')
        print('1: Current funds')
        print('2: Monthly report')
        print('3: Exit')
        option = input('Your choice:').rstrip()
        if check_number_correct(option):
            option = int(option)
        else:
            option = -5

        if 1 <= option <= 3:
            return option
        else:
            print('Wrong choice! Please, try again.')


def get_card_option():
    option = -5
    size = len(banking.CARD_MENU_INDEX.keys())
    while True:
        print('Select card number:')
        for index in banking.CARD_MENU_INDEX.keys():
            card = banking.CARD_MENU_INDEX[index][1]
            bank = banking.BANK_NAMES[banking.CARD_MENU_INDEX[index][0]]
            print(str(index) + ': *' + str(card) + ' ' + bank)
        print(size + 1, ': All cards')
        print(size + 2, ': Back to the main menu')
        option = input('Your choice:').rstrip()
        if check_number_correct(option):
            option = int(option)
        else:
            option = -5

        if 1 <= option <= size + 2:
            return option
        else:
            print('Wrong choice! Please, try again.')
