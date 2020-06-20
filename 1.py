import sys

def salary():
    args = sys.argv[1:]
    if help in args:
        print('Зарплата рассчитывается по 3 параметрам: выработка в часах,ставка в час, премия')
    else:
        print(f'Введите 3 параметра: {args[0]}, {args[1]}, {args[2]}')
        time_work = int(args[0])
        time_money = int(args[1])
        award = int(args[2])
        my_salary = time_work * time_money + award
    return my_salary



print(salary())

