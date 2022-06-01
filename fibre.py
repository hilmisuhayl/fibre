import re

class fibre(object):
    def __init__(self, file) -> None:
        self.file = file
        
    def save(self, errors: bool, save: bool, filename: str) -> list:
        """
        errors:
            Error restrictions is always a bool. Set as false to ignore errors.
        save:
            Saving the output is always a bool. Set as false to ignore saving.
        filename:
            The filename is always a string, set as None if you want the default name. Only works if save is true.
        """
        
        if errors == False: errors = "ignore"
        elif errors == True: errors = "replace"
        if filename == None: filename = "default.log"
        with open(self.file, "r", errors=errors) as f:
            content = f.read()
            
        s = re.findall("[\x1f-\x7e]{4,}", content)
        if save:  open("{}".format(filename), "w").write("\n".join(s))
        else: pass
        return s
