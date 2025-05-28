from insertion_sort import insertion_sort
from merge_sort import merge_sort

def print_array(arr):
    print(" ".join(map(str, arr)))

def main():
    # Get array from user
    array_size = int(input("Enter the size of the array to be sorted: "))
    arr = [int(input(f"Enter element {i+1}: ")) for i in range(array_size)]

    print("The array received from the user:")
    print_array(arr)

    # Merge Sort
    print("\nSorted with Merge Sort:")
    merge_sorted = arr.copy()
    merge_sort(merge_sorted, 0, len(merge_sorted) - 1)
    print_array(merge_sorted)

    # Insertion Sort
    print("\n************************")
    print("Sorted with Insertion Sort:")
    insertion_sorted = arr.copy()
    insertion_sort(insertion_sorted)
    print_array(insertion_sorted)

    # Predefined array
    print("\nSorting a predefined 12-element array with both algorithms:")
    print("************************")
    arr1 = [15, 20, 3, 56, 76, 34, 2, 13, 65, 89, 12, 126]
    arr2 = arr1.copy()

    print("\nMerge Sort result:")
    merge_sort(arr1, 0, len(arr1) - 1)
    print_array(arr1)

    print("\nInsertion Sort result:")
    insertion_sort(arr2)
    print_array(arr2)

if __name__ == "__main__":
    main()
