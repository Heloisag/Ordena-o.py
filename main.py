def bubbleSort(arr, choice_order):
    n = len(arr)

    for i in range(n-1):
        swapped = False

        for j in range(0, n-i-1):
            if choice_order.lower() == "a":
                if arr[j] > arr[j + 1]:
                    swapped = True
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
            elif choice_order.lower() == "d":
                if arr[j] < arr[j + 1]:
                    swapped = True
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

        if not swapped:
            return

def insertionSort(arr, choice_order):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        if choice_order.lower() == "a":
            while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        elif choice_order.lower() == "d":
            while j >=0 and key > arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key

def partition(arr, low, high, choice_order):
    i = (low-1)
    pivot = arr[high]
    if choice_order.lower() == "a":
        for j in range(low, high):
            if arr[j] <= pivot:
                i = i+1
                arr[i], arr[j] = arr[j], arr[i]
    elif choice_order.lower() == "d":
        for j in range(low, high):
            if arr[j] >= pivot:
                i = i+1
                arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)
 
 
def quickSort(arr, low, high, choice_order):
    if len(arr) == 1:
        return arr
    if low < high:
        pi = partition(arr, low, high, choice_order)
        quickSort(arr, low, pi-1, choice_order)
        quickSort(arr, pi+1, high, choice_order)


def check_input(numb):
    if isinstance(numb, int):
        return True
    else:
        print("Invalid input. Please enter an integer.")
        return False

def ascending_order(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def descending_order(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def main():
    my_array = []
    while True:
        input_Numb = input("Enter a number: ")
        if input_Numb.isdigit():
            input_Numb = int(input_Numb)
            if check_input(input_Numb):
                my_array.append(input_Numb)
        else:
            print("Invalid input. Please enter an integer.")

        check_continue = input("Do you want to continue? (y/n): ")
        if check_continue.lower() == "n":
            break
    print(type(my_array[0]))
    # my_array = [64, 34, 25, 12, 22, 11, 90]
    while True:
        print("1. Bubble Sort")
        print("2. Insertion Sort")
        print("3. Quick Sort")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            choice_order = input("Do you want to sort in ascending or descending order? (a/d): ")
            bubbleSort(my_array, choice_order)
            print("Sorted array is: ", my_array)

        elif choice == 2:
            choice_order = input("Do you want to sort in ascending or descending order? (a/d): ")
            insertionSort(my_array, choice_order)
            print("Sorted array is: ", my_array)
        elif choice == 3:
            choice_order = input("Do you want to sort in ascending or descending order? (a/d): ")
            quickSort(my_array, 0, len(my_array) - 1, choice_order)
            print("Sorted array is: ", my_array)
        elif choice == 4:
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
