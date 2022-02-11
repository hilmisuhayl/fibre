from fibre import fibre

"""
The first example or template on how to use Fibre:
Iteration over a file.
"""

for line in fibre.s("fibre.py", save=True, suppress=True):
    if len(line) > 25:
        print(line[0:40] + "..." + line[-10:])
        
"""
The second example or template on how to use Fibre:
Printing the strings in a file, without iteration.
"""
        
print(fibre.s("fibre.py", save=True, suppress=True))

"""
The third example or template on how to use Fibre:
Appedning strings to a list.
"""

strings = []

for string in fibre.s("fibre.py", save=True, suppress=True):
    strings.append(string)
