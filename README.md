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
fibre.s("yourfile.exe", suppress=True, save=True)
```
  
This can be also iterated, you can simply iterate it by using the following template
  
```py
strings = fibre.s("yourfile.exe", suppress=True,save=True)

for string in strings:
    print(string)
```
  
## Structure
```ini
(method) s: (f: fibre, suppress="suppress", save="save") -> list
```

`suppress` can be only given the value `True`, or `False`, otherwise it will print out an error
  
`save` works the same as how `suppress` works.
