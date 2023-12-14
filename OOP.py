from tabulate import tabulate

class Table:
    def __init__(self):
        self.columns = ["Марка", "Модель","Год выпуска", "Об. мотора(л)", "Тип мотора", "Номер",
    "Привод", "Мощность (л.с.)", "Двери (шт)", "Пробег (км)", "Цвет", "На парковке?", "Объем багажника", "Тип кузова", "Расход топлива (л/100км)"]
        self.table = []

    def load_table(self, file_name="tms", extension=".txt"):
        full_path = f"{file_name}{extension}"
        try:
            with open(full_path, 'r', encoding='utf-8') as file:
                headers = file.readline().strip().split(",")
                self.columns = headers
                self.table.clear()
                for line in file:
                    values = line.strip().split("|")
                    row = dict(zip(headers, values))
                    self.table.extend([row])
                print(f"Таблица успешно загружена из файла: {full_path}")
        except FileNotFoundError:
            print("Файл не найден. Создание новой таблицы.")
        except Exception as e:
            print(f"При загрузке файла произошла ошибка: {e}")

    def display_table(self):
        if not self.table:
            print("Таблица пуста")
        else:
            table_with_indices = [{"#": i, **row} for i, row in enumerate(self.table, start=1)]
            print(tabulate(table_with_indices, headers="keys", tablefmt="double_grid"))

    def save_table(self, file_name):
        if not self.table:
            print("Таблица пуста.Нечего сохранять.")
            return
        if not file_name.endswith(".txt"):
            file_name += ".txt"
        full_path = file_name
        with open(full_path, 'w', encoding='utf-8') as file:
            header_line = ",".join(self.columns)
            file.write(header_line + "\n")
            for row in self.table:
                values = [str(row[column]) for column in self.columns]
                file.write("|".join(values) + "\n")
            print(f"Таблица успешно сохранена в файл: {full_path}")
     
    def sort_table(self, column_name):
        if column_name in self.columns:
            self.table.sort(key=lambda row: row[column_name])
            print(f"Таблица успешно отсортирована по столбцу: {column_name}")
        else:
            print(f"Столбец с именем '{column_name}' не существует в таблице.")

class Car(Table):
    def __init__(self):
        super().__init__()


