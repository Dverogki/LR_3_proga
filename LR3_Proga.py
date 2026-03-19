import random
import numpy as np

univer = ['Государственный университет', 'Технический университет', 'Зарубежный университет', 'Университет дизайна']
kriterii = ['Репутация университета', 'Стоимость проживания', 'Отдаленность от дома', 'Дальнейшее трудоустройство', 'Инфраструктура']

def create_matrix(kriterii):
    matrix = []
    n=len(kriterii)

    for i in range(n):
        row = []
        for j in range(n):
            if i == j: ratio = 1
            elif j > i:
                values = [1 / 9, 1 / 8, 1 / 7, 1 / 6, 1 / 5, 1 / 4, 1 / 3, 1 / 2, 1, 2, 3, 4, 5, 6, 7, 8, 9]
                ratio = round(random.choice(values), 3)
            else: ratio = 1
            row.append(ratio)
        matrix.append(row)

    for i in range(n):
        for j in range(i + 1, n):
            if j > i: matrix[j][i] = round(1.0 / matrix[i][j], 3)

    return matrix

def display_matrix(matrix, krit):
    for i, row in enumerate(matrix):
        row_text = krit[i][:20].ljust(20)
        for j in range(len(row)):
            row_text += f" | {row[j]:.3f}"
        print(row_text)

def metod_analiza_matrix(matrix):
    n = len(matrix)
    matrix = np.array(matrix)

    sum_column = np.sum(matrix, axis=0)
    print(f"Суммы по столбцам: {np.round(sum_column, 3)}")

    norm_matrix = matrix / sum_column
    print(f"Нормированная матрица:\n{np.round(norm_matrix, 3)}")

    weight_column = np.mean(norm_matrix, axis=1)
    print(f"Весовой столбец: {np.round(weight_column, 3)}\n")

    return weight_column

def weight_alt():

    matrix_weight_alter = []
    matrix_weight_alter.append(metod_analiza_matrix(matrix_par_reput))
    matrix_weight_alter.append(metod_analiza_matrix(matrix_par_coin))
    matrix_weight_alter.append(metod_analiza_matrix(matrix_par_otdal))
    matrix_weight_alter.append(metod_analiza_matrix(matrix_par_trud))
    matrix_weight_alter.append(metod_analiza_matrix(matrix_par_infr))

    matrix_weight_alter_T = np.transpose(matrix_weight_alter)

    result = np.dot(matrix_weight_alter_T, metod_analiza_matrix(matrix_par_sravneni)).round(3)

    return result

matrix_par_sravneni = create_matrix(kriterii)

print("\nМатрица парных сравнений критериев:")
header = f"Критерий".ljust(20) + " | Репут | Стоим | Отдал | Трудо | Инфр "
print(f'{header}')
display_matrix(matrix_par_sravneni, kriterii)

matrix_par_reput = create_matrix(univer)
matrix_par_coin = create_matrix(univer)
matrix_par_otdal = create_matrix(univer)
matrix_par_trud = create_matrix(univer)
matrix_par_infr = create_matrix(univer)

print(f"\nРепутация университе".ljust(20) + " | Госуд | Техни | Заруб | Дизай ")
display_matrix(matrix_par_reput, univer)

print(f"\nСтоимость проживания".ljust(20) + " | Госуд | Техни | Заруб | Дизай ")
display_matrix(matrix_par_coin, univer)

print(f"\nОтдаленность от дома".ljust(20) + " | Госуд | Техни | Заруб | Дизай ")
display_matrix(matrix_par_otdal, univer)

print(f"\nДальнейшее трудоустр".ljust(20) + " | Госуд | Техни | Заруб | Дизай ")
display_matrix(matrix_par_trud, univer)

print(f"\nИнфраструктура".ljust(20) + "  | Госуд | Техни | Заруб | Дизай ")
display_matrix(matrix_par_infr, univer)

result = weight_alt()
print(f"\nВеса альтернатив: {result}")

print("\nРейтинг университетов:")
ranking = sorted([(result[i], univer[i]) for i in range(len(univer))], reverse=True)
for rank, (weight, name) in enumerate(ranking, 1):
    print(f"{rank}. {name} - {weight:.3f} ({weight*100:.1f}%)")

