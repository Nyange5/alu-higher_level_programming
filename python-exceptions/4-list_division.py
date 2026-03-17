#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        result = 0
        try:
            x = my_list_1[i]
            y = my_list_2[i]
            if not isinstance(x, (int, float)) or \ 
                not isinstance(y, (int, float)):
                raise TypeError
            result = x / y
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            new_list.append(result)
    return new_list
