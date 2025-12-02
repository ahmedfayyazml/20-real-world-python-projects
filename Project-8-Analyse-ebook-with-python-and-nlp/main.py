with open("miracle_in_the_andes.txt") as file:
    book = file.read()

## Finding the number of the chapter

import  re
pattern = re.compile("Chapter [0-9]+")
chapters = re.split(pattern,book)
chapters = chapters[1:]

