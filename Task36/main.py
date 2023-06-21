def print_operation_table(operation, num_rows=1, num_columns=6):
    # Вычисляем максимальную длину значения в таблице для выравнивания отступов
    max_length = len(str(operation(num_rows, num_columns)))

    for row in range(1, num_rows + 1):
        for col in range(1, num_columns + 1):
            value = operation(row, col)
            # Выравниваем отступы с помощью функции str.ljust() для добавления пробелов слева
            value_str = str(value).ljust(max_length)
            print(value_str, end=" ")
        print()


# Пример использования функции
print_operation_table(lambda x, y: x * y)
