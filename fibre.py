import re

class fibre(object):
    def __init__(self, file) -> None:
        self.file = file
        
    def save(self, errors: bool, save: bool):
        if errors == True: errors = "ignore"
        with open(self.file, "r", errors=errors) as f:
            content = f.read()
            
        s = re.findall("[\x1f-\x7e]{4,}", content)
        if save: open(".log", "w").write("\n".join(s))
        else: pass            
        return s
