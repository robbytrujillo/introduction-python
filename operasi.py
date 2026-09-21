# Operasi pada List, Set, dan String
# List
# len()
contoh_list = [1, 3, 3, 5, 5, 5, 7, 7, 9]

print(contoh_list)
print(len(contoh_list))

"""
Output:
[1, 3, 3, 5, 5, 5, 7, 7, 9]
9
"""

# Set
contoh_list = set([1, 3, 3, 5, 5, 5, 7, 7, 9])

print(contoh_list)
print(len(contoh_list))

"""
Output:
{1, 3, 5, 7, 9}
5
"""

# String
contoh_list = "Belajar Python"

print(contoh_list)
print(len(contoh_list))

"""
Output:
Belajar Python
14
"""

#min() dan max()
angka = [13, 7, 24, 5, 96, 84, 71, 11, 38]
print(min(angka))
print(max(angka))

"""
Output:
5
96
"""

# count()
genap = [2, 4, 4, 6, 6, 6, 8, 10, 10]
print(genap.count(6))

"""
Output:
3
"""

# substring
string = "Belajar Python di Dicoding sangat menyenangkan"
substring = "a"
print(string.count(substring))


"""
Output:
6
"""

# In dan Not In
kalimat = "Belajar Python di Dicoding sangat menyenangkan"
print('Dicoding' in kalimat)
print('tidak' in kalimat)
print('Dicoding' not in kalimat)
print('tidak' not in kalimat)

"""
Output:
True
False
False
True

"""

# Multiple Variable
data = ['shirt', 'white', 'L']
apparel, color, size = data

print(data)
print(apparel)
print(color)
print(size)

"""
Output:
['shirt', 'white', 'L']
shirt
white
L
"""
