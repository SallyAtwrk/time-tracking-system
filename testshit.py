from functools import reduce
import datetime


id_lst = [1,2,1,2] #Тестовые Id
date_lst = ['2018-12-02 12:00:00','2018-12-02 13:00:00','2018-12-02 12:20:00','2018-12-02 20:00:00'] #Тестовые даты

dt_group = list(zip(id_lst,date_lst)) #Групировка записей в кортеж айди+дата
#Поиск идексов дубликатов
seen = set()
for n in id_lst:
    if n in seen:
        indx = [i for i, x in enumerate(id_lst) if x == 1]
        for h in indx:
            for t in date_lst:
                print(t[h])

    else:
        seen.add(n)


#Преобразование даты в дейт, вывод в секундах для сравнения поиска макс и мин, конструкция перевода обратно к дате существует но не реализованна
for (x,y) in dt_group:
     (date, hmss) = y.split()
     (y,m,d) = date.split('-')
     (hh, mm, ss) = hmss.split(":")
     time = datetime.datetime(int(y), int(m),int(d), int(hh), int(mm), int(ss))
     print(time.timestamp())
