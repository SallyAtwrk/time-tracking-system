def entered_year():
    z = 0
    while z != 1:
        j = input('\n\nВведите год:')
        if j.isdigit() == True:
            j = int(j)
            if j > 2010 and j < 2100:
                j1 = int(j)
                return j1
                z = 1
            else:
                 print('Введеное значение за пределами диапазона 2010 - 2100 гг!')
        else:
            print('Ошибка вввода года!')

def entered_month():
    z = 0
    while z != 1:
        j1 = input('\n\nВведите месяц:')
        if j1 == 'Январь' or j1 == 'Февраль' or j1 == 'Март' or j1 == 'Апрель' or j1 == 'Май' or j1 == 'Июнь' or j1 == 'Июль' or j1 == 'Август' or j1 == 'Сентябрь' or j1 == 'Октябрь' or j1 == 'Ноябрь' or j1 == 'Декабрь':
            month_out = j1
            if month_out == 'Январь':
                month_out_n = 1
            elif month_out == 'Февраль':
                month_out_n = 2
            elif month_out == 'Март':
                month_out_n = 3
            elif month_out == 'Апрель':
                month_out_n = 4
            elif month_out == 'Май':
                month_out_n = 5
            elif month_out == 'Июнь':
                month_out_n = 6
            elif month_out == 'Июль':
                month_out_n = 7
            elif month_out == 'Август':
                month_out_n = 8
            elif month_out == 'Сентябрь':
                month_out_n = 9
            elif month_out == 'Октябрь':
                month_out_n = 10
            elif month_out == 'Ноябрь':
                month_out_n = 11
            elif month_out == 'Декабрь':
                month_out_n = 12
            else:
                month_out_n = 0
                print('Ошибка определения month_out_n')
            return month_out_n
            z = 1
        else:
            print('Введен не правильный месяц или ошибка при вводе')


def replace_name(a):
    if a == 1:
        b = 'Родыгин'
        return b
    elif a == 2:
        b = 'Рощин'
        return b
    elif a == 3:
        b = 'Русаков'
        return b
    elif a == 4:
        b = 'Пигин'
        return b
    elif a == 5:
        b = 'Середнев'
        return b
    elif a == 6:
        b = 'Брагин'
        return b
    elif a == 7:
        b = 'Еремин'
        return b
    elif a == 8:
        b = 'Калякин'
        return b
    else:
        print('Ошибка определения сотрудника')
        return 0
 
def time_comparison():
    pass
    
def time_calculation():
    pass
