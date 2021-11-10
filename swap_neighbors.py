"""
Please write a program that reads data separated by spaces from the keyboard. Then it prints the data, swapped pairwise
(i.e. `data[0]` is swapped with `data[1]`, `data[2]` swapped with `data[3]`, etc.). If the number of data items is odd,
the last item should remain in place.

Example:

    Enter the data: 1 2 3 4 5 6 7 8 9
    2 1 4 3 6 5 8 7 9
"""

# Your code here

lst = list(input("enter data: "))
for elements in lst:
    if elements == ' ':
        lst.remove(elements)

a = round(len(lst))
for i in range(0, a, 2):
    j = i + 1
    lst[i], lst[j] = lst[j], lst[i]

lst = " ".join(lst)

print (lst)
