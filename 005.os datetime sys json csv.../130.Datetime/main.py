# Datetime

from datetime import datetime

dt1 = datetime.strptime('20/04/1987 20:00:00', '%d/%m/%Y %H:%M:%S')
dt2 = datetime.strptime('25/04/1987 22:33:00', '%d/%m/%Y %H:%M:%S')

print(dt2 > dt1)
