import fakes as f
import config as conf
import view as v
import os
import dto
import csv
import random
import json
import helpers as h


# Создание БД из фейков
def create_db(quantity):    
    if quantity < 1: v.error_return("quantity < 1", "4101")

    else:
        # Удаляем предыдущую БД
        remove_db()

        # Заполняем
        for i in range (quantity):
            dto.insert_in_db(i + 1, f.first_name(), f.last_name(), f.birthday("1.1.1980", "1.1.2000", random.random()),\
                             f.work(), f.phone_number())
        
        v.success_return("create_db done", "2101")


# Удаление БД
def remove_db():
    if os.path.exists(conf.path_db): os.remove(conf.path_db)
    
    v.success_return("remove_db done", "2102")


# Экспорт в CSV
def export_csv():
    with open(conf.csv, mode="w") as w_file:
        file_writer = csv.writer(w_file, delimiter = ";", lineterminator="\r")
        #file_writer.writeheader("")

        with open(conf.path_db, "r", encoding="utf-8") as file:
            for line in file:
                line_split = line.split(",")

                file_writer.writerow([int(line_split[0]), str(line_split[1]), str(line_split[2]), str(line_split[3]),\
                                         str(line_split[4]), str(line_split[5].removesuffix("\n"))])
    
    v.success_return("export_csv done", "2103")


# Экспорт в Json
def export_json():
    data = {}
    data['records'] = []
    columns =["id", "first_name", "last_name", "birthday", "work", "phone_number"]
    
    # Собираем JSON
    with open(conf.path_db, "r", encoding="utf-8") as file: 
        for line in file:
            line_split = line.split(",")
            
            data['records'].append({
                columns[0]: str(line_split[0]),
                columns[1]: str(line_split[1]),
                columns[2]: str(line_split[2]),
                columns[3]: str(line_split[3]),
                columns[4]: str(line_split[4]),
                columns[5]: str(line_split[5])
            })            
    
    # Записываем JSON
    with open(conf.json, "w", encoding="utf-8") as write_file: json.dump(data, write_file)

    v.success_return("export_json done", "2104")


# Импорт из CSV
def import_csv():
    #  Очищаем БД
    with open(conf.path_db, "w", encoding="utf-8") as file: file.write('')

    # Записываем импортируемые значения
    with open(conf.csv, mode="r") as r_file:
        reader = csv.reader(r_file, delimiter = ";", lineterminator="\r")

        for i, line in enumerate(reader):
            with open(conf.path_db, "a", encoding="utf-8") as file:
                if i != 0:
                    file.write("\n" + line[0] + "," + line[1] + "," +  line[2] + "," +  line[3] + "," + \
                            line[4] + "," +  line[5])
                else:
                    file.write(line[0] + "," + line[1] + "," +  line[2] + "," +  line[3] + "," + \
                            line[4] + "," +  line[5])

    v.success_return("import_csv done", "2105")


# Импорт из Json
def import_json():
    #  Очищаем БД
    with open(conf.path_db, "w", encoding="utf-8") as file: file.write('')

    # Записываем импортируемые значения
    with open(conf.json) as json_file:
        data = json.load(json_file)
        for line in data["records"]:
            with open(conf.path_db, "a", encoding="utf-8") as file:
                file.write(line["id"] + "," + line["first_name"] + "," +  line["last_name"] + "," +\
                              line["birthday"] + "," + line["work"] + "," +  line["phone_number"])

    v.success_return("import_json done", "2106")


def insert_record():
    # тут должно быть много проверок, но нет времени их писать
    first_name = input("Введите имя :")
    last_name = input("Введите фамилию :")
    birthday = input("Введите день рождения в формате 1.1.1990 :")
    work = input("Введите должность :")
    phone_number = input("Введите телефонный номер, если номеров несколько используйте |, не используйте пробелы :")

    dto.insert_in_db(int(dto.get_last_id()) + 1 ,first_name, last_name, birthday, work, phone_number) 


def update_record():
    id = h.int_input_check(input("Введите ID записи, которую Вы хотите изменить: "))
    
    if id < 1: v.error_return("ID не может быть меньше 1 или не цифровым")

    else: 
        if dto.check_by_id(id) == True: 
            # тут должно быть много проверок, но нет времени их писать
            first_name = input("Введите имя :")
            last_name = input("Введите фамилию :")
            birthday = input("Введите день рождения в формате 1.1.1990 :")
            work = input("Введите должность :")
            phone_number = input("Введите телефонный номер, если номеров несколько используйте |, не используйте пробелы :")
            
            dto.update_by_id(id, first_name, last_name, birthday, work, phone_number)

        else: v.error_return("ID нет в БД", "4102")


def show_record():
    id = int(input("Введите ID записи для отображения: "))

    if id < 1: v.error_return("ID не может быть меньше 1 или не цифровым")

    else: dto.show_by_id(id)


def delete_record():
    id = int(input("Введите ID записи для удаления: "))

    if id < 1: v.error_return("ID не может быть меньше 1 или не цифровым")   

    else: 
        if dto.check_by_id(id) == True: dto.delete_by_id(id)    
        
        else: v.error_return("ID нет в БД", "4103")