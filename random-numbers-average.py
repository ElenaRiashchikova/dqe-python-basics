import random

# Generate 100 random numbers in the range from 0 to 1000
a:list[int] = [random.randint(0, 1000) for _ in range(100)]
print(a)


# Introduce merge_sort function which splits the list into two halves, recursively sorts each half and then merges the two sorted halves into a single sorted list
def merge_sort(arr:list):
    if len(arr) > 1:
        mid = len(arr) // 2
        l = arr[:mid]
        r = arr[mid:]

        merge_sort(l)
        merge_sort(r)

        i = j = k = 0

        while i < len(l) and j < len(r):
            if l[i] < r[j]:  # Ascending
                arr[k] = l[i]
                i += 1
            else:
                arr[k] = r[j]
                j += 1
            k += 1

        while i < len(l):
            arr[k] = l[i]
            i += 1
            k += 1

        while j < len(r):
            arr[k] = r[j]
            j += 1
            k += 1


# Apply merge_sort to previously created list
merge_sort(a)
print(a)

# Find odd numbers in the list
odd_numbers = [num for num in a if num % 2 != 0]
print(odd_numbers)

# Find even numbers in the list
even_numbers = [num for num in a if num % 2 == 0]
print(even_numbers)

#Find average for both even and odd numbers
avg_odd = sum(odd_numbers) / len(odd_numbers)
print(avg_odd)

avg_even = sum(even_numbers) / len(even_numbers)
print(avg_even)

