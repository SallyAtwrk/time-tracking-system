import datetime
import calendar
import time

#a = datetime.datetime(2018,4,10,6,48,12)
#b = datetime.datetime(2018,4,10,12,12,9)

#x = (b - a).seconds

#print(type(x),'\n\t',x)

#i = datetime.timedelta(hours = 8)

#c = x - i.seconds
#print(type(c),'\n\t',c,'\n\t',abs(c))


now = datetime.datetime.now()

then = datetime.datetime(2018,3,10)

delta = now - then
print(delta.days)

o1 = calendar.monthrange(2018,5)
print(o1)


for yy in range(2000,2021):
        for j in range(1,13):
                print('Год   ',yy,'   ','Месяц  ',j,'  ',calendar.monthrange(yy,j))


tmp_time_seconds = 342444
h = time.strftime('%H:%M:%S',time.gmtime(tmp_time_seconds))
print(h)
i1 = 32423
i2 = 3600
k2 = i1/i2
k = 7.8934343425234243424
l = round(k2,2)
print(l,'    ',k2)
print(type(k2))
print(type(k))
