def sum_elements(arr, result):
    status = False
    a = 0
    b = 0
    for i in arr:
        if i < result:
            second_number = int(result) - int(i)
            if second_number in arr:
                status = True
                a = i
                b = second_number
                break
    return status, a, b


if __name__ == '__main__':
    x = [1, 5, 8, 2, 9]
    y = 10
    status, a, b = sum_elements(x, y)
    if not status:
        print(f'No se encontraron elementos que sumen: {y}')
    else:
        print(f'Los dos primeros elementos que suman {y} son: {a}, {b}')
