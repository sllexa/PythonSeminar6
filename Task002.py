# Задача 2. Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,*. приоритет операций стандартный.
# *Пример:* 
# 2+2 => 4; 
# 1+2*3 => 7; 
# 1-2*3 => -5;
# - Добавьте возможность использования скобок, меняющих приоритет операций.
#     *Пример:* 
#     1+2*3 => 7; 
#     (1+2)*3 => 9;
count_actions = 0

def str_in_list(txt):
    global count_actions
    num = ""
    result = []
    for i in range(0, len(txt)):
        if txt[i].isdigit():
            num += txt[i]
        else:
            result.append(int(num))
            result.append(txt[i])
            num = ""
            count_actions += 1
    result.append(int(num))
    return result

def calc_action(lst):
    global count_actions
    ind = 0
    while count_actions > 0:
        if "*" in lst:
            ind = lst.index("*")
            lst[ind - 1] *= lst[ind + 1] 
        elif "/" in lst:
            ind = lst.index("/")
            lst[ind - 1] = int(lst[ind - 1] / lst[ind + 1])
        elif "+" in lst:
            ind = lst.index("+")
            lst[ind - 1] += lst[ind + 1]
        elif "-" in lst:
            ind = lst.index("-")
            lst[ind - 1] -= lst[ind + 1]

        lst.pop(ind + 1)
        lst.pop(ind)
        count_actions -= 1
    return lst[0]

str_simple = "17-5*6/3-4/2"
print(str_simple)
res = str_in_list(str_simple)
print(f"Результат = {calc_action(res)}")
