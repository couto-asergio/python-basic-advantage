''' 
    Last Day of Month in Leap Year

    Get the number of days in the month), get last day of month.
    This might not work as expected in a leap year.
    Function mdays to calendar

    You can also use calendar's monthrange function to get the
    number of the day of the week (between 0-6) and last day of
    the month (between 28-31).
'''

from calendar import monthrange
from datetime import datetime

print(monthrange(2020, 2))

dia_semana, ultimo_dia = monthrange(2020, 2)
print(ultimo_dia)


ultimos_dias_de_meses_do_ano_atual = [
    monthrange(datetime.now().year, mes)[1] for mes in range(1, 13)
]
print(ultimos_dias_de_meses_do_ano_atual)
