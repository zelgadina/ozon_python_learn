from os import path
from getpass import getuser
from decimal import Decimal


def hello_message():
    print(f"""
        Привет, {getuser()}!
        Перед тобой альфа-версия программы финансовой отчётности.
        Ты можешь записывать свои доходы или расходы в отдельные
        файлы с расширением '.txt', а программа рассчитает итоговую
        сумму и среднее арифметическое в выбранном файле.

        Файл должен содержать числа, записанные построчно.
        Результаты обработки данных будут записны в файл results.txt
        и продублированы на экране.

        Чтобы выйти из программы, нажми Ctrl+C.
        """)
    pass

def load_data():
    """Считывает текстовый файл, возвращает содержимое в виде списка строк."""
    try:
        while True:
            path_to_file = input("Введите путь к файлу:\n").strip()

            if path.exists(path.normpath(path_to_file)):
                with open(path_to_file, 'r') as f:
                    return  f.read().splitlines()

            print(f"Файл с именем '{path_to_file}' не найден, попробуйте снова.\
                    Проверьте путь к файлу и его расширение.")
            continue

    except KeyboardInterrupt:
        exit()
    except Exception:
        print("Упс! Что-то пошло не так.\n :'( Возможно, файл повреждён.")
        pass

def save_data(output_data):
    with open('financial_report.txt', 'w') as f:
            f.writelines('\n'.join(output_data))

def preprocessing_data(input_data):
    """Возвращает нормализованный список из 'Decimal(item)'."""
    norm_data = []
    for string in input_data:
        try:
            norm_data.append(Decimal(string))
        except Exception:
            continue
    return norm_data

def calc_total_sum(norm_data):
    total_sum = f"Сумма всех денежных средств: {sum(norm_data)}"
    return total_sum

def calc_average(norm_data):
    average = f"Среднее арифметическое: {sum(norm_data) / len(norm_data)}"
    return average



hello_message()

input_data = load_data()

norm_data = preprocessing_data(input_data)

output_data = calc_total_sum(norm_data), calc_average(norm_data)

print('\n'.join(output_data))
save_data(output_data)
