import datetime
import calendar
from secondary_func import*
a = datetime.datetime(2018,4,10,6,48,12)
b = datetime.datetime(2018,4,10,17,12,9)

x = b - a

print(type(x),'\n\t',x)

i = datetime.timedelta(hours = 8)

c = int(x) - int(i)

print(type(c),'\n\t',c)
year = 2017
month = 5
last_day = calendar.monthrange(int(year), int(month))[1]
a1 = datetime(int(year), int(month), 1) ;
b1 = datetime(int(year), int(month), last_day)
for dt in daterange(a1, b1, inclusive=True):
  print(dt,'dt')
  date = dt.strftime("%Y-%m-%d")
  print('\n\n\t')
  print(date,'date')
