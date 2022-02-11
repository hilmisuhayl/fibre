import re

class fibre:
    def s(f, suppress="suppress", save="save"):        
        if f is None:
            raise "FileNotFoundError: No file found, did you mean to use the 'save' option?"
        elif suppress == True:
            suppress = "ignore"
        else:
            suppress = False
        
        file = open(f, 'r', errors=suppress).read()
        
        s = re.findall("[\x1f-\x7e]{4,}", file)
        
        if save == True:
            with open(".log", "w") as f:
                for i in s:
                    f.write(i + "\n")
        elif save == False:
            pass
        else:
            raise "TypeError: save must be either True or False"
        
        return s