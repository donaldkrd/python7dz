import view as v
import services as s
import helpers as h


def run():
    choose_operation_level = h.int_input_check(input("1 - Работа с БД, 2 - Работа с записями в БД, 3 - Выход: "))
    
    if choose_operation_level == 1:
        choose_operation_type = h.int_input_check(input("1 - Создание новой БД (перезаписывает), 2 - Экспорт /"\
                                    " Импорт (перезаписывает), 3 - Просмотр БД, 4 - Очистка БД: "))

        if choose_operation_type == 1:
            choose_db_entries = h.int_input_check(input("Введите необходимое количество записей в БД: "))

            if choose_db_entries > 0:
                s.create_db(choose_db_entries)
                run()

            else:
                v.error_return("choose_db_entries out of index", "4001")        
                run()

        elif choose_operation_type == 2:
            choose_operation_e_i = h.int_input_check(input("1 - Экспорт БД в csv, 2 - Экспорт БД json, 3 - Импорт БД в csv, 4 - Импорт БД json: "))

            if choose_operation_e_i == 1:
                s.export_csv()
                run()

            if choose_operation_e_i == 2:
                s.export_json()
                run()

            if choose_operation_e_i == 3:
                s.import_csv()
                run()

            if choose_operation_e_i == 4:
                s.import_json()
                run()

            else:
                v.error_return("choose_format out of index", "4002")
                run()

        elif choose_operation_type == 3:
            v.show_full_db()
            run()

        elif choose_operation_type == 4:
            s.remove_db()            
            run()

        else:
            v.error_return("choose_operation_type out of index", "4003")        
            run()

    elif choose_operation_level == 2:
        choose_db_entry_type = h.int_input_check(input("1 - Добавить запись, 2 - Изменить запись, 3 - Отобразить запись, 4 - Удалить запись: "))

        if choose_db_entry_type == 1:
            s.insert_record()    
            run()

        elif choose_db_entry_type == 2:
            s.update_record()
            run()

        if choose_db_entry_type == 3:
            s.show_record()   
            run()

        if choose_db_entry_type == 4:
            s.delete_record()       
            run()

        else:
            v.error_return("choose_db_entry_type out of index", "4005")        
            run()

    elif choose_operation_level == 3:
        print("Bye!")
        exit()

    else:
        v.error_return("choose_operation_type out of index", "4006")        
        run()