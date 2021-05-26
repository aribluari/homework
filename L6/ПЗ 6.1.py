import math
floors = int(input('Количество этажей: '))
apart_in_floors = int(input('Количество квартир на этаже: '))
need_apart = int(input('Нужная квартира: '))

sum_floors = need_apart / apart_in_floors   # количество этажей между нужной и первой квартирой
sum_floors = math.ceil(sum_floors)
if sum_floors < floors:
    f = 1                                   # f - нужный подъезд
    need_level = sum_floors                 # нужный этаж
else:
    f = sum_floors / floors                 # подъезд если > 1
    f = math.ceil(f)
    lvl_f_ap = (floors * f) - sum_floors
    need_level = floors - lvl_f_ap

print('\nПодъезд: ' + str(math.ceil(f)) + ' Этаж: ' + str(int(need_level)))





