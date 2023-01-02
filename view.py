import config as conf


# Отображение всей БД построчным списком
def show_full_db():
    print ("id", "first_name", "last_name", "birthday", "work", "phone_number")
    with open(conf.path_db, "r", encoding="utf-8") as file:
        for line in file:
            line_split = line.split(",")
            print(line_split[0], line_split[1], line_split[2], line_split[3], line_split[4], line_split[5].removesuffix("\n"))


# Отображение одной записи     
def show_one_db(id, first_name, last_name, birthday, work, phone_number):
    print ("id", "first_name", "last_name", "birthday", "work", "phone_number")
    print (id, first_name, last_name, birthday, work, phone_number)


# Успешное выполнение задачи
def success_return(success, id):
    print(f"Success = {success}. Event code ID = {id}")
    
    
# Неудачное выполнение задачи 
def error_return(error, id):
    print(f"Error = {error}. Event code ID = {id}")