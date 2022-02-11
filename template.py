from fibre import fibre

for line in fibre.s("fibre.py", save=True, suppress=True):
    if len(line) > 25:
        print(line[0:40] + "..." + line[-10:])