class Features(Table):
    def __init__(self):
        super().__init__()

    def add_row(self):
        new_row = {}
        for column in self.columns:
            if column == "Номер":
                number = input(f"Введите {column}: ").upper()
                while any(row["Номер"] == number for row in self.table):
                    print("Автомобиль с таким номером уже существует в таблице. Пожалуйста, введите другой номер.")
                    number = input("Введите номер: ").upper()
                new_row[column] = number
            elif column == "Тип мотора":
                while True:
                    tup_mot=input("Введите тип мотора: ").upper()
                    if tup_mot in ["БЕНЗИН","ДИЗЕЛЬ","ЭЛЕКТРОМОТОР","ГИБРИД"]:
                        new_row[column] = tup_mot
                        break
                    else:
                        print("Введите тип мотора (БЕНЗИН,ДИЗЕЛЬ,ЭЛЕКТРОМОТОР,ГИБРИД)")
            elif column == "Привод":
                while True:
                    privod=input("Введите Привод: ").upper()
                    if privod in ["ПЕРЕДНИЙ","ЗАДНИЙ","ПОЛНЫЙ"]:
                        new_row[column] = privod
                        break
                    else:
                        print("Введите привод (передний,задний,полный)")
            elif column == "Год выпуска":
                while True:
                    age = input("Введите Год выпуска: ") 
                    try:
                        if 1900 <= int(age) <= 2023:
                            new_row[column] = age
                            break
                        else:
                            print("Год выпуска не может быть раньше 1900г. , или быть после 2023г.")
                    except ValueError:
                        print("Год должен быть числом") 
            elif column == "Об. мотора (л)":
                while True:
                    value_mot = input("Введите Объем мотора(л): ") 
                    try:
                        if 0.1 <= float(value_mot) <= 13.0:
                            new_row[column] = value_mot
                            break
                        else:
                            print("Объем мотора может быть от 0.1 до 13.0 литров")
                    except ValueError:
                        print("Объем мотора должен быть числом с точкой ")
            elif column == "Двери (шт)":
                while True:
                    doors = input("Введите Количество дверей(шт): ") 
                    try:
                        if 1 <= int(doors) <= 6:
                            new_row[column] = doors
                            break
                        else:
                            print("Количество дверей не может быть отрицательным, или быть больше 6-ти дверей")
                    except ValueError:
                        print("Количество дверей должно быть числом ")
            elif column == "Мощность (л.с.)":
                while True:
                    power = input("Введите Мощность двигателя(л.с.): ") 
                    try:
                        if 0 <= int(power) <= 2500:
                            new_row[column] = power
                            break
                        else:
                            print("Количество лошадинных сил не может быть отрицательным или быть больше 2500(л.с.)")
                    except ValueError:
                        print("Количество Лошадинных сил должно быть ТОЛЬКО числом без точек") 
            elif column == "Пробег (км)":
                while True:
                    milage = input("Введите Пробег: ") 
                    try:
                        if 0 <= int(milage) <= 4800000:
                            new_row[column] = milage
                            break
                        else:
                            print("Пробег не может быть орицателен, или быть больше 4.8млн.(км) ")
                    except ValueError:
                        print("Пробег должен быть ТОЛЬКО числом")
            elif column == "Объем багажника":
                while True:
                    bagage = input("Введите объем багажника: ")
                    try:
                        if 0 <= int(bagage) <= 5000:
                            new_row[column] = bagage
                            break
                        else:
                            print("Объем багажника не может быть отрицательным или больше 5000 литров ")
                    except ValueError:
                        print("Объем может быть ТОЛЬКО числом")
            elif column == "Тип кузова":
                while True:
                    tip_kuzova = input("Введите тип Кузова: ").upper()
                    if tip_kuzova:
                        new_row[column] = tip_kuzova
                        break
            elif column == "Расход топлива (л/100км)":
                while True:
                    rasxod = input("Введите расход топлива: ")
                    try:
                        if 0 <= int(rasxod) <= 117:
                            new_row[column] = rasxod
                            break
                        else:
                            print("Расход топлива не может быть отрицательным ")
                    except ValueError:
                        print("Расход топлива может быть ТОЛЬКО числом")
            else:
                value = input(f"Введите {column}: ").upper()
                new_row[column] = value
        self.table+=[new_row]
        print("Строка успешно добавлена")
        self.save_table("tms.txt")
        print("Изменения сохранены")

    def delete_row(self):
        if not self.table:
            print("Таблица пуста. Невозможно удалить строки.")
            return
        index = input("Введите номер строки, которую нужно удалить: ")
        if index.isdigit():
            index = int(index)
            if 1 <= index <= len(self.table):
                del self.table[index - 1]
                print(f"Строка с номером {index} была успешно удалена")
            else:
                print("Неверный номер строки")
        else:
            print("Номер должен быть целым числом")
        self.save_table("tms.txt")
        print("Изменения сохранены")

    def update_row(self):
        if not self.table:
            print("Таблица пуста.Невозможно изменить строки.")
            return
        index = input("Введите номер строки для обновления: ")
        if index.isdigit():
            index = int(index)
            if 1 <= index <= len(self.table):
                car = self.table[index - 1]
                existing_number = car["Номер"]
                column_name = input("Введите имя столбца для обновления: ")
                if column_name in self.columns:
                    new_value = input("Введите новое значение: ").upper()
                    if column_name == "Номер":
                        while any(row["Номер"] == new_value for row in self.table):
                            print("Автомобиль с таким номером уже существует в таблице. Пожалуйста, введите другой номер.")
                            new_value = input("Введите номер: ").upper()
                    car[column_name] = new_value
                    if column_name == "Номер" and existing_number != new_value:
                        while any(row["Номер"] == new_value for row in self.table):
                            print("Автомобиль с таким номером уже существует в таблице. Пожалуйста, введите другой номер.")
                            new_value = input("Введите номер: ").upper()
                        car[column_name] = new_value
                    print("Строка успешно изменена")
                else:
                    print("Неверное имя столбца")
            else:
                print("Неверный номер строки")
        else:
            print("Номер должен быть целым числом")
        self.save_table("tms.txt")
        print("Изменения сохранены")    
    
    def search(self):
        if not self.table:
            print("Таблица пуста. Нечего искать.")
            return

        search_query = input("Введите параметр для поиска: ").upper()
        found = False

        search_results = []

        for i, row in enumerate(self.table, start=1):
            found_in_row = any(search_query.lower() in str(value).lower() for value in row.values())

            if found_in_row:
                if not found:
                    print("Результаты поиска:\n")
                    found = True
                print(f"Найдено в строке #{i}:")
                print(tabulate([row], headers="keys", tablefmt="double_grid"))
                print()

                search_results.append({"#": i, **row})

        if not found:
            print(f"Нет совпадений для запроса <{search_query}>.")
        else:
            print("Результаты в виде таблицы:")
            print(tabulate(search_results, headers="keys", tablefmt="double_grid"))

car_data = Car()
features = Features()

while True:
    print("\nМеню:")
    print("1. Добавить строку")
    print("2. Удалить строку")
    print("3. Внести изменения")
    print("4. Поиск")
    print("5. Показать таблицу")
    print("6. Сохранить таблицу")
    print("7. Загрузить таблицу")
    print("8. Сортировать таблицу")
    print("9. Выйти")

    choice = input("Выберите действие: ")

    if choice == "1":
        features.add_row()
    elif choice == "2":
        features.delete_row()
    elif choice == "3":
        features.update_row()
    elif choice == "4":
        features.search()
    elif choice == "5":
        features.display_table()
    elif choice == "6":
        file_name = input("Введите название файла для сохранения (без расширения, например, table): ")
        features.save_table(file_name)
    elif choice == "7":
        load_auto = input("Загрузить автоматически (1) или вручную (2)?: ")
        if load_auto.strip().lower() in ["а","авто","1"]:
            features.load_table()
        elif load_auto.strip().lower() in ["б","вручную","2"]:
            file_name = input("Введите название файла для загрузки (без расширения, например, table): ")
            features.load_table(file_name)
        else:
            print("Неверный выбор.")
    elif choice == "8":
        column_name = input("Введите имя столбца для сортировки: ")
        features.sort_table(column_name)
    elif choice == "9":
        save_exit = input("Сохраниться перед выходом?: ")
        if save_exit.lower() in ['yes', '1', 'да']:
            file_name = input("Введите название файла для сохранения (без расширения, например, table): ")
            features.save_table(file_name)
            break
        elif save_exit.lower() in ['no', '2', 'нет']:
            break
        else:
            print('Неверный выбор')
            break
    else:
        print("Неверный выбор. Попробуйте снова.")
        
        