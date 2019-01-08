from secondary_func import*
from datetime import timedelta
from datetime import datetime
import sys
from calendar import monthrange
def daterange(start, stop, step=timedelta(days=1), inclusive=False):
  if step.days > 0:
    while start < stop:
      yield start
      start = start + step
  elif step.days < 0:
    while start > stop:
      yield start
      start = start + step
  if inclusive and start == stop:
    yield start
full_info = {}
f = open('1','r')
for line in f:
    Y = line[8:29]
    date_and_time = datetime.strptime(line[10:29], "%Y-%m-%d %H:%M:%S")
    date = line[10:20]
#    print(date, 'date')
#    print(date_and_time)
    U = int(Y[0])
    family = replace_name(U)
    if not  date in full_info.keys():
        full_info[date] = {}
    if U in full_info[date].keys():
        if full_info[date][U][0] < date_and_time:
            full_info[date][U][0] = date_and_time
        if full_info[date][U][1] > date_and_time:
            full_info[date][U][1] = date_and_time
    else:
        full_info[date][U] = [date_and_time, date_and_time]
number_family = [1,2,3,4,5,6,7,8]
op = open('y','w')
op.write(str(full_info))
op.close()
year = input("Get a year: ")
month = input("Get a month: ")
last_day = monthrange(int(year), int(month))[1]
a = datetime(int(year), int(month), 1)
b = datetime(int(year), int(month), last_day)
#print(full_info)
for dt in daterange(a, b, inclusive=True):
  date = dt.strftime("%Y-%m-%d")
  if date in full_info.keys():
    for i in full_info[date].keys():
      name = replace_name(i)
      #print(name + ": start time " + full_info[date][i][0].strftime("%Y-%m-%d %H:%M:%S") + ", finish time " + full_info[date][i][1].strftime("%Y-%m-%d %H:%M:%S"))
      if name != 'Рощин':
        if full_info[date][i][0] == full_info[date][i][1]:
          print("AHTUNG! " + name + " have only one fingerprint", file=sys.stderr)
          print('Фамилия', name)
          print('Дата время в системе',full_info[date][i][0])
          print('\n\n\tВыберете вариант:\n\n\t1.Ввести время прихода\n\t2.Введите время ухода')
          l = 0
          while l!=1:
            time_inp = input('\n\n\tВведите пункт меню:')
            if time_inp == '1' or time_inp == '2':
              l = 1
              if time_inp == '1':
                time_begin = input('Введите время прихода в формате час*ПРОБЕЛ*минуты*секунды(если есть)')
                time_begin_str = date + ' ' + time_begin
                time_begin_z = datetime.strptime(time_begin_str,"%Y-%m-%d %H %M %S")
              elif time_inp == '2': 
                time_end = input('Введите время ухода в формате час*ПРОБЕЛ*минуты*секунды(если есть)')
                time_end_str = date + ' ' + time_end
                time_end_z = datetime.strptime(time_end_str,"%Y-%m-%d %H %M %S")
              else:
                pass
          else:
            print('Введите правильный пункт меню!')
      else:
        pass
print('FINAL!')
