from datetime import datetime
from datetime import timedelta
from calendar import monthrange
def replace_name(a,с = 2):
	c = 2
	if c == 1:
		if a == 'Родыгин':
			b = 1
		elif a == 'Рощин':
			b = 2
		elif a == 'Русаков':
			b = 3
		elif a == 'Пигин':
			b = 4
		elif a == 'Середнев':
			b = 5
		elif a == 'Брагин':
			b = 6
		elif a == 'Еремин':
			b = 7
		elif a == 'Калякин':
			b = 8
		elif a == 'Манылюк':
			b == 9
		elif a == 'Журавлев':
			b == 0
		else:
			print('Ошибка определения сотрудника')
	else:
		if a == 1:
			b = 'Родыгин'
		elif a == 2:
			b = 'Рощин'
		elif a == 3:
			b = 'Русаков'
		elif a == 4:
			b = 'Пигин'
		elif a == 5:
			b = 'Середнев'
		elif a == 6:
			b = 'Брагин'
		elif a == 7:
			b = 'Еремин'
		elif a == 8:
			b = 'Калякин'
		elif a == 9:
			b = 'Манылюк'
		elif a == 0:
			b = 'Журавлев'
		else:
			print(a)
			print('Ошибка определения сотрудника')
	return b



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

def time_for_excel(data_from_file):
    time = datetime.time(data_from_file)
    print(time)
    return time
