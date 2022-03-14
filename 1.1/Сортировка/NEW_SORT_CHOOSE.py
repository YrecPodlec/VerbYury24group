try:
    def selection_sort(must):
        print('selection sort')
        for i in range(0, len(must) - 1):
            smallest = i
            for j in range(i + 1, len(must)):
                if must[j] < must[smallest]:
                    smallest = j
            must[i], must[smallest] = must[smallest], must[i]
    must1 = input('Введите путь к файлу: ')
    with open(must1, 'r') as file:
        must = [int(row.strip()) for row in file]
    selection_sort(must)
    print(must)
except FileNotFoundError:
    print('Файл не найден')
except ValueError:
    print('Уберите пустые строки из файла')