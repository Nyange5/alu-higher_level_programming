#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    div_answer = 0
    new_list = []
    for i in range(list_length):
        try:
            if not isinstance(my_list_1[i], (int, float)) or not isinstance(my_list_2[i], (int, float)):
                raise TypeError
            div_answer = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            new_list.append(div_answer)
    return new_list
