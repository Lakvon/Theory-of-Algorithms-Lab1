def insertion_sort(arr):
    n = len(arr)
    comparisons = 0
    assignments = 0
    print("Початковий масив:", arr)
 
    for i in range(1, n):
        print("-" * 30)
        print(f"Ітерація {i}:")
        key = arr[i]
        assignments += 1
        print("Елемент для вставки (key):", key)
        print("Відсортована частина:", arr[:i])
 
        j = i - 1
        assignments += 1
        while j >= 0 and arr[j] > key:
            comparisons += 1
            print(f"Порівняння: {arr[j]} > {key}. True. Зсуваємо {arr[j]} вправо.")
            arr[j + 1] = arr[j]
            assignments += 1
            j -= 1
            assignments += 1
 
        if j >= 0:
            comparisons += 1
            print(f"Порівняння: {arr[j]} > {key}. False. Цикл завершено.")
        else:
            print("Досягнуто початку масиву. Цикл завершено.")
 
        arr[j + 1] = key
        assignments += 1
        print(f"Вставка {key} на позицію {j + 1}.")
        print(f"Масив після ітерації {i}:", arr)
 
    print("-" * 30)
    print("Сортування завершено.")
    print("Фінальний відсортований масив:", arr)
    print("Загальна кількість порівнянь:", comparisons)
    print("Загальна кількість присвоєнь:", assignments)
    return arr, comparisons, assignments
 
my_list = [53, 100, 44, 74, 53, 38, 82, 65, 28]
insertion_sort(my_list.copy())
