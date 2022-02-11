<p align="center">
  <img src="https://imgur.com/GrTO4y8.png" alt="Fibre" />
</p>
<p align="center">
  <a href="https://discord.gg/79RjTfpzcW" target="_blank">
    <img src="https://img.shields.io/badge/python-3.10-yellow.svg" alt="Github Workflow build on master" />
  </a>
  
# Fibre
A fast, basic way to dump strings from a file, made using regular expressions

## Features
- Suppress errors
- Save output
  
## Installation
Download the file, make a new file and use the simple following template

```py
from fibre import fibre

fibre.s("yourfile.exe", suppress=True, save=True)
```
  
This can be also iterated, you can simply iterate it by using the following template
  
```py
from fibre import fibre
  
strings = fibre.s("yourfile.exe", suppress=True,save=True)

for string in strings:
    print(string)
```
Another basic example for customizing output
```py
from fibre import fibre

for line in fibre.s("fibre.py", save=True, suppress=True):
    if len(line) > 25:
        print(line[0:40] + "..." + line[-10:])
```
Output
```py
    def s(f, suppress="suppress", save="...):
            raise "FileNotFoundError: No...' option?"
        elif suppress == True:...s == True:
            suppress = "ignore"...= "ignore"
            suppress = False...ss = False
        file = open(f, 'r', errors=suppr...ss).read()
        s = re.findall("[\x1f-\x7e]{4,}"...,}", file)
            with open(".log", "w") as f:..."w") as f:
                for i in s:...or i in s:
                    f.write(i + "\n")...(i + "\n")
        elif save == False:... == False:
            raise "TypeError: save must ... or False"
```
  
## Structure
```ini
(method) s: (f: fibre, suppress="suppress", save="save") -> list
```

`suppress` can be only given the value `True`, or `False`, otherwise it will print out an error
  
`save` works the same as how `suppress` works.
  
## References
- [Bytes.com | Extract the strings in an exe](https://bytes.com/topic/python/answers/25257-extract-strings-exe)
