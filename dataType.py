x = 6
print(type(x))

x = "6"
print(type(x))

x = 1+2j
print(type(x))

"""
Output:
<class ‘int’>
<class ‘str’>
<class ‘complex’>
"""

var = 10
print(var)
print(id(var))

var = 11
print(var)
print(id(var))
"""
Output:
10
<memory address>
11
<memory address>
"""

x = True
print(type(x))
x = False
print(type(x))

"""
Output:
<class 'bool'>
<class 'bool'>
"""

x = 'Dicoding'
print(type(x))

"""
Output: 
<class 'str'>
"""

multi_line = """Halo!
Kapan terakhir kali kita bertemu?
Kita bertemu hari Jum’at yang lalu."""

print(multi_line)

"""
Output:
Halo!
Kapan terakhir kali kita bertemu?
Kita bertemu hari Jum’at yang lalu.
"""

# indexing dan slicing
x = 'Dicoding'
print(x[2:])

"""
Output:
coding
"""

multi_line = """Halo!
Kapan terakhir kali kita bertemu?
Kita bertemu hari Jum’at yang lalu."""

print(multi_line)

"""
Output:
Halo!
Kapan terakhir kali kita bertemu?
Kita bertemu hari Jum’at yang lalu.
"""