from random import randint


def quicksort(arr):
    if len(arr) < 2:
        return arr

    low, same, high = [], [], []

    pivot = arr[randint(0, len(arr) - 1)]

    for item in arr:

        if item < pivot:
            low.append(item)
        elif item == pivot:
            same.append(item)
        elif item > pivot:
            high.append(item)
    return quicksort(low) + same + quicksort(high)


def sum_elements(arr, result):
    sorted_array = quicksort(arr)
    status = False
    a = 0
    b = 0
    for i in sorted_array:
        if i < result:
            second_number = int(result) - int(i)
            if second_number in sorted_array:
                status = True
                a = i
                b = second_number
                break
    return status, a, b


if __name__ == '__main__':
    x = [1, 5, 8, 2, 9]
    y = 9
    status, a, b = sum_elements(x, y)
    if not status:
        print(f'No se encontraron elementos que sumen: {y}')
    else:
        print(f'Los dos primeros elementos que suman {y} son: {a}, {b}')
