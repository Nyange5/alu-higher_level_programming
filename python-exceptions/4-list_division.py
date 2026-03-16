#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        div_answer = 0
        try:
           div_answer = my_list_1[i] / my_list_2[i]
        except ValueError:
            print("Wrong type")
            div_answer = 0
        except ZeroDivisionError:
            print("division by 0")
            div_answer = 0
        except IndexError:
            print("out of range")
            div_answer = 0
        finally:
            new_list.append(div_answer)
    return new_list
