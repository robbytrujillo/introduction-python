# One-liner merupakan gaya penulisan pada Python yang memungkinkan Anda untuk membuat sebuah kode hanya dalam satu baris

x = 1
y = 2

temp = x
x = y
y = temp

print("Setelah pertukaran: ")
print("x = ", x)
print("y =",  y)

"""
Output:
Setelah pertukaran: 
x = 2
y = 1
"""

# Operasi menukar dua variable
x = 1
y = 2

x, y = y, x    # One-liner

print('Setelah pertukaran: ')
print('x =', x)
print('y =', y)



"""
Output:
Setelah pertukaran: 
x = 2
y = 1
"""