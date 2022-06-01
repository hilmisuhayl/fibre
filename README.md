<p align="center">
  <img src="https://imgur.com/GrTO4y8.png" alt="Fibre" />
</p>
<p align="center">
<a href="https://discord.gg/79RjTfpzcW" target="_blank">
  <img src="https://img.shields.io/badge/python-3.10-pink.svg" 
  alt="Github Workflow build on master" />
  <img src="https://shields.io/badge/dependencies-recent-pink"/>
</a>
  
# Introduction
## Fibre
A fast, basic way to dump strings from any file, made using regular expressions

### The installation
Click the <kbd>Code</kbd> button and download ZIP.

### Examples
#### Basic iteration
```py
from fibre import fibre as fb
fibre = fb("fibre.py")
content = fibre.save(errors=True, save=False)
for c in content: print(c)
```
#### Saving dump
```py
from fibre import fibre as fb
fibre = fb("fibre.py")
fibre.save(errors=True, save=True)
```

### References
- [Bytes.com | Extract the strings in an exe](https://bytes.com/topic/python/answers/25257-extract-strings-exe)
  
### Stats
![Alt](https://repobeats.axiom.co/api/embed/c7e22fdc4b939bb9d0388093224c43f8eeed773a.svg "Repobeats analytics image")
