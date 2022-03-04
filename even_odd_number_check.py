numbers = input("Enter your faviourite numbers: ").split(',')
even = []
odd = []
for num in numbers:
    if int(num) % 2 == 0:
        even.append(num)
    else:
        odd.append(num)
print('Even List', even)
print('Odd List', odd)
count_even = len(even)
count_odd = len(odd)
print(f'There are {count_even} Even numbers')
print(f'There are {count_odd} Odd numbers')