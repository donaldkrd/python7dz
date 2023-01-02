import config as conf
import view as v
import os
   

# Добавление записи в БД
def insert_in_db(id, first_name, last_name, birthday, work, phone_number):
    if os.path.exists(conf.path_db):
        with open(conf.path_db, "a", encoding="utf-8") as file:
            file.write("\n" + str(id) + "," + first_name + "," + last_name + \
                        "," + birthday + "," + work + "," + phone_number)                         
    else:        
        with open(conf.path_db, "w", encoding="utf-8") as file:
            file.write(str(id) + "," + first_name + "," + last_name + \
                        "," + birthday + "," + work + "," + phone_number)
        
    v.success_return(f"insert_in_db {id} done", "2201")


# Проверяем наличие записи по ID
def check_by_id(id):
    with open(conf.path_db, "r", encoding="utf-8") as file:
        for line in file:
            line_split = line.split(",")

            if int(line_split[0]) == id:
                return True

    return False


# Возвращаем последний ID в БД
def get_last_id(path = conf.path_db):
    with open(path, "r", encoding="utf-8") as file:
        last_line = file.readlines()[-1] 

    last_line_split = last_line.split(",")

    return last_line_split[0]


# Показываем запись из БД по ID
def show_by_id(id):
    check = 0

    with open(conf.path_db, "r", encoding="utf-8") as file:
        for line in file:
            line_split = line.split(",")

            if int(line_split[0]) == id:
                v.show_one_db(line_split[0], line_split[1], line_split[2], line_split[3], line_split[4], line_split[5])
                check = 1
                break            

    if check == 0: v.error_return(f"ID {id} not found in DB", "4201")


# Удалить запись по ID
def delete_by_id(id):
    with open(conf.path_db, "r", encoding="utf-8") as file:
        lines = file.readlines()

    with open(conf.path_db, "w", encoding="utf-8") as file:
        for line in lines:
            line_split = line.split(",")

            if int(line_split[0]) != int(id):
                file.write(line)

    v.success_return(f"delete_by_id {id} done", "2201")

    
# Изменить запись по ID
def update_by_id(id, first_name, last_name, birthday, work, phone_number):
    with open(conf.path_db, "r", encoding="utf-8") as file:
        lines = file.readlines()

    with open(conf.path_db, "w", encoding="utf-8") as file:
        for i, line in enumerate(lines):
            line_split = line.split(",")
            
            if i < len(lines) - 1:
                if int(line_split[0]) != int(id):
                    file.write(line)
                elif int(line_split[0]) == int(id):
                    file.write(str(id) + "," + first_name + "," + last_name + \
                            "," + birthday + "," + work + "," + phone_number + "\n") 
            else:
                if int(line_split[0]) != int(id):
                    file.write(line)
                elif int(line_split[0]) == int(id):
                    file.write(str(id) + "," + first_name + "," + last_name + \
                            "," + birthday + "," + work + "," + phone_number)


    v.success_return(f"delete_by_id {id} done", "2201")