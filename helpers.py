import view as v
import controller as c


def int_input_check(str):    
    try:
        return int(str)

    except ValueError:        
        v.error_return("Не цифра", "4401")
        c.run()