import banking
import interface
import excelreporting
transactions = banking.get_transactions()
flag = 0


while True:
    if flag == 3:
        print("Terminating the program...")
        break
    elif flag == 0:
        flag = interface.get_option_from_menu()
        print(flag)
    elif flag == 1:
        balances = banking.get_current_funds(transactions)
        for index in balances.keys():
            bank = banking.BANK_NAMES[index[0]]
            card = str(index[1])
            cash = str(balances[index])
            print('Card *' + card + ' ' + bank + ' ' + cash + ' EUR')
        flag = 0
    elif flag == 2:
        date = interface.get_date_by_user()
        card_option = interface.get_card_option()
        spent = 0
        received = 0
        delta = 0
        report = None

        if card_option == len(banking.CARD_MENU_INDEX.keys())+ 2:
            flag = 0
        elif card_option == len(banking.CARD_MENU_INDEX.keys()) + 1:
            for index in banking.CARD_MENU_INDEX.keys():
                bank = banking.CARD_MENU_INDEX[index][0]
                card = banking.CARD_MENU_INDEX[index][1]
                report = banking.get_report(transactions, bank, card, date)
                spent += report['spent']
                received += report['received']
                delta += report['delta']
            print('Total report:')
            print('Spent: ' + str(spent) + ' EUR')
            print('Received: ' + str(received) + ' EUR')
            delta = str(delta)
            if delta[0] not in '-0':
                delta = '+' + delta
            print('Delta: ' + delta + ' EUR')
        else:
            bank = banking.CARD_MENU_INDEX[card_option][0]
            card = banking.CARD_MENU_INDEX[card_option][1]
            report = banking.get_report(transactions, bank, card, date)
            month = interface.get_month(int(date[5:7]))
            print('Report for ' + month + ' ' + date[:4] + ':')
            print('Bank: ' + banking.BANK_NAMES[bank])
            print('Card: *' + str(card))
            print('Spent: ' + str(report['spent']) + ' EUR')
            print('Received: ' + str(report['received']) + ' EUR')
            delta = str(report['received'] - report['spent'])
            if delta[0] not in '-0':
                delta = '+' + delta
            print('Delta: ' + delta + ' EUR')

        check = input('Would you like to get full excel report? y-yes, other-no')
        if check[0] == 'y':
            excelreporting.full_excel_report(transactions, card_option, date)
            print('Your report is saved in xls. Cheers!')

        check = input('Would you like to make new request? y-yes, other-no')
        if check[0] != 'y':
            flag = 0