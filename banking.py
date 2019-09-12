SUPER_BANK_CODE = 480
GORGEOUS_BANK_CODE = 720
CARDS = {
    SUPER_BANK_CODE: (2662, 5469),
    GORGEOUS_BANK_CODE: (2435, 8788, 3400)
}

BANK_NAMES = {
    GORGEOUS_BANK_CODE: 'GorgeousBank',
    SUPER_BANK_CODE: 'SuperBank'
}

CARD_MENU_INDEX = {
    1: (SUPER_BANK_CODE, 2662),
    2: (SUPER_BANK_CODE, 5469),
    3: (GORGEOUS_BANK_CODE, 2435),
    4: (GORGEOUS_BANK_CODE, 8788),
    5: (GORGEOUS_BANK_CODE, 3400)
}


def get_transactions(filename='messages.txt'):
    fin = open(filename, 'r')
    messages = fin.readlines()
    transactions_list = []

    for i in range(len(messages)):
        if messages[i][-1] == '\n':
            messages[i] = messages[i][:-1]

        msg = messages[i].split()
        #print(msg)
        date = msg[-2] + ' ' + msg[-1]
        year = int(date[:4])
        month = int(date[5:7])
        day = int(date[8:10])
        hour = int(date[11:13])
        minute = int(date[14:16])
        second = int(date[17:])

        elem_date = (year, month, day, hour, minute, second)

        if int(msg[0]) != SUPER_BANK_CODE and int(msg[0]) != GORGEOUS_BANK_CODE:
            continue

        bank = int(msg[0])
        card = 0
        delta = 0

        if bank == GORGEOUS_BANK_CODE:
            delta = int(msg[2])
            card = int(msg[1][1:-1])
        elif msg[1] == 'Перевод:':
            delta = int(msg[4])
            card = int(msg[3][1:-1])
        else:
            delta = -int(msg[5])
            card = int(msg[4][1:-1])

        balance = 0

        for j in range(len(msg)):
            if msg[j] == 'баланс:':
                balance = int(msg[j + 1])
                break

        transactions_list.append((bank, card, delta, balance, elem_date))

    fin.close()

    return sorted(transactions_list, key=lambda x: x[-1])


def get_current_funds(transactions):
    calc_flag = 0
    was = {}
    balances = {}
    for key in CARDS.keys():
        for num in CARDS[key]:
            was[(key, num)] = balances[(key, num)] = 0

    count = len(CARDS[SUPER_BANK_CODE]) + len(CARDS[GORGEOUS_BANK_CODE])

    for i in range(len(transactions) - 1, -1, -1):
        if was[(transactions[i][0], transactions[i][1])]:
            continue
        else:
            was[(transactions[i][0], transactions[i][1])] = True
            calc_flag += 1
            balances[(transactions[i][0], transactions[i][1])] = transactions[i][3]

        if calc_flag == count:
            break

    return balances


def right_transaction(trans, bank, card, date):
    year = int(date[:4])
    month = int(date[5:])
    date_trans = trans[-1]

    return year == date_trans[0] and month == date_trans[1] and bank == trans[0] and card == trans[1]


def get_report(transactions, bank, card, date):
    year = int(date[:4])
    month = int(date[5:])
    spent = received = 0
    for curr in transactions:
        if right_transaction(curr, bank, card, date):
            if curr[2] > 0:
                spent += curr[2]
            else:
                received -= curr[2]

    ans = {
        'spent': spent,
        'received': received,
        'delta': received - spent
    }

    return ans
