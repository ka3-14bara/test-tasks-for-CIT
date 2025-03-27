def bubbleSort(arr):
    length = len(arr)
    for i in range(length):
        for j in range(0,length-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr

def shakerSort(arr):
    start = 0
    end = len(arr) - 1
    swapped = True

    while swapped:
        swapped = False
        for i in range(start, end):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True

        if not swapped:
            break   

        end -= 1
        swapped = False

        for i in range(end - 1, start - 1, -1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True
        
        start += 1
    return arr

def combSort(arr):
    n = len(arr)
    gap = n
    shrink = 1.3
    sorted = False

    while not sorted:
        gap = int(gap / shrink)
        if gap <= 1:
            gap = 1
            sorted = True

        for i in range(n - gap):
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                sorted = False
    return arr

def quick_sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)
    #return arr

def partition(arr, low, high):
    pivot = arr[high]  # Выбираем последний элемент как опорный
    i = low - 1  # Индекс для элемента, меньшего опорного
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    # Помещаем опорный элемент на правильную позицию
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

a = [ 64, 11, 23, 90, 10]
'''print(bubbleSort(a))
print(shakerSort(a))
print(combSort(a))'''
print(quick_sort(a,0,len(a)-1),a)
