def selection_sort(arr):
    n = len(arr)
    comparisons = 0
    assignments = 0
    print("Початковий масив:", arr)
 
    for i in range(n - 1):
        print("-" * 30)
        print(f"Ітерація {i}:")
        print(f"Поточний елемент (для обміну): arr[{i}] = {arr[i]}")
        print("Шукаємо мінімальний елемент у частині:", arr[i:])
 
        min_index = i
        assignments += 1
 
        for j in range(i + 1, n):
            comparisons += 1
            if arr[j] < arr[min_index]:
                min_index = j
                assignments += 1
 
        print(f"Знайдено мінімальний елемент: arr[{min_index}] = {arr[min_index]}")
        comparisons += 1
        if min_index != i:
            print(f"Обмін arr[{i}] ({arr[i]}) і arr[{min_index}] ({arr[min_index]})")
            arr[i], arr[min_index] = arr[min_index], arr[i]
            assignments += 3
        else:
            print("Обмін не потрібний")
 
        print(f"Масив після ітерації {i}:", arr)
 
    print("-" * 30)
    print("Сортування завершено.")
    print("Фінальний відсортований масив:", arr)
    print("Загальна кількість порівнянь:", comparisons)
    print("Загальна кількість присвоєнь:", assignments)
    return arr, comparisons, assignments
 
my_list = def selection_sort(arr):
    n = len(arr)
    comparisons = 0
    assignments = 0
    print("Початковий масив:", arr)
 
    for i in range(n - 1):
        print("-" * 30)
        print(f"Ітерація {i}:")
        print(f"Поточний елемент (для обміну): arr[{i}] = {arr[i]}")
        print("Шукаємо мінімальний елемент у частині:", arr[i:])
 
        min_index = i
        assignments += 1
 
        for j in range(i + 1, n):
            comparisons += 1
            if arr[j] < arr[min_index]:
                min_index = j
                assignments += 1
 
        print(f"Знайдено мінімальний елемент: arr[{min_index}] = {arr[min_index]}")
        comparisons += 1
        if min_index != i:
            print(f"Обмін arr[{i}] ({arr[i]}) і arr[{min_index}] ({arr[min_index]})")
            arr[i], arr[min_index] = arr[min_index], arr[i]
            assignments += 3
        else:
            print("Обмін не потрібний")
 
        print(f"Масив після ітерації {i}:", arr)
 
    print("-" * 30)
    print("Сортування завершено.")
    print("Фінальний відсортований масив:", arr)
    print("Загальна кількість порівнянь:", comparisons)
    print("Загальна кількість присвоєнь:", assignments)
    return arr, comparisons, assignments
 
my_list = [28, 38, 44, 53, 53, 65, 74, 82, 100]
selection_sort(my_list.copy())

selection_sort(my_list.copy())
