bill = float(input('Bill: '))

def tip(bill):
    tipCalculated = False
    while tipCalculated == False:
        service = input('Was the service bad, okay, good, or great? ')
        if service == 'great':
            tipAmount = 0.25 * bill
            tipCalculated = True
        elif service == 'good':
            tipAmount = 0.2 * bill
            tipCalculated = True
        elif service == 'okay':
            tipAmount = 0.15 * bill
            tipCalculated = True
        elif service == 'bad':
            tipAmount = 0
            tipCalculated = True
        else:
            print('Please type in either "great", "good", "okay", or "bad".')
    print(f'Tip: {round(tipAmount)}')

tip(bill)