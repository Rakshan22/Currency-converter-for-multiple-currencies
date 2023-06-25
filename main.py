from currency_converter import CurrencyConverter
from datetime import date
amount = int(input('Enter the amount of money you want to convert: '))
code1 = input('Enter the code of the first currency: ')
code2 = input('Enter the code of the second currency: ')
input_date = input('If you want the rate for a particular date then type yes or no: ')
if input_date == 'yes':
    day = int(input('Enter the day: '))
    month = int(input('Enter the month: '))
    year = int(input('Enter the year: '))
    c = CurrencyConverter()
    conversion = c.convert(amount, code1, code2, date=date(year, month, day))
    print(int(conversion))
elif input_date == 'no':
    c = CurrencyConverter()
    conversion = c.convert(amount, code1, code2)
    print(int(conversion))
else:
    print('Invalid input')
