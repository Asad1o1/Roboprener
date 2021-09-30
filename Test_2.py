# Write a Python Program to find the two largest numbers in an array.

def find_largest(arr: list, n: int) -> list:
    largest_number = []
    for i in range(n):
        arr.sort()
        x = arr.pop(len(arr) - 1)
        largest_number.append(x)
    return largest_number


if __name__ == '__main__':
    total_largest_number_to_find = 2
    ar = [1, 2, 3, 7, 8, 9, 10, 11, 12, 14, 15, 25]
    print(find_largest(ar, total_largest_number_to_find))
