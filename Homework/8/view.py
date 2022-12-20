def show_menu() -> int:
    print("\n" + "=" * 20)
    print("Выберите необходимое действие")
    print("1. Найти сотрудника")
    print("2. Сделать выборку сотрудников по должности")
    print("3. Сделать выборку сотрудников по зарплате")
    print("4. Добавить сотрудника")
    print("5. Удалить сотрудника")
    print("6. Обновить данные сотрудника")
    print("7. Экспортировать данные в формате json")
    print("8. Экспортировать данные в формате csv")
    print("0. Закончить работу")
    return int(input("Введите номер необходимого действия: "))

def input_value():
    return input("Введите значение: ")
def exit():
    print('Выход')
def print_list(data):
    print("\n" + "=" * 20)
    print(*data, sep="\n")
def parameter_search_worker():
    print("\n" + "=" * 20)
    print("1. Фамилия")
    print("2. Имя")
    print("3. Отчество")
    print("4. ID")
    print("0. Выйти в меню")
    return int(input("Введите номер необходимого действия: "))
def position_selection():
    print("\n" + "=" * 20)
    print("Выберите необходимую должность")
    print("1. Менеджер")
    print("2. Программист")
    print("3. Директор")
    print("0. Выйти в меню")
    return int(input("Введите номер необходимой должности: "))
def salary_range():
    print("\n" + "=" * 20)
    range_line = []
    range_line.append(int(input("Введите нижнею планку: ")))
    range_line.append(int(input("Введите верхнею планку: ")))
    return range_line
def input_worker_data():
    print("\n" + "=" * 20)
    temp = []
    temp.append(input("Введите Фамилию: "))
    temp.append(input("Введите Имя: "))
    temp.append(input("Введите Отчество: "))
    temp.append(input("Введите должность: "))
    temp.append(input("Введите номер телефона №1: "))
    temp.append(input("Введите номер телефона №2: "))
    temp.append(input("Введите номер телефона №3: "))
    return temp
def input_id():
    return input("Введите номер сотрудкника id: ")
def finish():
    print("Выполнено")