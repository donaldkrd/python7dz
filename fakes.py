import random
import names
import time

   
def first_name():  
    return names.get_first_name()


def last_name():    
    return names.get_last_name()

def str_time_prop(start, end, time_format, prop):
    stime = time.mktime(time.strptime(start, time_format))
    etime = time.mktime(time.strptime(end, time_format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(time_format, time.localtime(ptime))

def birthday(start, end, prop):
    return str_time_prop(start, end, '%d.%m.%Y', prop)
        

def work():
    arr = ['Рабочий', 'Менеджер', "Начальник", "Бухгалтер", "Делопроизводитель", "Специалист"]
    return arr[random.randint(0,5)]

def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return str(random.randint(range_start, range_end))

def random_phone_number(quantity):
    if quantity == 1:
        return '+7' + random_with_N_digits(3) + random_with_N_digits(7)

    else:
        numbers = ""
        for i in range(quantity):
            if i == quantity - 1:
                numbers = numbers + '+7' + random_with_N_digits(3) + random_with_N_digits(7)
            else:
                numbers = numbers + '+7' + random_with_N_digits(3) + random_with_N_digits(7) + "|"
        return numbers

def phone_number():
    return random_phone_number(random.randint(1, 5))